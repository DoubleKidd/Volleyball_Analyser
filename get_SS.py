import cv2

read_file = '/Users/BenKidd/Desktop/Volleyball_Data/Videos_in_MP4/pexels-pavel.mp4'
write_file = '/Users/BenKidd/Desktop/Volleyball_Data/Pictures_in_png/pexels-pavel_frame_1.png'

# Open the video file
video_capture = cv2.VideoCapture(read_file)

# Check if the video opened successfully
if not video_capture.isOpened():
    print("Error: Could not open video.")
    exit()

# Read the first frame
ret, frame = video_capture.read()

# Check if the frame was read successfully
if not ret:
    print("Error: Could not read frame.")
    exit()

# Release the video capture object
video_capture.release()

# Save the first frame as a PNG file
cv2.imwrite(write_file, frame)

print("First frame saved as '"+write_file+"'.")