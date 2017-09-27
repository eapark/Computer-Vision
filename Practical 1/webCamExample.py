# Computer Vision Course (CSE 40535/60535)
# University of Notre Dame, Fall 2017
# ________________________________________________________________
# Adam Czajka, Andrey Kuehlkamp, September 2017


# 1. Follow these instructions to OpenCV and Python:
# On Windows - http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_setup/py_setup_in_windows/py_setup_in_windows.html
# On Linux   - http://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/
# On Mac     - http://www.pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/
#
# 2. Try to run the following code using the command "python webCamExample.py".
# It should start your webcam, show the preview and the captured image.
# Press Esc to stop the loop.

import cv2

cam = cv2.VideoCapture(0)

while (True):
    retval, img = cam.read()
    res_scale = 0.5             # rescale the input image if it's too large
    img = cv2.resize(img, (0,0), fx=res_scale, fy=res_scale)

    cv2.imshow("Live WebCam", img)

    action = cv2.waitKey(1)
    if action==27:
        break
    elif action==ord('c'):      # capture
        cap_img = img

        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(cap_img,    # image
                    'I can write or draw on an image!!',  # text
                    (10,50),    # start position
                    font,       # font
                    1.0,        # size
                    (0, 255, 0),# BGR color
                    1,          # thickness
                    cv2.LINE_AA )          # type of line
        cv2.line(cap_img,   # image
                 (100,100), # start point
                 (300,300), # end point
                 (0,0,255), # color
                 4)         # thickness

        cv2.imshow("Captured image", cap_img)