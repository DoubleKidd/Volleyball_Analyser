import cv2
import numpy as np

from court_detection import detect_court

from court_calibration import calibrate_court

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
    
    # Court Detection
    court_contour = detect_court(frame)

    if court_contour is not None:
    	print("worked")
        # Calibration
        x_scale, y_scale = calibrate_court(court_contour)
        
        # Draw the court on the original frame
        cv2.drawContours(frame, [court_contour], -1, (0, 255, 0), 2)
        
        
        # Display the processed frame (e.g., court contours)
        processed_frame = cv2.drawContours(np.zeros_like(frame), [court_contour], -1, (0, 255, 0), 2)
        cv2.imshow('Processed Frame', processed_frame)
    else:
    	print('court_contour is None')
 
    # Display the original frame
    cv2.imshow('Original Video', frame)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
