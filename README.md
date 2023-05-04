# Deep Learning Website

Developed a website that utilises a CNN model to detect microsatellite instability in histological images of Gastrointestinal Cancer Tumours.

Gastrointestinal Cancer Tumours are often referred to as having an "MSI status", meaning they will either be MSI or MSS - not both. 
Determining the MSI status is extremely important as it dictates the type of treatment needed for the tumour.

The website is aimed towards medical professionals who can utilise the platform to assist their work. They can create an account to manage patients with gastrointestinal cancer tumours. They can upload Histological images and results from the deep learning algorithm are saved to patients.

- Formed the CNN architecture using Densenet from the Tensorflow Keras library to achieve an accuracy of 85.77% and F1-Score of 88.85%.

- Developed the website using Flask framework and SQLAlchemy ORM.

- Deployed the website to Heroku using a PostgreSQL database.

Dataset of histological images can be found on [kaggle](https://www.kaggle.com/datasets/joangibert/tcga_coad_msi_mss_jpg)

<br>

## Screenshots
### Log In Page
<img width="1920" alt="loginPage" src="https://user-images.githubusercontent.com/49575407/236291419-ddf59653-e42f-4880-b8bd-6a0bd37646a6.png">

<br>

### Home Page
<img width="1920" alt="homePage" src="https://user-images.githubusercontent.com/49575407/236292073-a3a62b21-3d1b-4d7c-a7db-627c5127ee68.png">

<br>

### Patient Page
<img width="1920" alt="patientPage" src="https://user-images.githubusercontent.com/49575407/236291736-b5325e1d-75a9-40f9-a966-598f3b793631.png">

<br>

### Results Page
<img width="1920" alt="resultPage" src="https://user-images.githubusercontent.com/49575407/236291786-9176bdeb-0866-4d39-bdf3-ed8b0e239b5c.png">

<br>

## Demo 
### Signing Up
https://user-images.githubusercontent.com/49575407/236292751-34c10fa7-6505-4d5a-88bd-d2855be39044.mp4

<br>

### Logging In
https://user-images.githubusercontent.com/49575407/236292905-22cab6ca-bbd0-4238-a097-cfdf8973f61f.mp4

<br>

### Creating Patient 
https://user-images.githubusercontent.com/49575407/236293092-acc02514-9762-4082-aaa9-12807b3ff58f.mp4

<br>

### Uploading and Saving Result
https://user-images.githubusercontent.com/49575407/236293285-e9d58f58-a8de-4fc1-a8e4-d3af55f0a1ee.mp4

