
# coding: utf-8

# # resizing image in aspect to ratio

# In[44]:


from PIL import Image
import cv2
img = cv2.imread("mie.jpg")
import matplotlib.pyplot as plt


# In[43]:


factor = 55
width = int(img.shape[1]*factor/100)
height = int(img.shape[0]*factor/100)
dim = (width,height)
resized_im = cv2.resize(img,dim)
cv2.imwrite("res_img.png",resized_im)


# In[243]:


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
    
    


# In[242]:


type(imag)


# In[216]:


img = cv2.imread(path)
img.shape


# In[251]:


imag.shape


# In[275]:


im = res_img(path,35)


# In[276]:


im = cv2.cvtColor(im,cv2.COLOR_BGR2RGB)


# In[277]:


ims = Image.fromarray(im)


# In[278]:


ims

