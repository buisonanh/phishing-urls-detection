# Phishing URL Detection Machine Learning Model

## Table of Contents
  1. [Introduction](#introduction)<br>
  2. [Usage](#usage)<br>
  3. [Datasets](#datasets)<br>
  4. [Model Training](#model-training)<br>
  5. [Evaluation](#evaluation)<br>
  6. [Contributing](#contributing)<br>
  7. [License](#license)

## <a name="introduction"></a> Introduction
This repository contains a machine-learning model for detecting phishing URLs. The model uses [sklearn] to classify URLs as either legitimate or phishing.

## <a name="usage"></a> Usage
Writing...

```python3
import phishing_url_detector

model = phishing_url_detector.PhishingURLDetector()
result = model.detect_url('http://example.com')

print(result)
```

## <a name="datasets"> Datasets
This project requires a large number of authentic (0) and phishing (1) URLs.

The open-source tool PhishTank makes it relatively simple to collect phishing URLs. This site offers a collection of phishing URLs that are updated hourly in a variety of formats, including CSV, JSON, etc. Visit https://www.phishtank.com/developer_info.php to download the information.

n order to find the legitimate URLs, I discovered a source that has a collection of benign, spam, phishing, malware, and defacement URLs. University of New Brunswick, https://www.unb.ca/cic/datasets/url-2016.html, is the dataset's original publisher. 35,300 valid URLs are included in this collection. The URL collection is downloaded, and the file of importance is "Benign_list_big_final.csv" from that.

## <a name="model-training"> Model Training
Writing...

## <a name="evaluation"> Evaluation
Writing...

## <a name="contributing"> Contributing
Writing...

## <a name="license"> License
Writing...

