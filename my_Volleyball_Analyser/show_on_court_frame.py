import cv2

def colour_contours(frame, court_contours, colour):
    if court_contours is not None:
        # Colour the contours
        for contour in court_contours:
            cv2.circle(frame, contour, 5, colour, -1)

def colour_lines(frame, court_lines, colour):
    if court_lines is not None:
        # Colour the contours
        for line in court_lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), colour, 2)