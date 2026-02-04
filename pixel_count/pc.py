# Requires use of OpenCV and NumPy
# Installed with bash command: pip install opencv-python numpy

import cv2
import numpy as np

def count_colour_pixels(image_path, target_colour_rgb):
    """
    Docstring for count_colour_pixels
    
    :param image_path: Path to the image file.
    :param target_colour_rgb: The target colour as an RGB tuple (R,G,B)
    :return: The count of pixels matching the target colour.
    """

    # Read the image, OpenCV reads in BGR (Blue, Green, Red) format by default.
    img_bgr = cv2.imread(image_path)
    if img_bgr is None:
        print(f"Error: Could not open or find the image at {image_path}")
        return 0
    
    # Switch values from RGB to BGR, and setting strict bounds
    target_colour_bgr = (target_colour_rgb[2], target_colour_rgb[1], target_colour_rgb[0])
    lower_bound_bgr = np.array([target_colour_bgr[0]-5,target_colour_bgr[1]-5,target_colour_bgr[2]-5])
    upper_bound_bgr = np.array([target_colour_bgr[0]+5,target_colour_bgr[1]+5,target_colour_bgr[2]+5])

    # Creating a mask for target colour
    mask = cv2.inRange(img_bgr,lower_bound_bgr,upper_bound_bgr)

    # If pixel matches target colour, mask pixel will be 255 (white), others 0 (black),
    # Therefore, should be counting non-zero pixels.
    count = cv2.countNonZero(mask)
    return count
