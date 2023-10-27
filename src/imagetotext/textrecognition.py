import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class ImageToText():
    def __init__(self, image):
        self.image = image

    def region_of_interest(self, top_left, bottom_right):
        region_of_interest_img = self.image[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        return region_of_interest_img

    def roi_to_text(self, roi):
        text = pytesseract.image_to_string(roi)
        return text
