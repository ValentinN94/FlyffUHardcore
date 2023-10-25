
# This is a convert images to greyscale example
#####################################################################

import cv2

# Load the input image
# image = cv2.imread('new_char_gold.PNG')
# cv2.imshow('Original', image)
# cv2.waitKey(0)
#
# # Use the cvtColor() function to grayscale the image
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('Grayscale', gray_image)
# cv2.waitKey(0)
#
# # Load the input image
# image2 = cv2.imread('new_char_orig.PNG')
# cv2.imshow('Original2', image2)
# cv2.waitKey(0)
#
# # Use the cvtColor() function to grayscale the image
# gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
#
# cv2.imshow('Grayscale2', gray_image2)
# cv2.waitKey(0)

# Window shown waits for any key pressing event
#cv2.destroyAllWindows()

# this is a matching techniques comparison
#####################################################################

# import cv2
# from matplotlib import pyplot as plt
#
# img = cv2.imread('../images/screenshoot.PNG', 0)
# img2 = img.copy()
# template = cv2.imread('../new_char_gold.PNG', 0)
# w, h = template.shape[::-1]
#
# # All the 6 methods for comparison in a list
# methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
#             'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
#
# for meth in methods:
#     img = img2.copy()
#     method = eval(meth)
#
#     # Apply template Matching
#     res = cv2.matchTemplate(img,template,method)
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#
#     # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
#     if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#
#     cv2.rectangle(img,top_left, bottom_right, color=(0, 255, 0), lineType=cv2.LINE_4)
#
#     plt.subplot(121),plt.imshow(res,cmap = 'gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122),plt.imshow(img,cmap = 'gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#
#     plt.show()

import cv2
from matplotlib import pyplot as plt
import os
from PIL import Image

# script_directory = os.path.dirname(os.path.abspath(__file__))

img = cv2.imread("C:\\Users\\vnegru\\PycharmProjects\\FlyffUHardcore\\utils\\screenshoot_lvl_1.PNG", 0)
img2 = img.copy()
template = cv2.imread('C:\\Users\\vnegru\\PycharmProjects\\FlyffUHardcore\\utils\\lvl_1_char.PNG', 0)
w, h = template.shape[::-1]

img = img2.copy()


# Apply template Matching
res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

#result = cv2.rectangle(img, top_left,bottom_right , color=(0, 255, 255), lineType=cv2.LINE_4)

x1 = (0, top_left[0])
x2 = top_left
y1 = (top_left[0],top_left[1])
y2 = bottom_right

result = cv2.rectangle(img, x1,y2 , color=(0, 255, 255), lineType=cv2.LINE_4)

cv2.imshow('Result', result)
cv2.waitKey()


