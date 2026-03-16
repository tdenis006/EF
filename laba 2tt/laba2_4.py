import matplotlib.pyplot as plt

категории = ['Социалка', 'Оборона', 'Экономика', 'ЖКХ', 'Другое']
доли = [35, 20, 15, 10, 20]
взрыв = [0.1, 0, 0, 0, 0]

plt.pie(доли, labels=категории, autopct='%1.1f%%', explode=взрыв, shadow=True)
plt.title('Структура расходов бюджета')
plt.show()