import cv2
import os
import numpy as np
def saveSlide(frame,slide_num):
    frame=processSlide(frame)
    cv2.imwrite(f'Images/{slide_num}.jpg',frame)


def deleteImages(image_folder="Images"):
    for f in os.listdir(image_folder):
        os.remove(f"{image_folder}/{f}")

def processSlide(image):
    y_nonzero, x_nonzero, _ = np.nonzero(image)
    return image[np.min(y_nonzero):np.max(y_nonzero), np.min(x_nonzero):np.max(x_nonzero)]