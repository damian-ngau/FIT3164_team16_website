# Deep Learning Website

Developed a website that utilises a CNN model to detect microsatellite instability in histological images of Gastrointestinal Cancer Tumours.

Gastrointestinal Cancer Tumours are often referred to as having an "MSI status", meaning they will either be MSI or MSS - not both. 
Determining the MSI status is extremely important as it dictates the type of treatment needed for the tumour.

The website is aimed towards medical professionals who can utilise the platform to assist their work. They can create an account to manage patients with gastrointestinal cancer tumours. Histological images are uploaded and results from the deep learning algorithm are saved to patients.

- Developed the website using Flask framework and SQLAlchemy ORM.

- Deployed the website to Heroku using a PostgreSQL database.

- Formed the CNN architecture using Densenet from the Tensorflow Keras library to achieve an accuracy of 85.77% and F1-Score of 88.85%.

Dataset of histological images can be found on [kaggle](https://www.kaggle.com/datasets/joangibert/tcga_coad_msi_mss_jpg)

