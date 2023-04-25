import pandas as pd
from  urllib.parse import urlparse
import numpy as np

dump = pd.read_csv('dump-2020-12-15.csv')
urls = dump['url']
urls = np.array(urls)

domains = {}
for url in urls:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain not in domains:
        domains[domain] = url

urls = np.array(domains.values())


df = pd.DataFrame(urls, columns=['url'])
df.to_csv('legitimate_urls_2', index=False)



