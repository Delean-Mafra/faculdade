from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score




y_true = [0, 1, 1, 0, 1]
y_prev = [0, 1, 0, 0, 1]

acc = accuracy_score(y_true, y_prev)
print(acc)

confm = confusion_matrix(y_true, y_prev)
print(confm)

pres = precision_score(y_true, y_prev)
print(pres)

recall = recall_score(y_true, y_prev)
print(recall)

f1 = f1_score(y_true, y_prev)
print(f1)   


import matplotlib.pyplot as plt

labels = ['Modelo 1', 'Modelo 2', 'Modelo 3']
accuracies = [0.85, 0.92, 0.78]
precisions = [0.88, 0.85, 0.92]
recalls = [0.90, 0.78, 0.85]

plt.figure(figsize=(12, 6))

plt.bar(labels, accuracies, label='Acurácia')
plt.bar(labels, precisions, label='Precisão')
plt.bar(labels, recall, label='recalls')

plt.xlabel('Modelos')
plt.ylabel('Métricas')
plt.title('qwety')
plt.legend()
plt.show()



y_true = [1,4,3,5,7]
y_prev = [1.8,4.2,2.9,4.8,6.5]

plt.scatter(y_true, y_prev)
plt.plot([min(y_true), max(y_true)], [min(y_true), max(y_true)], 'k--', lw=2)
plt.show()




