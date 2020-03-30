import numpy as np
import matplotlib.pyplot as plt
import imageio
img = imageio.imread('cameraman.tif')
d = np.zeros(256)
m,n=img.shape
for i in range(0,255):
    b=np.uint8(img==i);
    d[i]=np.sum(np.ravel(b));
plt.figure(1)
plt.subplot(121)
plt.imshow(img,cmap='gray')
plt.title('Image')
plt.axis('off')
plt.subplot(122)
plt.stem(d)
plt.title('Histogram')
plt.xlabel('bins'), plt.ylabel('count')
plt.show()