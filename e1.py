import requests
from bs4 import BeautifulSoup
import pandas as pd
%matplotlib inline

# Q1
url_va = 'http://historical.elections.virginia.gov/elections/search/year_from:1924/year_to:2016/office_id:1/stage:General'
req_va = requests.get(url_va)
html_va = req_va.content
soup = BeautifulSoup(html_va, 'html.parser')
tags = soup.find_all('tr','election_item')

ELECTION_ID = []
election_dic = {}
for t in tags:
    year = t.td.text
    year_id = t['id'][-5:]
    ELECTION_ID.append(year + ' ' + year_id)
    election_dic[year] = year_id
print(ELECTION_ID)
