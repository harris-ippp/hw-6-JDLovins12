import requests
from bs4 import BeautifulSoup
import pandas as pd
%matplotlib inline

# Q2
base = 'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'
for year in election_dic.keys():
    url = base.format(election_dic[year])
    with open( 'president_general_' + year + '.csv', 'w') as output:
        output.write(requests.get(url).text)
    
