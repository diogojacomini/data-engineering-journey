from etl.structure import ETL
import requests
import json
import pandas as pd


class ETLCoinmarket(ETL):

    def extract(self):
        '''Extraction of the data from API requests.'''
        response = requests.get(**self.input)
        self.data_rw = json.loads(response.text)

    def transform(self):
        '''From the raw data (json) transform it into a dataframe.'''
        datasets = []
        for coin in self.data_rw['data']:
            df_line = pd.DataFrame([coin])

            # Append line of data raw to datasets with json treated.
            datasets.append(pd.concat(
                [df_line.drop('quote', axis=1),
                 df_line.quote.apply(pd.Series).BRL.apply(pd.Series).drop('last_updated', axis=1)],
                axis=1,
            ))

        # Merge datasets.
        self.dataframe = pd.concat(datasets)

        # Drop columns.
        self.dataframe.drop('platform', axis=1, inplace=True)

        # String to datetime format.
        self.dataframe['date_added'] = pd.to_datetime(self.dataframe['date_added'], format='%Y-%m-%dT%H:%M:%S.%f%z')
        self.dataframe['last_updated'] = pd.to_datetime(self.dataframe['last_updated'], format='%Y-%m-%dT%H:%M:%S.%f%z')

    def load(self):
        '''Load data on database.'''
        try:
            self.dataframe.to_sql(**self.output, index=False, if_exists='append')
        except Exception as err:
            print(f"\nFail to load data on database: {err}")
