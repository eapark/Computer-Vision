# Computer Vision Course (CSE 40535/60535)
# University of Notre Dame, Fall 2017
# ________________________________________________________________
# Adam Czajka, Andrey Kuehlkamp, September 2017

# Instructions
#
# In step 1 you have selected a good range of pixel values for RGB and HSV
# channels. All this information can be used to detect an object
# of interest in the live camera feed.
#
# Say if you want to detect a blue M&M candy, and after analysing the blue
# candy histogram, you find out that:
# - It has a certain red and green value ranges
# - It also has a significant blue values
#
# Here are your tasks for today:
#
# Task 1:
# - Select one candy that you want to track and set the RGB
#   channels to the selected ranges (found by hsvSelection.py).
# - Check if HSV color space works better. Can you ignore one or two
#   channels when working in HSV color space? Why?
# - Try to track candies of different colors (blue, yellow, green).
# - Upload your best solution for one candy/color to your Dropbox as colorTracking1.py
#
# Task 2:
# - Adapt your code to track multiple candies of *the same* color simultaneously.
# - Upload your solution to your Dropbox as colorTracking2.py
#
# Task 3:
# - Adapt your code to track multiple candies of *different* colors simultaneously.
# - Upload your solution to your Dropbox as colorTracking3.py


import cv2
import numpy as np

cam = cv2.VideoCapture(0)

while (True):
    retval, img = cam.read()

    res_scale = 0.5             # rescale the input image if it's too large
    img = cv2.resize(img, (0,0), fx = res_scale, fy = res_scale)

    # detect selected color (OpenCV uses BGR instead of RGB)
    # this example is tuned to blue, in a relatively dark room
    #lower = np.array([40, 75, 175])
    #upper = np.array([70, 100,200])
    #objmask = cv2.inRange(img, lower, upper)

    # # uncomment this if you want to use HSV

    # This is for detecting an orange jelly bean
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 150, 150])
    upper = np.array([15, 230, 230])
    objmask = cv2.inRange(hsv, lower, upper)

    # you may use this for debugging
    cv2.imshow("Binary image", objmask)

    # Resulting binary image may have large number of small objects.
    # You may check different morphological operations to remove these unnecessary
    # elements. You may need to check your ROI defined in step 1 to
    # determine how many pixels your candy may have.
    kernel = np.ones((15,15), np.uint8)
    objmask = cv2.morphologyEx(objmask, cv2.MORPH_OPEN, kernel=kernel)
    objmask = cv2.morphologyEx(objmask, cv2.MORPH_DILATE, kernel=kernel)

    cv2.imshow("Image after morphological operations", objmask)

    # find connected components
    cc = cv2.connectedComponents(objmask)
    ccimg = cc[1].astype(np.uint8)

    # find contours of these objects
    imc, contours, hierarchy = cv2.findContours(ccimg,
                                                cv2.RETR_TREE,
                                                cv2.CHAIN_APPROX_SIMPLE)

    # You may display the countour points if you want:
    # cv2.drawContours(img, contours, -1, (0,255,0), 3)

    if contours:
        # use just the first contour to draw a rectangle
        x, y, w, h = cv2.boundingRect(contours[0])
        # do not show very small objects
        if w > 20 or h > 20:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
            cv2.putText(img,                        # image
                        "Here's my candy!",         # text
                        (x, y-10),                  # start position
                        cv2.FONT_HERSHEY_SIMPLEX,   # font
                        0.7,                        # size
                        (0, 255, 0),                # BGR color
                        1,                          # thickness
                        cv2.LINE_AA)                # type of line

    cv2.imshow("Live WebCam", img)

    action = cv2.waitKey(1)
    if action==27:
        break
