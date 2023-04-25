import pandas as pd
from urllib.parse import urlparse

# Load the dataset into a pandas DataFrame
legitimate2 = pd.read_csv('dump-2020-12-15.csv')

# Extract the domain name from each URL
legitimate2['domain'] = legitimate2['url'].apply(lambda x: urlparse(x).netloc)

# Group the URLs by domain name and select one URL to keep
legitimate2 = legitimate2.groupby('domain').apply(lambda x: x.sort_values('date', ascending=False).iloc[0])

# Drop duplicates to keep only one URL per domain
legitimate2 = legitimate2.drop_duplicates(subset='domain', keep='first')

# Select only the url column and save the result
legit2 = legitimate2['url']
legit2.to_csv('legit2.csv', index=False)