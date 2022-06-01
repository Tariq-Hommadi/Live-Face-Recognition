# Live-Face-Recognition

Live Face recognistion 

Since we are using a cascade classifier, we trained the classifier using a dataset that has positive and negative images. The positive images are face images, which is 35% of the dataset and the negative images are random images other than faces. The format of the images in the dataset is PGM, which is by default a grayscale image. 

 

Below are samples of the positive category: 

 

 

 

 

 

 

 

Below are samples of the negative category: 

 

 

 

 

 

 

Below is a chart diagram of the number of samples in both positive and negative categories: 

 

  

Below is a table shows the samples in both positive and negative categories 

 

Diagrams 

K-nearest neighbor 

As shown in figures 3 & 4, the flowchart diagram illustrates the use of the model and how the users will interact with it. In short, the model can be used to generate dataset for each person, and then a test image, which could be everyday attendance image, is fed and classified according to the nearest one based on distance measure L2 or cosine similarity after converting all images to 1-D array so that they become used in mathematical computation. 

Diagram

Description automatically generated 

Figure 3user enrollment flowchart 

Diagram

Description automatically generated 

Figure 4 flowchart of model usage 

Live Face recognition 

To illustrate how our approach works, we presented as a diagram as shown below. The first part concern about creation of the dataset (as it shown by Naif’s photos), the second part matches each category of images (Tariq images, Naif Images) with a unique id, lastly, we will recognize the faces and match is with its id. 

 

 

Experiment and results 
