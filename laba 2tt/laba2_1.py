import matplotlib.pyplot as plt 

месяцы = ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек']
ставка = [7.5, 7.5, 8.0, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5, 12.0]

plt.plot(месяцы, ставка, marker='o', color='tab:red', linestyle='-')

plt.title('Ключевая ставка ЦБ в 2024 году') 
plt.xlabel('Месяц') 
plt.ylabel('Ставка (%)')

plt.grid(True)

plt.show()