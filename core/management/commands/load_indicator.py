from datetime import datetime
from django.core.management.base import BaseCommand
from core.models import INDICATOR
from eurostatapiclient import EurostatAPIClient

VERSION = '1.0'
FORMAT = 'json'
LANGUAGE = 'en'
client = EurostatAPIClient(VERSION, FORMAT, LANGUAGE)


gdp_growth_dataset = client.get_dataset('tec00115').to_dataframe()
GDP_df = gdp_growth_dataset[["time","geo", "values"]]


class Command(BaseCommand):
    help = 'Load data from models file'

    def handle(self, *args, **kwargs):
        # Replace NaN values in 'values' column with 0
        GDP_df.loc[:, 'values'] = GDP_df.loc[:, 'values'].fillna(0)

        # Create or update rows in the model based on the DataFrame
        for index, row in GDP_df.iterrows():
            try:
                dt = datetime.strptime(row['time'], '%Y')
                year = dt.year  # Extract the year from the datetime object

                model_instance, created = INDICATOR.objects.update_or_create(
                    year=year,  # Use the year instead of the datetime object
                    country=row['geo'],
                    defaults={'value': row['values']}
                )
            except ValueError:
                # Handle invalid datetime strings
                print(f"Invalid datetime format in row {index}: {row['time']}")