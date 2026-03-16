import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import numpy as np

data = {
    'Страна': ['Норвегия', 'Швейцария', 'Люксембург', 'США', 'Германия', 'Россия', 'Китай', 'Индия'],
    'ВВП': [90, 95, 130, 80, 55, 15, 12, 2.5],
    'Инфляция': [2.5, 2.0, 2.2, 3.2, 2.5, 7.4, 1.5, 5.5]
}
df = pd.DataFrame(data)

X = df[['ВВП', 'Инфляция']]
kmeans = KMeans(n_clusters=3, random_state=42)
df['Кластер'] = kmeans.fit_predict(X)

plt.figure(figsize=(10, 6))
scatter = plt.scatter(df['ВВП'], df['Инфляция'], c=df['Кластер'], cmap='viridis', s=100)

for i, txt in enumerate(df['Страна']):
    plt.annotate(txt, (df['ВВП'][i], df['Инфляция'][i]), xytext=(5, 5), textcoords='offset points')

plt.title('Финальное задание: Кластеризация стран')
plt.xlabel('ВВП на душу (тыс. $)')
plt.ylabel('Инфляция (%)')
plt.grid(True)
plt.show()