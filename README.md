# Phishing URL Detection Machine Learning Model

## Table of Contents
  1. [Introduction](#introduction)<br>
  2. [Datasets](#datasets)<br>
  3. [Model Training](#model-training)<br>
  4. [Evaluation](#evaluation)<br>
  5. [Contributing](#contributing)<br>
  6. [License](#license)

## <a name="introduction"></a> Introduction
This repository contains a machine-learning model for detecting phishing URLs. The model uses [sklearn]'s Logistic Regression to classify URLs as either legitimate or phishing.

## <a name="datasets"> Datasets
For training and evaluating the phishing URL detection model, we utilized multiple datasets from various sources. The primary datasets were obtained from the University of New Brunswick (UNB) URL Datasets (https://www.unb.ca/cic/datasets/url-2016.html), while additional phishing URLs were obtained from Phishtank Developer Info (https://www.phishtank.com/developer_info.php).

The datasets from UNB included:
 - Legitimate URLs: A collection of over 35,000 genuine and non-malicious URLs.
 - Phishing URLs: An initial set of more than 9,000 fraudulent URLs.

To address the data imbalance, we augmented the dataset by incorporating additional datasets provided by UNB. These datasets included spam, malware, and defacement URLs, which increased the total count to over 24,500 URLs. Furthermore, we obtained an additional 11,000 phishing URLs from Phishtank, ensuring a more balanced representation of phishing data.

## <a name="model-training"> Model Training
Writing...

## <a name="evaluation"> Evaluation
Writing...

## <a name="contributing"> Contributing
Writing...

## <a name="license"> License
Writing...

