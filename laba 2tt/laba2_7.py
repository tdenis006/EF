import matplotlib.pyplot as plt

дни = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт']
курс = [90, 91, 89, 92, 93]
объем = [100, 120, 80, 150, 170]

fig, ax1 = plt.subplots()

ax1.plot(дни, курс, color='red', marker='o', label='Курс $')
ax1.set_ylabel('Цена доллара (руб)')

ax2 = ax1.twinx()
ax2.bar(дни, объем, alpha=0.3, color='gray', label='Объем торгов')
ax2.set_ylabel('Объем торгов (млн $)')

plt.title('Динамика валютного рынка')
plt.show()