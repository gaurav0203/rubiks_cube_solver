import cv2
import numpy as np

window_height = 480
window_width = 640

ROI = {"roi1":[window_height // 4 - 10,window_height // 4 + 10,window_width // 4 - 10,window_width // 4 + 10],
       "roi2":[window_height // 4 - 10,window_height // 4 + 10,window_width // 2 - 10,window_width // 2 + 10],
       "roi3":[window_height // 4 - 10,window_height // 4 + 10,3*window_width // 4 - 10,3*window_width // 4 + 10],
       "roi4":[window_height // 2 - 10,window_height // 2 + 10,window_width // 4 - 10,window_width // 4 + 10],
       "roi5":[window_height // 2 - 10,window_height // 2 + 10, window_width // 2 - 10,window_width // 2 + 10 ],
       "roi6":[window_height // 2 - 10,window_height // 2 + 10,3*window_width // 4 - 10,3*window_width // 4 + 10],
       "roi7":[3 * window_height // 4 - 10,3 * window_height // 4 + 10,window_width // 4 - 10,window_width // 4 + 10],
       "roi8":[3 * window_height // 4 - 10,3 * window_height // 4 + 10,window_width // 2 - 10,window_width // 2 + 10],
       "roi9":[3 * window_height // 4 - 10,3 * window_height // 4 + 10,3*window_width // 4 - 10,3*window_width // 4 + 10]
    }

def main():
    cap = cv2.VideoCapture(2)

    if not cap.isOpened():
        print("Cant open camera")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("No frames received")
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        draw_roi_selector(frame,window_height,window_width)
        face_colors = get_colors(hsv_frame)
        display_color_name(frame, face_colors)
        cv2.imshow('Cube Face Detector', frame)



        k = cv2.waitKey(1)
        if k == ord('q'):
            print("quit")
            break
        
        if k == ord('c'):
            print("C pressed")
            with open('colors.txt', 'a') as f:
                f.write(','.join(face_colors))
                f.write('\n')

        if k == ord('n'):
            print("N pressed")
            with open('colors.txt', 'w') as f:
                f.write('')


    cap.release()
    cv2.destroyAllWindows()


def display_color_name(frame, face_colors):
    for index, roi in enumerate(ROI):
        cv2.putText(frame, face_colors[index],(ROI[roi][3] + 5,ROI[roi][1]),
                    cv2.FONT_HERSHEY_PLAIN,1.0,(255,255,255),1)


def get_colors(hsv_frame):
    color_list = []
    for roi in ROI:
        area = hsv_frame[ROI[roi][0]:ROI[roi][1], ROI[roi][2]:ROI[roi][3]]
        # print(ROI[roi][0],ROI[roi][1], ROI[roi][2],ROI[roi][3])
        if white_detected(area):
            color_list.append("White")
        elif red_detected(area):
            color_list.append("Red")
        elif green_detected(area):
            color_list.append("Green")
        elif orange_detected(area):
            color_list.append("Orange")
        elif blue_detected(area):
            color_list.append("Blue")
        elif yellow_detected(area):
            color_list.append("Yellow")
        else:
            color_list.append(None)

    return color_list


def blue_detected(roi):
    lower_blue_range = np.array([84, 83, 34])
    upper_blue_range = np.array([140, 255, 255])
    mask = cv2.inRange(roi, lower_blue_range, upper_blue_range)
    threshold = 350

    is_color_within_range = np.count_nonzero(mask) > threshold
    if is_color_within_range:
        return True
    else:
        return False


def yellow_detected(roi):
    lower_blue_range = np.array([13, 155, 128])
    upper_blue_range = np.array([30, 255, 218])
    mask = cv2.inRange(roi, lower_blue_range, upper_blue_range)
    threshold = 350

    is_color_within_range = np.count_nonzero(mask) > threshold
    if is_color_within_range:
        return True
    else:
        return False


def green_detected(roi):
    lower_blue_range = np.array([28, 215, 71])
    upper_blue_range = np.array([85, 255, 157])
    mask = cv2.inRange(roi, lower_blue_range, upper_blue_range)
    threshold = 350

    is_color_within_range = np.count_nonzero(mask) > threshold
    if is_color_within_range:
        return True
    else:
        return False


def red_detected(roi):
    lower_blue_range = np.array([125, 181, 55])
    upper_blue_range = np.array([179, 255, 255])
    mask = cv2.inRange(roi, lower_blue_range, upper_blue_range)

    threshold = 350

    is_color_within_range = np.count_nonzero(mask) > threshold
    # cv2.imshow("RedMask", mask)

    if is_color_within_range:
        return True
    else:
        return False


def orange_detected(roi):
    lower_blue_range = np.array([0, 155, 125])
    upper_blue_range = np.array([12, 255, 255])
    mask = cv2.inRange(roi, lower_blue_range, upper_blue_range)
    threshold = 350

    is_color_within_range = np.count_nonzero(mask) > threshold
    if is_color_within_range:
        return True
    else:
        return False


def white_detected(roi):
    lower_blue_range = np.array([56, 0, 47])
    upper_blue_range = np.array([179, 98, 185])
    mask = cv2.inRange(roi, lower_blue_range, upper_blue_range)
    threshold = 320
    # cv2.imshow("White Mask", mask)
    is_color_within_range = np.count_nonzero(mask) > threshold
    if is_color_within_range:
        return True
    else:
        return False


def draw_roi_selector(frame,window_height, window_width):
    # center_center
    frame = cv2.rectangle(frame, (window_width // 2 - 10, window_height // 2 - 10),
                          (window_width // 2 + 10, window_height // 2 + 10), (255, 255, 255), 2)
    # top left
    frame = cv2.rectangle(frame, (window_width // 4 - 10, window_height // 4 - 10),
                          (window_width // 4 + 10, window_height // 4 + 10), (255, 255, 255), 2)
    # top center
    frame = cv2.rectangle(frame, (window_width // 2 - 10, window_height // 4 - 10),
                          (window_width // 2 + 10, window_height // 4 + 10), (255, 255, 255), 2)
    # top right
    frame = cv2.rectangle(frame, (3 * window_width // (4) - 10, window_height // 4 - 10),
                          (3 * window_width // (4) + 10, window_height // 4 + 10), (255, 255, 255), 2)
    # center left
    frame = cv2.rectangle(frame, (window_width // 4 - 10, window_height // 2 - 10),
                          (window_width // 4 + 10, window_height // 2 + 10), (255, 255, 255), 2)
    # center right
    frame = cv2.rectangle(frame, (3 * window_width // 4 - 10, window_height // 2 - 10),
                          (3 * window_width // 4 + 10, window_height // 2 + 10), (255, 255, 255), 2)
    # bottom left
    frame = cv2.rectangle(frame, (window_width // 4 - 10, 3 * window_height // 4 - 10),
                          (window_width // 4 + 10, 3 * window_height // 4 + 10), (255, 255, 255), 2)
    # bottom center
    frame = cv2.rectangle(frame, (window_width // 2 - 10, 3 * window_height // 4 - 10),
                          (window_width // 2 + 10, 3 * window_height // 4 + 10), (255, 255, 255), 2)
    # bottom right
    frame = cv2.rectangle(frame, (3 * window_width // 4 - 10, 3 * window_height // 4 - 10),
                          (3 * window_width // 4 + 10, 3 * window_height // 4 + 10), (255, 255, 255), 2)


if __name__ == "__main__":
    main()
