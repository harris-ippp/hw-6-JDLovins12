import requests
from bs4 import BeautifulSoup
import pandas as pd
%matplotlib inline

df_dic = {}
for year in election_dic.keys():
    header = pd.read_csv("president_general_" + year +  ".csv", nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv("president_general_" + year +  ".csv", skiprows = [1], index_col = 0, thousands = ",")
    df.rename(inplace = True, columns = d) # rename to democrat/republican
    df.dropna(inplace = True, axis = 1)    # drop empty columns
    df = df[['Republican', 'Democratic', 'Total Votes Cast']]
    df["Year"] = int(year)
    df_dic[year] = df

df_meta = pd.concat([df_dic[year] for year in election_dic.keys()])
df_meta['R share'] = df_meta['Republican']/ df_meta['Total Votes Cast']

counties = ['Accomack County', 'Albemarle County', 'Alexandria City', 'Alleghany County']
df_counties = df_meta.loc[ df_meta.index.isin(counties) , ['Year', 'R share']]

for county in counties:
    ax = df_meta.loc[ df_meta.index == county, ['Year', 'R share']].set_index('Year').iloc[::-1].plot()
    ax.set_title(county)
    ax.figure.savefig(county + '.pdf')
