import matplotlib.pyplot as plt

страны = ['США', 'Германия', 'Россия', 'Китай', 'Бразилия', 'Индия', 'Япония', 'Турция']
ввп = [80, 55, 15, 12, 10, 2.5, 40, 13]
безработица = [3.5, 3.0, 3.2, 5.0, 8.0, 7.5, 2.6, 10.5]

plt.scatter(ввп, безработица, color='green')

for i, страна in enumerate(страны):
    plt.annotate(страна, (ввп[i], безработица[i]), xytext=(5, 5), textcoords='offset points')

plt.title('Связь ВВП на душу населения и безработицы')
plt.xlabel('ВВП на душу населения (тыс. $)')
plt.ylabel('Безработица (%)')
plt.grid(True)
plt.show()