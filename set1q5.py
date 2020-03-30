import numpy as np
import matplotlib.pyplot as plt
import imageio
img = imageio.imread('embedded_square_noisy_512.tif')
a=np.double(img)
m,n=a.shape
ws=7;
pd=int((ws-1)/2);
start=ws-pd-1;
f=np.pad(a,[(pd,pd)],'constant')
row,col=f.shape;
out=np.zeros((256),'int16')
outres=np.zeros([m,n],'int16')
for i in range(start,row-pd-1,ws):
    for j in range(start,col-pd-1,ws):
        window=f[i-pd:i+pd+1,j-pd:j+pd+1];
        s=0;  
        enimg=np.zeros([ws,ws]);
        for k in range(1,256):
            b=np.uint8(window==k);
            s=np.add(s,np.sum(np.ravel(b)));
            out[k]=np.ceil(255*(s)/(ws*ws))
            enimg=np.add(enimg,out[k]*b)
        outres[i-start:i-start+ws,j-start:j-start+ws]=enimg;
plt.figure(1)
plt.subplot(121)
plt.title('Original image')
plt.imshow(img,cmap='gray')
plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.imshow(outres,cmap='gray')
plt.title('Local Histogram Equalized Image')
plt.axis('off')
plt.show()
