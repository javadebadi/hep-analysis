"""
Module to read countries data from web pages.
"""

import os
import ssl
import pandas as pd
from hep_analysis.settings import BASE_DIR
ssl._create_default_https_context = ssl._create_unverified_context

# website to get countries regions
REGION_URL = 'https://statisticstimes.com/geography/countries-by-continents.php'
# website to get countries codes
CODE_URL = 'https://countrycode.org'

# get all tables from htmls
region_tables = pd.read_html(REGION_URL)
code_tables = pd.read_html(CODE_URL)

# get dataframes for tables of interest from htmls
code_df = code_tables[0]
region_df = region_tables[2]

# the data in code_df which contains codes is in the ISO2/ ISO3 format
# thus wee need to split data and get ISO2 and ISO3 data in separate columns
code_df[['ISO2', 'ISO3']] = \
    code_df['ISO CODES'].str.split('/ ', expand=True)
# clean data (remove whitespaces from data in column ISO2)
code_df['ISO2'] = code_df['ISO2'].str.strip()

# rename region_df column in order to join two dataframes
region_df.rename(
    columns={
        'ISO-alpha3 Code': 'ISO3',
        'Country or Area': 'COUNTRY VARIATIONS',
        'Region 1': 'REGION_1',
        'Region 2': 'REGION_2',
        'Continent': 'CONTINENT'
        },
    inplace=True,
    )

# merge two dataframes
df = pd.merge(code_df, region_df, on=["ISO3"])

# select columns
df = df[
    [
        'COUNTRY',
        'COUNTRY VARIATIONS',
        'ISO2',
        'ISO3',
        'REGION_1',
        'REGION_2',
        'CONTINENT',
    ]
    ]


df.to_csv(os.path.join(BASE_DIR, 'country_table.csv'))
