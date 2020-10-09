import cv2

DEFAULT_HEIGHT = 720
DEFAULT_WIDTH = 1280
"""
    Change image resolution
    Defaults to  1280 * 720
"""
class Image():
    def __init__(self, image,height=DEFAULT_HEIGHT,width=DEFAULT_WIDTH):
        self.image = image
        self.height = height
        self.width = width
    
    def read(self):
        img = cv2.imread(self.image, cv2.IMREAD_UNCHANGED)
        return img

    def resize(self):
        img = self.read()
        new_dim = (self.width, self.height)
        resized = cv2.resize(img, new_dim, interpolation = cv2.INTER_AREA)
        return resized