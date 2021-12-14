# Single Image Counting Dataset

This dataset contains 33 images of repeating objects with their dot-image labels.
The classes of the repeating objects are varied (flowers, crowd, animals etc...) and the number of repeating instances is between 33 up to 877.

The use of this dataset is for *single* image object counting.

This dataset was published in "Single Image Object Counting and Localizing using Active-Learning" paper (WACV 2022)
https://www.cs.huji.ac.il/~inbarhub/projects/count_WACV/


Here are some images from the dataset: <br>
### **Birds**
![rsz_1birds](https://user-images.githubusercontent.com/11428415/141969128-55921426-3765-4c3d-9020-986f34b61d3f.png)

### **Cars**
![Cars](https://user-images.githubusercontent.com/11428415/141969357-a8a28d77-0685-4e8e-a3fa-5150489100d3.png)

### **Blood cells**
![rsz_1cellsml](https://user-images.githubusercontent.com/11428415/141969509-fbf21d4e-b339-4b6d-80fa-a569e33f5017.png)

### **Crowd**
![rsz_1crowd](https://user-images.githubusercontent.com/11428415/141969625-e9d674e5-db76-47a2-a11b-6aaabced993c.png)

### **Flowers**
![rsz_flowers](https://user-images.githubusercontent.com/11428415/141969821-3996a9d6-da3d-494b-953f-41dcf2d6eb56.png)

### **Water**
![Water](https://user-images.githubusercontent.com/11428415/141969852-3ac8a53c-a147-4ad9-a5e2-83a3518445a7.png)

### **Logs**
![rsz_logs](https://user-images.githubusercontent.com/11428415/141970053-3c8fac1e-d37f-411f-bada-67b830966fb8.png)

------------------------------------------------------------------------------------------------------------------------------------------------
## Running the code

A short python program is also available for evaluating your results. </br>
The program evaulates the number of false positive and false negative over *one* image. The name of the image should be supplied in the command line. </br>

The program assumes two files are in the main directory:
- image_name_gt.png - the `.png' dot file (from the dot directory in this repository).
- image_name_ours.txt - your solution -  a text file contains all the locations of the repeating object (the number of rows of this file is the number of repetition your find).
 
#### Please note:
As we rescale the image before applying our method (more details in the paper), these locations should be a the locations as they appear in the new scale (the image sizes we use can be found in conf.py).

For example: if the ground_truth image is 400x400, and we rescale the image to be 200x200 (as shown in conf.py):
* image_name_gt.png size is 400x400
* The locations in image_name_ours.txt are the locations of the repeating object of your solution of a 200x200 image.

In other words, if you write a code for counting repeating object in a single image, and you resalce the image before applying your code as we did - you should just save the locations as a text file. Otherwise, before saving please resalce the image to fit the size in conf.py and then extract the location of your solution.

You should use the code as follows:
count_gt_vs_output_for_database image_name

for example:
count_gt_vs_output_for_database Chairs

