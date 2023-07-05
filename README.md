# Phishing URL Detection Machine Learning Model

## Table of Contents
  1. [Introduction](#introduction)<br>
  2. [Datasets](#datasets)<br>
  3. [Exploratory Data Analysis](#eda)<br>
  4. [Model Training](#model-training)<br>
  5. [Evaluation](#evaluation)<br>
  6. [Contributing](#contributing)<br>
  7. [License](#license)

## <a name="introduction"></a> Introduction
This repository contains a machine-learning model for detecting phishing URLs. The model uses [sklearn]'s Logistic Regression to classify URLs as either legitimate or phishing.

## <a name="datasets"> Datasets
For training and evaluating the phishing URL detection model, we utilized multiple datasets from various sources. The primary datasets were obtained from the University of New Brunswick (UNB) URL Datasets (https://www.unb.ca/cic/datasets/url-2016.html), while additional phishing URLs were obtained from Phishtank Developer Info (https://www.phishtank.com/developer_info.php).

The datasets from UNB included:
 -  Legitimate URLs: A collection of over 35,000 genuine and non-malicious URLs.
 -  Phishing URLs: An initial set of more than 9,000 fraudulent URLs.

To address the data imbalance, we augmented the dataset by incorporating additional datasets provided by UNB. These datasets included spam, malware, and defacement URLs, which increased the total count to over 24,500 URLs. Furthermore, we obtained an additional 11,000 phishing URLs from Phishtank, ensuring a more balanced representation of phishing data.

## <a name="eda"> Exploratory Data Analysis
We selected specific features to extract from the URLs for further analysis. The following features were chosen:
 -  Domain
 -  Have_IP
 -  Have_At
 -  URL_Length
 -  URL_Depth
 -  Redirection
 -  https_Domain

To gain insights from the extracted features, we conducted exploratory data analysis (EDA) and represented the findings using bar charts. The bar charts visually illustrate the distribution and characteristics of each feature (except the Domain feature), providing a comprehensive understanding of the data.

![EDA Image](imgs/eda-graphs.png)

Upon evaluation, the decision was made to incorporate only URL_Length and URL_Depth into the model. This decision was made based on the limited availability of data in the other features, where either the data did not sufficiently represent both labels or the features held limited significance in the context of the study. Therefore, URL_Length and URL_Depth were deemed the most relevant and informative features for the model.

## <a name="model-training"> Model Training
Writing...

## <a name="evaluation"> Evaluation
Writing...

## <a name="contributing"> Contributing
Writing...

## <a name="license"> License
Writing...

