import cv2

class CharStatus():

    def __init__(self,top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right

    def usernamename_coordonates(self):
        username_bottom_right = (self.top_left[0], self.bottom_right[1] + 5)
        username_top_left = (self.top_left[1] + 5, 0)
        return username_top_left, username_bottom_right

    def level_coordonates(self):
        level_bottom_right = (self.bottom_right[0] + 30, self.bottom_right[1])
        level_top_left = (self.top_left[0] + 30, self.top_left[1])
        return level_top_left, level_bottom_right
