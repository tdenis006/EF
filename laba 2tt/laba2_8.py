import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

страны = ['Норвегия', 'Швейцария', 'Люксембург', 'США', 'Германия', 'Россия', 'Китай', 'Индия']
ввп = [90, 95, 130, 80, 55, 15, 12, 2.5]
инфляция = [2.5, 2.0, 2.2, 3.2, 2.5, 7.4, 1.5, 5.5]

X = np.array(list(zip(ввп, инфляция)))

kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

plt.scatter(ввп, инфляция, c=clusters, cmap='viridis', s=100)

for i, страна in enumerate(страны):
    plt.annotate(страна, (ввп[i], инфляция[i]), xytext=(5, 5), textcoords='offset points')

plt.title('Кластеризация стран по ВВП и инфляции')
plt.xlabel('ВВП на душу (тыс. $)')
plt.ylabel('Инфляция (%)')
plt.grid(True)
plt.show()