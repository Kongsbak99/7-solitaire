import cv2


def write_on_image(frame, cam_num, text):
    # text
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    color = (0, 0, 0)
    thickness = 1

    if cam_num == 0: org = (20, 310)
    elif cam_num == 1: org = (200, 310)
    elif cam_num == 2: org = (375, 310)
    elif cam_num == 3: org = (560, 310)
    elif cam_num == 4: org = (745, 310)
    elif cam_num == 5: org = (930, 310)
    elif cam_num == 6: org = (1100, 310)

    elif cam_num == 7: org = (10, 20)
    elif cam_num == 8: org = (260, 20)
    elif cam_num == 9: org = (525, 20)
    elif cam_num == 10: org = (775, 20)
    elif cam_num == 11: org = (1040, 20)
    else: org = (10, 20)

    frame = cv2.putText(frame, str(cam_num), org, font,
                        fontScale, color, thickness, cv2.LINE_AA)
    return frame
