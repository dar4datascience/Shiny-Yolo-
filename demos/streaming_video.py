import cv2

cam_feed = cv2.VideoCapture(0)

cam_feed.set(cv2.CAP_PROP_FRAME_WIDTH, 650)
cam_feed.set(cv2.CAP_PROP_FRAME_HEIGHT, 750)
# annotated_image, preds = obj_detect.detectObjectsFromImage(input_image=img,
#                 input_type="array",
#                   output_type="array",
#                   display_percentage_probability=False,
#                   display_object_name=True)

while True:    
    ret, img = cam_feed.read()   

    cv2.imshow("Camera Feed", img)     

    key = cv2.waitKey(1)
    if (key & 0xFF == ord("q")) or (key == 27):
        break

cam_feed.release()
cv2.destroyAllWindows()