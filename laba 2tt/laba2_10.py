import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Год': [2019, 2020, 2021, 2022, 2023],
    'ВВП': [109, 107, 131, 153, 171],
    'Инфляция': [3.0, 4.9, 8.4, 11.9, 7.4]
}
df = pd.DataFrame(data)

fig, ax1 = plt.subplots()

ax1.bar(df['Год'], df['ВВП'], color='skyblue', label='ВВП (трлн руб)')
ax1.set_xlabel('Год')
ax1.set_ylabel('ВВП (трлн руб)')

ax2 = ax1.twinx()
ax2.plot(df['Год'], df['Инфляция'], color='red', marker='o', linewidth=2, label='Инфляция (%)')
ax2.set_ylabel('Инфляция (%)')

plt.title('Динамика ВВП и инфляции (2019-2023)')
fig.tight_layout()
plt.show()