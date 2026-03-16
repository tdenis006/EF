import matplotlib.pyplot as plt

страны = ['Россия', 'США', 'Германия', 'Турция', 'Аргентина', 'Япония', 'Китай']
инфляция = [7.4, 3.2, 2.5, 64, 120, 2.0, 1.5]
цвета = ['tab:blue', 'tab:blue', 'tab:blue', 'tab:red', 'tab:red', 'tab:blue', 'tab:blue']

plt.bar(страны, инфляция, color=цвета)
plt.title('Уровень инфляции в странах')
plt.xlabel('Страна')
plt.ylabel('Инфляция (%)')
plt.show()