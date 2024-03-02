import pandas as pd
from eurostatapiclient import EurostatAPIClient

VERSION = '1.0'
FORMAT = 'json'
LANGUAGE = 'en'
client = EurostatAPIClient(VERSION, FORMAT, LANGUAGE)


gdp_growth_dataset = client.get_dataset('tec00115').to_dataframe()
GDP_df = gdp_growth_dataset.query("unit == 'CLV_PCH_PRE'")[["time", "geo", "values"]]

with pd.option_context ("display.max_rows", None):
   print(GDP_df)

# print(GDP_df)

