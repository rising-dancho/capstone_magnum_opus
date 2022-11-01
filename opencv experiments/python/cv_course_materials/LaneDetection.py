import cv2
import numpy as np


def draw_the_lines(image, lines):
    # create a distinct image for the lines [0,255] - all 0 values means black image
    lines_image = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)

    # there are (x,y) for the starting and end points of the lines
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(lines_image, (x1, y1), (x2, y2), (255, 0, 0), thickness=3)

    # finally we have to merge the image with the lines
    image_with_lines = cv2.addWeighted(image, 0.8, lines_image, 1, 0.0)

    return image_with_lines


def region_of_interest(image, region_points):
    # we are going to replace pixels with 0 (black) - the regions we are not interested
    mask = np.zeros_like(image)
    # the region that we are interested in is the lower triangle - 255 white pixels
    cv2.fillPoly(mask, region_points, 255)
    # we have to use the mask: we want to keep the regions of the original image where
    # the mask has white colored pixels
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image


def get_detected_lanes(image):
    (height, width) = (image.shape[0], image.shape[1])

    # we have to turn the image into grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # edge detection kernel (Canny's algorithm)
    canny_image = cv2.Canny(gray_image, 100, 120)

    # we are interested in the "lower region" of the image (there are the driving lanes)
    region_of_interest_vertices = [
        (0, height),
        (width / 2, height * 0.65),
        (width, height)
    ]

    # we can get rid of the un-relevant part of the image
    # we just keep the lower triangle region
    cropped_image = region_of_interest(canny_image, np.array([region_of_interest_vertices], np.int32))

    # use the line detection algorithm (radians instead of degrees 1 degree = pi / 180)
    lines = cv2.HoughLinesP(cropped_image, rho=2, theta=np.pi / 180, threshold=50, lines=np.array([]),
                            minLineLength=40, maxLineGap=150)

    # draw the lines on the image
    image_with_lines = draw_the_lines(image, lines)

    return image_with_lines


# video = several frames (images shown after each other)
video = cv2.VideoCapture('lane_detection_video.mp4')

while video.isOpened():

    is_grabbed, frame = video.read()

    # because the end of the video
    if not is_grabbed:
        break

    frame = get_detected_lanes(frame)

    cv2.imshow('Lane Detection Video', frame)
    cv2.waitKey(50)

video.release()
cv2.destroyAllWindows()
