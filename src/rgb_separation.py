# this code return the grayscale images
import cv2


sample = cv2.imread('./img/rgb.png')
# to split call split method

blue, green, red = cv2.split(sample)
# cv2.imwrite('./img/blue.png', blue)
# cv2.imwrite('./img/green.png', green)
# cv2.imwrite('./img/red.png', red)

cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)
cv2.imshow('original', sample)
 
cv2.waitKey(0)
cv2.destroyAllWindows()