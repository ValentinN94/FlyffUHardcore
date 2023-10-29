
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
# import pytesseract
# from PIL import Image
# import cv2
#
# image = Image.open('C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\utils\\screenshoot_lvl_1.PNG')
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
# # Define the region you want to extract text from (in pixel coordinates)
# x1, y1, x2, y2 = 4, 0, 146, 25
# #username_bot_right = (146, 25)
# #username_top_left =  (4, 0)
#
# # Crop the image to the specified region
# cropped_image = image.crop((x1, y1, x2, y2))
# cropped_image.save("geeks.PNG")
#
# # Perform OCR on the cropped image
# text = pytesseract.image_to_string(cropped_image)
#
# # Print the extracted text
# print("Extracted Text:")
# print(text)

#Optimization of text detection
####################################################################################################################
# import pytesseract
# from PIL import Image
# from src.imagetotext.textrecognition import ImageToText
# from src.widgets.charstatus import CharStatus
# import numpy as np
# from matplotlib import pyplot as plt
#
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
#
# image = Image.open('C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\utils\\screenshoot_lvl_1.PNG')
#
# img = cv2.imread("C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\utils\\screenshoot_lvl_1.PNG", cv2.IMREAD_GRAYSCALE)
# img2 = img.copy()
# #current_directory = os.getcwd()
# #image_template = os.path.join(current_directory, 'images', 'char_status', 'LVL_target.PNG')
# template = cv2.imread('C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\images\\char_status\\LVL_target.PNG',  cv2.IMREAD_GRAYSCALE)
# w, h = template.shape[::-1]
#
# # Apply template Matching
# res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
#
#
#
# new_targets = CharStatus(top_left, bottom_right)
#
# username_top_left, username_bottom_right = new_targets.usernamename_coordonates()
#
# # result = cv2.rectangle(img, username_top_left, username_bottom_right , color=(0, 255, 255), lineType=cv2.LINE_4)
# result = img[username_top_left[1]:username_bottom_right[1], username_top_left[0]:username_bottom_right[0]]
#
# img2 = cv2.medianBlur(result,3)
# ret,th1 = cv2.threshold(img2,127,255,cv2.THRESH_BINARY)
# th2 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)
# th3 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# titles = ['Original Image', 'Global Thresholding (v = 127)',
#  'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
# images = [result, th1, th2, th3]
# for i in range(4):
#     plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])
# plt.show()
# #
# text = pytesseract.image_to_string(th2)
# print(text)



# Crop the image to the specified region
# cropped_image = image.crop((x1, y1, x2, y2))
# cropped_image.save("geeks.PNG")
#
# # Perform OCR on the cropped image
#
#
# # Print the extracted text
# print("Extracted Text:")
# print(text)

#Working example of name extraction
####################################################################################################################

# import pytesseract
# from PIL import Image
# from src.imagetotext.textrecognition import ImageToText
# from src.widgets.charstatus import CharStatus
# import numpy as np
# from matplotlib import pyplot as plt
#
#
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#
#
# #image = Image.open('C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\utils\\screenshoot_lvl_1.PNG')
#
# img = cv2.imread("C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\utils\\screenshoot_lvl_1.PNG", cv2.IMREAD_GRAYSCALE)
# img2 = img.copy()
# #current_directory = os.getcwd()
# #image_template = os.path.join(current_directory, 'images', 'char_status', 'LVL_target.PNG')
# template = cv2.imread('C:\\Users\\negru\\PycharmProjects\\FlyffUHardcore\\images\\char_status\\LVL_target.PNG',  cv2.IMREAD_GRAYSCALE)
# w, h = template.shape[::-1]
#
# # Apply template Matching
# res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
# top_left = max_loc
# bottom_right = (top_left[0] + w, top_left[1] + h)
#
#
#
# new_targets = CharStatus(top_left, bottom_right)
#
# username_top_left, username_bottom_right = new_targets.usernamename_coordonates()
#
# # result = cv2.rectangle(img, username_top_left, username_bottom_right , color=(0, 255, 255), lineType=cv2.LINE_4)
# result = img[username_top_left[1]:username_bottom_right[1], username_top_left[0]:username_bottom_right[0]]
#
#
# _, binary_image = cv2.threshold(result, 128, 255, cv2.THRESH_TOZERO)
#
# # Display the original and blurred images (optional)
# cv2.imshow('Original Image', result)
# cv2.imshow('Blurred Image', binary_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
#
# # Perform OCR on the cropped image
# text = pytesseract.image_to_string(binary_image)
#
# # Print the extracted text
# print("Extracted Text:")
# print(text)

# Testing our classes
########################################################################################################################
# from time import time
# from windowcapture import WindowCapture
# from src.detection.vision import Vision
#
# import os
#
# current_directory = os.getcwd()
#
# image_path = os.path.join(current_directory, 'images', 'char_status', 'LVL_target.PNG')
# print(image_path)
#
# wincap = WindowCapture('FlyffHarcore')
#
# lvl_target = Vision(image_path)
#
# loop_time = time()
# wincap.start()
# while (True):
#
#     # if we don't have a screenshot yet, don't run the code below this point yet
#     if wincap.screenshot is None:
#         continue
#
#     # display the processed image
#     points = lvl_target.find(wincap.screenshot, method=cv2.TM_CCOEFF_NORMED)
#
#     # debug the loop rate
#     print('FPS {}'.format(1 / (time() - loop_time)))
#     loop_time = time()
#     if points:
#         break

# Windows capture test
########################################################################################################################
import os
import time
from windowcapture import WindowCapture
from src.detection.vision import Vision
from PyQt5.QtCore import QObject, pyqtSignal
import cv2 as cv

script_directory = os.path.dirname(os.path.abspath(__file__))
src_directory = os.path.join(script_directory, os.path.pardir)
main_directory = os.path.join(src_directory, os.path.pardir)
os.chdir(main_directory)
image_path = os.path.join(os.getcwd(), 'images', 'char_status', 'LVL_target.PNG')
print(f"Full image path: {image_path}")

wincap = WindowCapture('Flyff Universe — Mozilla Firefox')
wincap.list_window_names()
#new_char = Vision(image_path)

#loop_time = time()
#wincap.start()
while True:
    # if wincap.screenshot is None:
    #     continue

    screenshot = wincap.get_screenshot()
    cv.imwrite('result10.jpg', screenshot)
    print('First screenshoot')

    time.sleep(10)
    screenshot2 = wincap.get_screenshot()
    cv.imwrite('result111.jpg', screenshot2)
    print('Second Screenshoot')
    break
