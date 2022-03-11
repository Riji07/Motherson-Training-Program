import argparse
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
cv2.imshow("image", image)
cv2.waitKey(0)
print(image.shape)
h, w, _= image.shape
print('width:  ', w)
print('height: ', h)
resized=cv2.resize(image,[320,320])
print("Resized Dimensions:",resized.shape)
cv2.imshow("Resized image:",resized)








