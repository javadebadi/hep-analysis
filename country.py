import os
import logging
logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S',
    level=logging.DEBUG,
)
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','hep_analysis.settings')
django.setup()

import pandas as pd
df = pd.read_csv("country_table.csv")
df_dict = df.to_dict(orient='records')
print(df_dict)

from inspirehep.models import Country
for country_dict in df_dict:
    try:
        name = country_dict.get("COUNTRY")
        iso2 = country_dict.get("ISO2")
        iso3 = country_dict.get("ISO3")
        Country.objects.get_or_create(
            name=name,
            iso2=iso2,
            iso3=iso3,
        )
    except Exception as e:
        logging.error(str(e))
        logging.info("country_dict = ")
        logging.info(country_dict)
