import pandas as pd

statisticstimes_url = 'https://statisticstimes.com/geography/countries-by-continents.php'
countrycode_url = 'https://countrycode.org'

statisticstimes_tables = pd.read_html(statisticstimes_url)
countrycode_tables = pd.read_html(countrycode_url)

table1 = countrycode_tables[0]
table2 = statisticstimes_tables[2]
table1[['ISO2', 'ISO3']]=table1['ISO CODES'].str.split('/ ', expand=True)
table2 =table2.rename(columns={"ISO-alpha3 Code":"ISO3",'Country or Area':'COUNTRY'})


final_table = pd.merge(table1, table2, on=["ISO3"])

final_table.to_csv('country_table.csv')


