import cv2

def resize_image(image, width=300, height=400):
    return cv2.resize(image, (width, height))
