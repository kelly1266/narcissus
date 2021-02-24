import numpy as nm
import pytesseract
import cv2
from PIL import ImageGrab
import config


def search_twitch():

    return


def image_to_string():
    # Path of tesseract executable
    pytesseract.pytesseract.tesseract_cmd = config.TESSERACT_PATH
    while (True):
        # ImageGrab-To capture the screen image in a loop.
        # Bbox used to capture a specific area.
        #TODO: FIND BBOX DIMENSIONS
        cap = ImageGrab.grab()

        # Converted the image to monochrome for it to be easily
        # read by the OCR and obtained the output String.
        tesstr = pytesseract.image_to_string(
            cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY),
            lang='eng')
        print(tesstr)

    # Calling the function


image_to_string()