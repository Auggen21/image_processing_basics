import numpy as np
import matplotlib.pyplot as plt
import imageio
img = imageio.imread('einstein.tif')
d = np.zeros(256)
s=0
m,n=img.shape
si=img.size
enimg=np.zeros([m,n]);
out=np.zeros(256)
for i in range(0,256):
    b=np.uint8(img==i);
    s=np.add(s,np.sum(np.ravel(b)));
    out[i]=np.ceil(255*s/si)
    enimg=np.add(enimg, out[i]*b);
plt.figure(1)
plt.subplot(121)
plt.title('Original image')
plt.imshow(img,cmap='gray')
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(enimg,cmap='gray')
plt.title('Histogram Equalized Image')
plt.axis('off')
plt.figure(2)
plt.subplot(121)
plt.title('Original image histogram')
plt.hist(img.flatten(),256,[0,256],linewidth=1.0);
plt.xlabel('bins'), plt.ylabel('count')
plt.subplot(122)
plt.title('Equalised image histogram')
plt.hist(enimg.flatten(),256,[0,256],linewidth=1.0);
plt.xlabel('bins'), plt.ylabel('count')
plt.show()