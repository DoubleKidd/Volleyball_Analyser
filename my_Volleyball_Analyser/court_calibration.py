import cv2

court_real_dimensions = {'width': 18.0, 'length': 27.0}  # Dimensions in meters

def calibrate_court(court_contour):
    # Assuming court dimensions are available in the real world
    img_width, img_length = cv2.boundingRect(court_contour)[2:]
    
    # Calculate the scaling factors
    x_scale = court_real_dimensions['width'] / img_width
    y_scale = court_real_dimensions['length'] / img_length
    
    return x_scale, y_scale
