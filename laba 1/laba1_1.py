import pandas as pd
import numpy as np
    
df = pd.read_excel('laba1_1.xls')


df.columns = df.columns.str.strip()
col_territory = df.columns[0]
col_activity = df.columns[1]
df[col_territory] = df[col_territory].ffill()

years = ['2017', '2018', '2019', '2020', '2021']
for year in years:
    df[year] = pd.to_numeric(df[year], errors='coerce').fillna(0)

# Расчет динамики
df['Абсолютное_изм'] = df['2021'] - df['2017']
df['Относительное_изм_%'] = np.where(
    df['2017'] != 0,
    ((df['2021'] - df['2017']) / df['2017'] * 100).round(2),
    0
)

with pd.ExcelWriter('analysis_result.xlsx', engine='openpyxl') as writer:

    df.to_excel(writer, sheet_name='Общий_анализ', index=False)
    
    regions = df[col_territory].unique()
    for region in regions:
        region_data = df[df[col_territory] == region]
        sheet_name = str(region)[:30].replace(' ', '_').replace('.', '')
        region_data.to_excel(writer, sheet_name=sheet_name, index=False)

print("Анализ завершен. Данные сохранены в файл analysis_result.xlsx")