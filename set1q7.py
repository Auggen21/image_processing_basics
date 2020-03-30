import numpy as np
import matplotlib.pyplot as plt
import imageio

name=input('Enter the image name:')
im = imageio.imread(name)
row,col=im.shape
plt.figure(1)
plt.title('Original image')
plt.imshow(im,cmap='gray')
plt.xticks([]), plt.yticks([])
    
ch=input('Menu\n1.Translation\n2.Rotation \n3.Scaling \n4.Skewing\nEnter Choice:')
if (ch=='1'):
    #translation
    tx=int(input('Enter the translation in X direction:'))
    ty=int(input('Enter the translation in Y direction:'))
    T=[[tx],[ty]]
    out1=np.zeros([row+tx,col+ty])
    for i in range(row):
        for j in range(col):
            P=[[i],[j]]
            Trns=np.uint16(np.ceil(np.add(T,P)))
            out1[Trns[0],Trns[1]]=im[i,j]
    plt.figure(2)
    plt.imshow(out1,cmap='gray')
    plt.title('Translated Image tx=%(one)1.0f ty=%(two)1.0f'%{'one':tx,'two':ty})
    plt.xticks([]), plt.yticks([])
    plt.show()

elif (ch=='2'):
    #Rotation
    degree=int(input('Enter the rotation angle in degree:'))
    angle=degree*np.pi/180
    R=[[np.cos(angle),-np.sin(angle)], [np.sin(angle),np.cos(angle)]]
    first=np.zeros([row,col])
    second=np.zeros([row,col])
    for i in range(0,row):
        for j in range(0,col):
             P=[[i],[j]]
             Rot=np.floor(np.matmul(R,P))
             first[i,j]=Rot[0]
             second[i,j]=Rot[1]             
    fmin=np.min(np.ravel(first))
    smin=np.min(np.ravel(second))
    first=first-fmin+1
    second=second-smin+1
    outsize1=np.int(max(np.ravel(first)))
    outsize2=np.int(max(np.ravel(second)))
    out2=np.zeros([outsize1+1,outsize2+1]);
    for i in range(1,row-1):
        for j in range(1,col-1):
            a=np.int16(first[i,j])
            b=np.int16(second[i,j])
            out2[a,b]=im[i,j]
            out2[a-1,b]=im[i,j]
            out2[a+1,b]=im[i,j]
            out2[a,b-1]=im[i,j]
            out2[a,b+1]=im[i,j]
    plt.figure(3)
    plt.imshow(out2,cmap='gray')
    plt.title('Rotated Image with angle=%1.0f'%degree);
    plt.axis('off')
    plt.show()
    
elif (ch=='3'):    
    #scaling
    sx=float(input('Enter the scaling parameter in x:'))
    sy=float(input('Enter the scaling parameter in y:'))
    S=[[sx, 0],[0,sy]];
    out3=np.zeros([np.int(np.ceil(sx*row)),np.int(np.ceil(sy*col))])
    for i in range(0,row):
        for j in range(0,col):
            P=[[i],[j]]
            Scal=np.int16(np.floor(np.matmul(S,P)));
            out3[Scal[0],Scal[1]]=im[i,j]      
    plt.figure(4)
    plt.imshow(out3,cmap='gray')
    plt.title('Scaled Image sx=%(one)1.1f sy=%(two)1.1f'%{'one':sx,'two':sy})
    plt.axis('off')
    plt.show()
    
elif (ch=='4'):
    #skewing
    skx=float(input('Enter the skewing parameter in x:'))
    sky=float(input('Enter the skewing parameter in y:'))
    SK=[[1, skx],[sky,1]];
    out4=np.zeros([row+np.int(np.ceil(skx*row)),col+np.int(np.ceil(sky*col))])
    for i in range(0,row):
        for j in range(0,col):
            P=[[i],[j]]
            Skew=np.int16(np.floor(np.matmul(SK,P)));
            out4[Skew[0],Skew[1]]=im[i,j]; 
    plt.figure(5)
    plt.imshow(out4,cmap='gray')
    plt.title('Skewed Image skx=%(one)1.1f sky=%(two)1.1f'%{'one':skx,'two':sky})
    plt.axis('off')
    plt.show()
    
else:
    print('Invalid Choice')
        