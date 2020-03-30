import numpy as np
import matplotlib.pyplot as plt
import imageio
import cv2
im = cv2.imread('einstein_orig.tif')
cv2.imshow('Original Image',im)

# Brightness
im=np.double(im)
b=im+100;
b=np.clip(b,0,255);
#cv2.imshow('Brightness Enhanced',np.uint8(b))

# contrast
alpha=.1;
beta=3;
gamma=.1;
low=70;
high=180;
out1=alpha*np.multiply(im,np.uint(im<low));
out2=beta*np.multiply((im-low),np.uint((low<im)&(im<high)))+out1
out3=gamma*np.multiply((im-high),np.uint(high<im))+out2
con=np.add(out1,out2,out3);
con=np.clip(con,0,255);
#cv2.imshow('Contrast Enhanced',np.uint8(con))
#cv2.waitKey(0)

#complement
im2=imageio.imread('mars_moon_phobos.tif');
plt.figure(2)
plt.subplot(121),
plt.imshow(im2,cmap='gray'),plt.title ('Original Image')
plt.axis('off')
d=256-im2;
plt.subplot(122)
plt.imshow(d,cmap='gray'),plt.title ('Complement of  Image')
plt.axis('off')

#binary contrast image
im3=imageio.imread('spot_shaded_text_image.tif');
plt.figure(3)
plt.subplot(121),
plt.imshow(im3,cmap='gray'),plt.title ('Original Image')
plt.axis('off')
t=25;
e=255*(im3>t);
e=np.uint8(e);
plt.subplot(122),plt.imshow(e,cmap='gray'),plt.title ('Binary Image Enhancement')
plt.axis('off')

#brightness slicing
im4=imageio.imread('kidney.tif');
plt.figure(4)
plt.subplot(131),
plt.imshow(im4,cmap='gray'),plt.title ('Original Image')
plt.axis('off')
im4=np.double(im4)
lo=180;
hi=250;
fst=(lo<im4);
lst=(im4<hi);
rng=(fst==lst);
f=rng*256;
plt.subplot(132),plt.imshow(np.uint16(f),cmap='gray'),plt.title ('Brightness Slicing without background')
plt.axis('off')
fb=f+im4;
plt.subplot(133),plt.imshow(np.uint16(fb),cmap='gray'),plt.title('Brightness Slicing with background')
plt.axis('off')

#lowpass filtering
im5=imageio.imread('test_pattern_blurring_orig.tif');
a=np.uint16(im5)
plt.figure(5)
plt.subplot(121),
plt.imshow(im5,cmap='gray'),plt.title ('Original Image')
plt.axis('off')
ws=3;
avg=np.ones([ws,ws])
pd=int((ws-1)/2);
start=ws-pd-1;
row,col=im5.shape
f=np.pad(im5,[(pd,pd)],'constant')
r,c=f.shape;
lpf=np.zeros([row,col])
for i in range(start,r-pd):
    for j in range(start,c-pd):
        window=f[(i-pd):(i+pd+1),(j-pd):(j+pd+1)];
        su=0;        
        for s in range(ws):
            for t in range(ws):
                m=np.multiply(avg[s][t],window[s][t])
                su=np.add(su,m)
        lpf[i-start,j-start]=su;
out1=lpf/9;
plt.subplot(122)
plt.imshow(np.uint8(out1),cmap='gray'),plt.title ('Low Pass Filtered Image')
plt.axis('off')

#highpass filtering
im6 = imageio.imread('cameraman.tif')
a1=np.uint16(im6)
plt.figure(6)
plt.subplot(121),
plt.imshow(a1,cmap='gray'),plt.title ('Original Image')
ws=5;
pd=int((ws-1)/2);
start=ws-pd;
lap=-1*np.ones([ws,ws])
lap[pd,pd]=-1*np.sum(np.ravel(lap))-1
f=np.pad(a1,[(pd,pd)],'edge')
r,c=f.shape;
row,col=a1.shape
hpf=np.zeros([row,col])
for i in range(start,r-pd):
    for j in range(start,c-pd):
        window=f[i-pd:i+pd+1,j-pd:j+pd+1];
        su=0;        
        for s in range(ws):
            for t in range(ws):
                m=np.multiply(lap[s][t],window[s][t])
                su=np.add(su,m)
        hpf[i-start-1,j-start-1]=su;
out2=np.clip(hpf,0,255);
plt.subplot(122)
plt.imshow((out2),cmap='gray'),plt.title ('High Pass Filtered Image')
plt.axis('off')
plt.show()

