import pandas as pd

data = {
    'Показатели': [
        'Долгосрочные активы (ДА)', 
        'Краткосрочные активы (КА)', 
        'Собственный капитал (СК)', 
        'Долгосрочные обязательства (ДО)', 
        'Краткосрочные обязательства (КО)',
        'Баланс'
    ],
    'На начало года': [69340, 28759, 79094, 19005, 18679, 98099],
    'На конец года': [70488, 30897, 79274, 22111, 21672, 101385]
}

df = pd.DataFrame(data)

def get_val(df, row_name, col_name):
    return df.loc[df['Показатели'] == row_name, col_name].values[0]

results = []
for col in ['На начало года', 'На конец года']:
    da = get_val(df, 'Долгосрочные активы (ДА)', col)
    ka = get_val(df, 'Краткосрочные активы (КА)', col)
    sk = get_val(df, 'Собственный капитал (СК)', col)
    do = get_val(df, 'Долгосрочные обязательства (ДО)', col)
    ko = get_val(df, 'Краткосрочные обязательства (КО)', col)
    ib = get_val(df, 'Баланс', col)
    
    k1 = ka / ko
    k2 = (sk + do - da) / ka
    k3 = (ko + do) / ib
    
    results.append([k1, k2, k3])

res_df = pd.DataFrame({
    'Коэффициент': ['К1 (Текущая ликвидность)', 'К2 (Обеспеченность СОС)', 'К3 (Обеспеченность активами)'],
    'На начало года': [results[0][0], results[0][1], results[0][2]],
    'На конец года': [results[1][0], results[1][1], results[1][2]],
    'Норматив': ['>= 1.5', '>= 0.1', '<= 0.85']
})

with pd.ExcelWriter('Express_Control_Financial.xlsx') as writer:
    df.to_excel(writer, sheet_name='Исходные_данные', index=False)
    res_df.to_excel(writer, sheet_name='Расчет_коэффициентов', index=False)