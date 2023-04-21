import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load the dataset
dataset = pd.read_csv('both_urls_dataset.csv')
url_data = dataset[['url', 'status']]

# Create a bag-of-words matrix
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(url_data['url'])

# Create the target variable
y = url_data['status']

# Train the logistic regression model
lr_model = LogisticRegression(solver='lbfgs', max_iter=5000)
lr_model.fit(X, y)

# Make predictions on new URLs
new_urls = ['http://www.youtube.com', 'https://ipfs.io/ipfs/QmcW7EJ188qhHQEpdA9AwMK2tNTg2R7yTckjZtN4HzSBUp/xand1.html#redacted@abuse.ionos.com', 'facebook.com']
X_new = vectorizer.transform(new_urls)
y_pred = lr_model.predict(X_new)

# Print the predictions
print(y_pred)



from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y, y_pred)
print('Accuracy:', accuracy)
