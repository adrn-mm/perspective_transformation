# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 19:16:01 2018

@author: @adriantoto
"""
# Libraries
import numpy as np

# Open webcam 
cap = cv2.VideoCapture(0)

while True:
    # While webcam opened
    _, frame = cap.read()
    
    # Draw points on paper's edges
    cv2.circle(frame, (155, 120), 5, (0, 0, 255), -1)
    cv2.circle(frame, (480, 120), 5, (0, 0, 255), -1)
    cv2.circle(frame, (20, 475), 5, (0, 0, 255), -1)
    cv2.circle(frame, (620, 475), 5, (0, 0, 255), -1)
 
    # Perpective Transformation methods
    pts1 = np.float32([[155, 120], [480, 120], [20, 475], [620, 475]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
 
    result = cv2.warpPerspective(frame, matrix, (500, 600))
 
    # Show output
    cv2.imshow("Frame", frame)
    cv2.imshow("Perspective transformation", result)
    
    # Break the process
    if((cv2.waitKey(1) & 0xFF) == ord('q')):
        break

# end of process
cap.release()
cv2.destroyAllWindows()
 
