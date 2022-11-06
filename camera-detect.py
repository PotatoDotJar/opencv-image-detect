
import tensorflow_hub as hub
import tensorflow as tf
import cv2

# Use openimages_v4/ssd/mobilenet_v2 model
detector = hub.load("https://tfhub.dev/google/openimages_v4/ssd/mobilenet_v2/1").signatures['default']
  
vid = cv2.VideoCapture(0)

window = 'window'

width = 512
height = 512
thresh = 40

def onThreshChange(value):
    global thresh
    thresh = value

cv2.namedWindow(window)
cv2.createTrackbar('score threshold', window, thresh, 100, onThreshChange)

while(True):
    ret, frame = vid.read()

    inp = cv2.resize(frame, (width, height))
    rgb = cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)

    rgb_tensor = tf.image.convert_image_dtype(rgb, tf.float32)[tf.newaxis, ...]

    result = detector(rgb_tensor)
    result = {key:value.numpy() for key,value in result.items()}
    boxes = result["detection_boxes"]
    class_entities = result["detection_class_entities"]
    class_labels = result["detection_boxes"]
    class_names = result["detection_boxes"]
    scores = result["detection_scores"]
   
    # loop throughout the detections and place a box around it
    for i in range(boxes.shape[0]):
        if(scores[i] * 100 < thresh):
            continue

        im_width, im_height = rgb.shape[0:2]

        ymin, xmin, ymax, xmax = tuple(boxes[i])

        (left, right, top, bottom) = (int(xmin * im_width), int(xmax * im_width), int(ymin * im_height), int(ymax * im_height))

        img_boxes = cv2.rectangle(rgb, (left, top), (right, bottom), (0, 255, 0), 1)
        font = cv2.FONT_HERSHEY_SIMPLEX

        display_str = "{}: {}%".format(class_entities[i].decode("ascii"), int(100 * scores[i]))
        cv2.putText(img_boxes, display_str, (left, bottom - 10), font, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

    cv2.imshow(window, rgb)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()