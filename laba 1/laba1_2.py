import pandas as pd
import numpy as np

df = pd.read_excel('Число организаций, осуществляющих туристическую деятельность на конец периода_области.xls', skiprows=1)
    
df.columns = df.columns.str.strip()
col_territory = 'Территория Республики Беларусь'

years = [str(year) for year in range(2010, 2022)]
for year in years:
    df[year] = pd.to_numeric(df[year], errors='coerce').fillna(0)

df['Абсолютное_изменение'] = df['2021'] - df['2010']
df['Относительное_изменение_%'] = np.where(
    df['2010'] != 0,
    ((df['2021'] - df['2010']) / df['2010'] * 100).round(2),
    0
)

df['Спад_пандемия_2020_абс'] = df['2020'] - df['2019']

df.to_excel('Analiz_turizma_final.xlsx', index=False, sheet_name='Data')