import cv2
import os
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

#########################################

face_detector = cv2.CascadeClassifier(
    r"cascade.xml")

# face_detector = cv2.CascadeClassifier(
#     cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# For each person, enter one numeric face id
student_id = input('\n Enter your student ID: ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while(True):
    # print('here')
    _, img = cam.read()
    # img = cv2.flip(img, -1)  # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # for pre-trained haarcascade
    # faces = face_detector.detectMultiScale(gray, 1.3, 5)
    # for custom haarcascede
    faces = face_detector.detectMultiScale(gray, 1.1, 3)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(student_id) + '.' +
                    str(count) + ".jpg", gray[y:y+h, x:x+w])

    k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
    cv2.imshow('image', img)
    if k == 27:
        break
    elif count >= 30:  # Take 30 face sample and stop video
        break

cam.release()
cv2.destroyAllWindows()
