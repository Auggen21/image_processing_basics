import os
import matplotlib.pyplot as plt
import imageio
image = imageio.imread('cameraman.tif')
plt.figure()
plt.subplot(121)
plt.imshow(image,cmap='gray')
plt.title('Original Image')
plt.xticks([]), plt.yticks([]) 
statinfo=os.stat('cameraman.tif')
a=statinfo.st_size
imageio.imsave('new1.jpg',image)
newimage=imageio.imread('new1.jpg')
plt.subplot(122)
plt.imshow(newimage,cmap='gray')
plt.xticks([]), plt.yticks([])
plt.title('Copied Image')
plt.show() 
print('Image Information')
print ('Image Shape',newimage.shape)
print ('Image Size',newimage.size)
print ('Image Datatype',newimage.dtype)
statinfo=os.stat('new1.jpg')
b=statinfo.st_size
cr=a/b
print ('Compression ratio',cr)