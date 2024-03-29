import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import pickle
from sklearn import linear_model
from sklearn.utils import shuffle

data = pd.read_csv('data/student-mat.csv', sep=';')
data = data[['G1', 'G2', 'G3', 'studytime', 'failures', 'absences']]

predict = 'G3'

x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

# best = 0
# for _ in range(30):
#     x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size=0.1)

#     linear = linear_model.LinearRegression()
#     linear.fit(x_train, y_train)

#     acc = linear.score(x_test, y_test)
#     print(acc)

#     if acc > best:
#         best = acc
#         with open('data/student_model.pickle', 'wb') as f:
#             pickle.dump(linear, f)

pickle_in = open('data/student_model.pickle', 'rb')
linear = pickle.load(pickle_in)

print(f'Coefficient: {linear.coef_}')
print(f'Intercept: {linear.intercept_}')

predictions = linear.predict(x_test)
# for x in range(len(predictions)):
#     print(predictions[x], x_test[x], y_test[x])

p = 'absences'
fig, ax = plt.subplots()

ax.scatter(data[p][:40], data['G2'][:40], label='2nd grade')
ax.scatter(data[p][:40], predictions, label='3rd grade (predicted)')

ax.set_xlabel(p)
ax.set_ylabel('Final Grade')

ax.legend()
ax.set_axisbelow(True)
plt.grid()
plt.show()
