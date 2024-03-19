import cv2
import numpy as np

from court_detection import detect_court

import show_on_court_frame

from court_calibration import calibrate_court
import cv2
import numpy as np

# video_path = input("Please enter the name of your volleyball file path (an mp4) (I should test if non mp4 works)")

video_path = '/Users/BenKidd/Desktop/Volleyball_Data/Videos_in_MP4/pexels-pavel.mp4'
cap = cv2.VideoCapture(video_path)

frame_num = -1
while True:
    ret, frame = cap.read()
    frame_num += 1
    print ('Frame: '+str(frame_num))
    if not ret:
        break
    
    # Preprocess the frame

    court_contours, court_lines = detect_court(frame)
    green = (0, 255, 0)
    red = (0, 0, 255)
    show_on_court_frame.colour_lines(frame, court_lines, green)
    show_on_court_frame.colour_contours(frame, court_contours, red)

    if court_contours is None:
        print('court_contour is None')

        # Display the original frame
        cv2.imshow('Original Video', frame)
        continue

    print("worked")
    # Calibration
    # print("court_contour:\n",court_contour)
    # x_scale, y_scale = calibrate_court(court_contour)
        
    # Draw the court on the original frame
    # cv2.drawContours(frame, [court_contour], -1, (0, 255, 0), 2)
        
    # # Draw the court on the processed frame
    # # Extract the numpy array from the tuple
    # # rectangles = court_contour[0]
    # # Draw each rectangle
    # # for rectangle in rectangles:    
    # #     x, y, w, h = rectangle[0]
    # #     processed_frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the processed frame (e.g., court contours)
    # processed_frame = cv2.drawContours(np.zeros_like(frame), [court_contour], -1, (0, 255, 0), 2)
    cv2.imshow('Processed Frame', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
