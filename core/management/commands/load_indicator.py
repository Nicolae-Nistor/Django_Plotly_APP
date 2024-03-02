from datetime import datetime
from django.core.management.base import BaseCommand
from core.models import INDICATOR
from data.Eurostat_Data import GDP_df

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
                    year=year,
                    country=row['geo'],
                    defaults={'value': row['values']}
                )
            except ValueError:
                # Handle invalid datetime strings
                print(f"Invalid datetime format in row {index}: {row['time']}")