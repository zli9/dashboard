'''
Preprocessing the dataset.
'''
import os
from pathlib import Path
import pandas as pd

data_path = Path(__file__).parent.parent / 'data/countries-table.csv'

data = pd.read_csv(data_path)\
    .assign(density=lambda df: round(df['density'], 2),
            worldPercentage=lambda df: round(df['worldPercentage']*100, 2),
            )\
    .sort_values(by='rank')\
    .rename(columns={'pop1980': 1980, 'pop2000': 2000, 'pop2010': 2010, 'pop2022': 2022,
                     'pop2023': 2023, 'pop2030': 2030, 'pop2050': 2050, 'cca3': 'abbr', 'landAreaKm': 'landArea'})

countries = data['country'].sort_values().unique()
years = data.columns[-7:]
