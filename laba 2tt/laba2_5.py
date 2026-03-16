import matplotlib.pyplot as plt

зарплаты = [40, 45, 50, 52, 55, 60, 62, 65, 70, 75, 80, 85, 90, 100, 120, 150, 200]

plt.hist(зарплаты, bins=6, color='skyblue', edgecolor='black')
plt.title('Распределение зарплат в отрасли')
plt.xlabel('Зарплата (тыс. руб.)')
plt.ylabel('Количество сотрудников')
plt.show()