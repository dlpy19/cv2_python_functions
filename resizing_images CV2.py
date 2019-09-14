
# coding: utf-8

# # resizing image in aspect to ratio

# to resize an image with respect to ratio in open-cv you need the following:
#  1. factor which is integer which indicate how much the new size woill be different 
# from the original size.
#  For exammple 50 means new size will 50% less than original whearas  200 meabs twice
#   2. width * factor 
#   3. height * factor
#   4. dimintion which is (width,height)
#   5. resized_im = cv2.resize(img,dim)
#factor = 55 # any integer 
#width = int(img.shape[1]*factor/100)
#height = int(img.shape[0]*factor/100)
#dim = (width,height)
#resized_im = cv2.resize(img,dim)
#cv2.imwrite("res_img.png",resized_im)


def res_img(path=str,thresh=int):
    import cv2
    image = cv2.imread(path)
    w = int(image.shape[1]*thresh/100)
    h = int(image.shape[0]*thresh/100)
    dim = (w,h)
    output = cv2.resize(image,dim)
    #print(output.shape)
    if save is True:
        return cv2.imwrite("saved.jpg", output)
    return output
    

