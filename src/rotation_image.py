import cv2

src_img = cv2.imread('./img/yoda.jpg')
rot_img = cv2.rotate(src_img, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite('./img/yoda_90degRotANTICLOCKWISE.jpg', rot_img)

# Displaying the image 
cv2.imshow('rotated image', rot_img) 
cv2.waitKey(0) 