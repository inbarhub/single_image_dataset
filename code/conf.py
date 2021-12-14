import numpy as np

def get_image_size(image_name):
    print(image_name)
    if image_name == "Water":
        im_size = [276,404]
    elif image_name == "Cells_small":
        im_size = [400,400]
    elif image_name == "Cells_large":
        im_size = [320,320]
    elif image_name == "Beer":
        im_size = [280,412]
    elif image_name == "Pills":
        im_size = [100,280]
    elif image_name == "Flowers":
        im_size = [200,424]
    elif image_name == "Sheep":
        im_size = [376,832]
    elif image_name == "Cars":
        im_size = [188,412]
    elif image_name == "Audience":
        im_size = [372,620]
    elif image_name == "Fish":
        im_size = [400,700]
    elif image_name == "Matches":
        im_size = [272,380]
    elif image_name == "CarsBg":
        im_size = [612,568]
    elif image_name == "Birds":
        im_size = [320,480]
    elif image_name == "Parasol":
        im_size = [244,196]
    elif image_name == "Beach":
        im_size = [420,860]
    elif image_name == "Wall":
        im_size = [224,224]
    elif image_name == "Cookies":
        im_size = [200,260]
    elif image_name == "Chairs":
        im_size = [360,480]
    elif image_name == "Candles":
        im_size = [160,300]
    elif image_name == "Logs":
        im_size = [236,324]
    elif image_name == "Peas":
        im_size = [152,228]
    elif image_name == "CokeReg":
        im_size = [212,580]
    elif image_name == "CokeDiet":
        im_size = [212,580]
    elif image_name == "Antartica":
        im_size = [2*136,2*476]
    elif image_name == "Oranges":
        im_size = [400,272]
    elif image_name == "Discussion":
        im_size = [600,800]
    elif image_name == "Hats":
        im_size = [304,600]
    elif image_name == "Fish097":
        im_size = [412,300]
    elif image_name == "Fish107":
        im_size = [412,300]
    elif image_name == "Birds002":
        im_size = [624,964]
        window_loc = [[559,485]]
    elif image_name == "Bees":
        im_size = [248,980]
    elif image_name == "Soldiers":
        im_size = [252,396]
    elif image_name == "RealCells":
        im_size = [488,488]
    else:
        print(image_name + ' not found image name')
        exit()
    return im_size
