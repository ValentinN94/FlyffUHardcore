
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

#exmaple of matching and searching for name of char
# #####################################################################
# import cv2
#
#
# # script_directory = os.path.dirname(os.path.abspath(__file__))
#
# img = cv2.imread("C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\utils\\screenshoot_lvl_1.PNG", 0)
# img2 = img.copy()
# template = cv2.imread('C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\utils\\lvl_1_char.PNG', 0)
# w, h = template.shape[::-1]
#
# img = img2.copy()
#
#
# # Apply template Matching
# res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
#
# result = cv2.rectangle(img, top_left,bottom_right , color=(0, 255, 255), lineType=cv2.LINE_4)
#
# user_name_bottom_right = (top_left[0], bottom_right[1])
# user_name_top_left = (top_left[1], 0)
#
# result = cv2.rectangle(img, top_left, bottom_right , color=(0, 255, 255), lineType=cv2.LINE_4)
# cv2.drawMarker(img, user_name_bottom_right, color=[0, 0, 0], thickness=5,
#    markerType= cv2.MARKER_TILTED_CROSS, line_type=cv2.LINE_AA,
#    markerSize=5)
#
# cv2.drawMarker(img, user_name_top_left, color=[0, 255, 0], thickness=5,
#    markerType= cv2.MARKER_TILTED_CROSS, line_type=cv2.LINE_AA,
#    markerSize=5)
#
# result = cv2.rectangle(img, user_name_top_left, user_name_bottom_right , color=(0, 255, 255), lineType=cv2.LINE_4)
#
# cv2.imshow('Result', result)
# cv2.waitKey()
#

#Text extraction example
###################################################################################
import pytesseract
from PIL import Image
import cv2

image = Image.open('C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\utils\\screenshoot_lvl_1.PNG')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Define the region you want to extract text from (in pixel coordinates)
x1, y1, x2, y2 = 4, 0, 146, 25
#username_bot_right = (146, 25)
#username_top_left =  (4, 0)

# Crop the image to the specified region
cropped_image = image.crop((x1, y1, x2, y2))
cropped_image.save("geeks.PNG")

# Perform OCR on the cropped image
text = pytesseract.image_to_string(cropped_image)

# Print the extracted text
print("Extracted Text:")
print(text)