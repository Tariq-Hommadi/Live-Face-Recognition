# Live-Face_Recognition


- Face Detection:
In this step we trained a cascade classifier using a dataset that has positive data, face images, and negative data, random images other than faces. The classifier will detect the faces in the webcam.

- Face Recognition:
This step has three sub-steps under it.

•	Dataset Creation:
In this step we will create a dataset by taking 30 pictures of a person and save it in a folder. Each person will be labeled with an ID. Before saving the images, we perform three preprocessing tasks:
i. Converting the image into grayscale.
ii. Detect the faces in the image using the model we trained in the face detection step.

•	Train LBPH algorithm using the data we collected in the previous step. LBPH is a model used for face recognition.


•	Recognize the Face:
In this we will detect the faces in the image using the model we trained in the previous step. Three preprocessing tasks will be performed in the image:
i. Converting the image into grayscale.
ii. Detect the faces in the image using the model we trained in the face detection step
iii. Recognize the faces in the image and label each face with the names of each person
