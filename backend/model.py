from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([
    [1, 3, 1],
    [2, 5, 2],
    [3, 7, 3],
    [4, 9, 4],
    [5, 10, 5]
])

y = np.array([0, 0, 1, 1, 1])

model = RandomForestClassifier()
model.fit(X, y)

def predict(data):
    data = np.array(data).reshape(1, -1)
    return model.predict(data)[0]