import numpy as np
import cv2
import copy

# Make this return only the court corner verticies? 
# Perhaps also the cernteer line verticies
def detect_court(frame):
    lines = get_lines(frame)

    intersections = get_intersections(lines, frame)

    # corners = detect_corners_ShiTomasi(frame)
    # corners = detect_corners_harris(frame)
    
    return intersections, lines

def get_lines(frame):
    # Step 2.1: Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 2.2: Apply Canny edge detector
    edges = cv2.Canny(gray, 50, 150)

    # Step 3: Hough Transform
    lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=100, maxLineGap=10)

    return lines

def get_intersections(lines, frame):
    # Find intersections
    intersections = find_intersections(lines)
    if intersections is not None:

        # Get the dimensions of the frame using the shape attribute
        height, width, channels = frame.shape

        # Remove impossible intersections (off screen)
        # Should remove/change this to allow for court coners which are outside of the recording?
        # for intersection in intersections:
        #     x, y = intersection
        #     if x > width or y > height:
        #         intersections.remove(intersection)

        # This method below works to minimise the list, however can end up picking up the wrong intexceptions, perhaps a combinations of this an FAST could be used to be more accurate?
        # use intersections then fast corner and check if there is an intersection in the fast area as well

        # Specify the rectangular area around each point allowed (x_change, y_change)
        area_rect = (50, 100)

        threshold_count = 1  # Set your desired threshold count
        # 10 line intersections on a volleyball court
        if len(intersections) > 10:
            orignal_intersections = intersections
            while len(intersections) > 10:
                threshold_count += 1
                intersections = orignal_intersections.copy()
                # Remove intersection without enough other intersection nearby
                intersections = remove_intersections_less_than_threshold_amount_in_area(intersections, area_rect, threshold_count)
                if len(intersections) <=10:
                    intersections = remove_intersections_less_than_threshold_amount_in_area(orignal_intersections, area_rect, threshold_count-1)
                    break

    return intersections


def find_intersections(lines):
    intersections = []
    for i in range(len(lines)):
        for j in range(i + 1, len(lines)):
            line1 = lines[i][0]
            line2 = lines[j][0]

            x1, y1, x2, y2 = line1
            x3, y3, x4, y4 = line2

            # Calculate the denominator
            denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

            # Check if the lines are not parallel (denominator is not zero)
            if denominator != 0:
                # Calculate the intersection point
                intersection_x = ((x1*y2-y1*x2)*(x3-x4) - (x1-x2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))
                intersection_y = ((x1*y2-y1*x2)*(y3-y4) - (y1-y2)*(x3*y4-y3*x4)) / ((x1-x2)*(y3-y4) - (y1-y2)*(x3-x4))

                intersections.append((int(intersection_x), int(intersection_y)))

    return intersections

# this is very slow, find a better way?
def remove_intersections_less_than_threshold_amount_in_area(intersections, area_rect, threshold):
    x_change, y_change = area_rect
    x_change = x_change//2
    y_change = y_change//2
    new_intersections = []

    for intersection in intersections:
        x, y = intersection
        # Set allowed max and min x and y for each intersection
        x_min = x - x_change
        x_max = x + x_change
        y_min = y - y_change
        y_max = y + y_change

        # Count number of intersections nearby
        count = 0
        x_total = x
        y_total = y
        indexes_to_remove = []
        for i in range(len(intersections)):
            w, v = intersections[i]
            if x_min <= w <= x_max and y_min <= v <= y_max:
                count += 1
                x_total += w
                y_total += v
                indexes_to_remove.append(i)
        # If there are enough intersection, add the average intercetion point to the list
        if count >= threshold:
            new_intersections.append((x_total//count, y_total//count))
            for i in range(len(indexes_to_remove)-1, 0, -1):
                intersections.pop(indexes_to_remove[i])
    return new_intersections

#This method doesn't work nearly as well as my previous method
def detect_corners_ShiTomasi(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect corners using Shi-Tomasi algorithm
    corners = cv2.goodFeaturesToTrack(gray, maxCorners=100, qualityLevel=0.01, minDistance=10)

    # Convert corners to integers
    corners = np.int0(corners)

    # Draw corners on the frame
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)

    return corners

#This method doesn't work nearly as well as my previous method
def detect_corners_harris(frame):
    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect corners using Harris Corner Detection
    corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Threshold for an optimal value, it may vary depending on the image and lighting conditions
    corners_thresh = 0.01 * corners.max()

    # Draw circles on the original frame for the detected corners
    for y in range(corners.shape[0]):
        for x in range(corners.shape[1]):
            if corners[y, x] > corners_thresh:
                cv2.circle(frame, (x, y), 5, (255, 0, 0), -1)  # Draw blue circle

    return corners