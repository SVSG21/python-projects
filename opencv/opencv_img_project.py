import cv2
img=cv2.imread('no_way_home.jpeg',0)
img2=cv2.resize(img,(1280,700))
cv2.imshow("opencv project",img2)
#print(img2)  to print numpy array for image
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()