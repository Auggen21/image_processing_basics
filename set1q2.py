import matplotlib.pyplot as plt
import imageio
img = imageio.imread('mri2.jpg')
negative=abs(255-img); 
plt.subplot(121)
plt.imshow(img);
plt.title('Original Image')
plt.axis('off') 
plt.subplot(122)
plt.imshow(negative)
plt.title('Negative Image')
plt.axis('off')
plt.show()