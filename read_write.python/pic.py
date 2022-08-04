import cv2

img = cv2.imread("sample.jpg")
cv2.imwrite("newsample1.png", img)
cv2.imshow("AI imgae", img)
cv2.waitKey(0)

cv2.destroyAllWindows()
