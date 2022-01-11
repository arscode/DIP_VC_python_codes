import cv2

testImage = cv2.imread('./img/yoda.jpg')
grayImage = cv2.cvtColor(testImage, cv2.COLOR_BGR2GRAY)

cv2.imshow('Original image', testImage)
cv2.imshow('Gray image', grayImage)
cv2.imwrite('./img/yoda_gray.jpg', grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()