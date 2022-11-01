import cv2
import numpy as np

# we are not going to bother with objects less than 30% probability
THRESHOLD = 0.6
# the lower the value: the fewer bounding boxes will remain
SUPPRESSION_THRESHOLD = 0.2
SSD_IMAGE_SIZE = 320


# read the class label names
def construct_class_names(file_name):
    with open(file_name, 'rt') as file:
        names = file.read().rstrip('\n').split('\n')

    return names


def show_detected_objects(img, boxes_to_keep, all_bounding_boxes, object_names, class_ids):
    for index in boxes_to_keep:
        box = all_bounding_boxes[index[0]]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x + w, h + y), color=(255, 0, 0), thickness=1)
        cv2.putText(img, object_names[class_ids[index[0]][0] - 1].upper(), (box[0], box[1] - 10),
                    cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (255, 0, 0), 1)


class_names = construct_class_names('class_names')

capture = cv2.VideoCapture('objects.mp4')

neural_network = cv2.dnn_DetectionModel('ssd_weights.pb', 'ssd_mobilenet_coco_cfg.pbtxt')
# define whether we run the algorithm with CPU or with GPU
# WE ARE GOING TO USE CPU !!!
neural_network.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
neural_network.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)
neural_network.setInputSize(320, 320)
neural_network.setInputScale(1.0 / 127.5)
neural_network.setInputMean((127.5, 127.5, 127.5))
neural_network.setInputSwapRB(True)

while True:

    # after reading a frame (so basically one image) we just have to do
    # the same operations as with single images !!!
    frame_grabbed, frame = capture.read()

    if not frame_grabbed:
        break

    # detect the bounding boxes automatically
    class_label_ids, confidences, bbox = neural_network.detect(frame)
    # these are tuples - but NMS needs lists so we have to make transformations
    bbox = list(bbox)
    confidences = np.array(confidences).reshape(1, -1).tolist()[0]

    # these are the bounding box indexes to keep after NMS
    box_to_keep = cv2.dnn.NMSBoxes(bbox, confidences, THRESHOLD, SUPPRESSION_THRESHOLD)

    show_detected_objects(frame, box_to_keep, bbox, class_names, class_label_ids)

    cv2.imshow("SSD", frame)
    cv2.waitKey(1)

capture.release()
cv2.destroyAllWindows()
