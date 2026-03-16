import matplotlib.pyplot as plt

чеки = [4000, 5000, 4500, 4800, 5200, 100000, 1, 50000, 10]
частота = [4, 5, 4, 3, 5, 10, 20, 1, 50]
имена = ['Обычный 1', 'Обычный 2', 'Обычный 3', 'Обычный 4', 'Обычный 5', 'Олигарх', 'Тестер', 'Оптовик', 'Спамер']

plt.scatter(чеки, частота, color='blue')

for i, имя in enumerate(имена):
    plt.annotate(имя, (чеки[i], частота[i]), xytext=(5, 5), textcoords='offset points')

plt.title('Поиск аномалий среди покупателей')
plt.xlabel('Средний чек (руб)')
plt.ylabel('Частота покупок (раз в месяц)')
plt.xscale('log') 
plt.grid(True)
plt.show()