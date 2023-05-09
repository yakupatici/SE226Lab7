
import cv2

image = cv2.imread('/Users/jacob/pythonProject/Lab7/WorldCupMessi.jpeg')

blue, green, red = cv2.split(image)

cv2.imshow('Blue Channel', blue)
cv2.imshow('Green Channel', green)
cv2.imshow('Red Channel', red)

green *=0

new_image = cv2.merge((blue, green , red))

cv2.imshow('New Image', new_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
