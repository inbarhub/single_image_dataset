from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as image
from conf import get_image_size
import numpy as np
import scipy.misc
import os
import os.path

import sys

image_name = sys.argv[1]

patch_sz = 15
gt_color = [255,255,255]

im_size = get_image_size(image_name)
gt_image = np.array(Image.open('../dots/' + image_name+'_gt.png'))
gt_image = gt_image[:,:,:3]
print(image_name+'_gt.png')

res = np.loadtxt(image_name+'_ours.txt')
[row_ours,col_ours] = np.unravel_index(np.int32(res), [im_size[0], im_size[1]])

tmp = np.where(np.reshape(gt_image[:,:,0],-1) == gt_color[0])[0]
tot_tmp = tmp
tmp = np.where(np.reshape(gt_image[:,:,1],-1) == gt_color[1])[0]
tot_tmp = np.intersect1d(tmp, tot_tmp)
tmp = np.where(np.reshape(gt_image[:,:,2],-1) == gt_color[2])[0]
tot_tmp = np.intersect1d(tmp, tot_tmp)
[row_gt,col_gt] = np.unravel_index(tot_tmp, [gt_image.shape[0], gt_image.shape[1]])

ratio = [np.float(gt_image.shape[0])/im_size[0],np.float(gt_image.shape[1])/im_size[1]]
row_gt = np.int32(row_gt/ratio[0])
col_gt = np.int32(col_gt/ratio[1])


matched_pt = []
gt_count = row_gt.shape
count = row_ours.shape
row_ours_copy = row_ours.copy()
col_ours_copy = col_ours.copy()
row_gt_copy = row_gt.copy()
col_gt_copy = col_gt.copy()

r = 2*patch_sz/3
counter = 0
for i in range(0,len(row_gt)):
    match = []
    for j in range(0,len(row_ours)):
        if np.power(row_gt[i]-row_ours[j],2)+np.power(col_gt[i] - col_ours[j],2) < np.power(r,2) and row_ours_copy[j] != -1:
            match.append([j,np.power(row_gt[i]-row_ours[j],2)+np.power(col_gt[i]-col_ours[j],2)])
    if len(match) > 0:
        counter = counter+1
        match = np.stack(match)
        closer = np.argmin(match[:,1])
        row_ours_copy[match[closer,0]] = -1
        matched_pt.append(i)
if len(matched_pt)>0:
    matched_pt = np.stack(matched_pt)
row_gt_copy = np.delete(row_gt_copy,matched_pt)
col_gt_copy = np.delete(col_gt_copy,matched_pt)
col_ours_copy = np.delete(col_ours_copy,np.where(row_ours_copy == -1)[0])
row_ours_copy = np.delete(row_ours_copy,np.where(row_ours_copy == -1)[0])

print("FN: " + str(row_ours_copy.shape[0])+"\n")
print("FP: " + str(row_gt_copy.shape[0])+"\n")
print("gt_count: " + str(gt_count[0])+"\n")
print("our count: " + str(count[0])+"\n")
