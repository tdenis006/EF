import matplotlib.pyplot as plt

инфляция_регионы = [5.2, 6.0, 6.5, 7.1, 7.3, 7.5, 7.8, 8.2, 9.0, 12.5]

plt.boxplot(инфляция_регионы)
plt.title('Разброс инфляции по регионам')
plt.ylabel('Уровень инфляции (%)')
plt.show()