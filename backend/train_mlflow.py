import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# dataset (resume features)
X = np.array([
    [1, 3, 1],
    [2, 5, 2],
    [3, 7, 3],
    [4, 9, 4],
    [5, 10, 5]
])

y = np.array([0, 0, 1, 1, 1])

mlflow.set_experiment("resume-shortlisting-mlops")

with mlflow.start_run():

    model = RandomForestClassifier(n_estimators=50)
    model.fit(X, y)

    accuracy = model.score(X, y)

    mlflow.log_param("model", "RandomForest")
    mlflow.log_param("n_estimators", 50)

    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(model, "model")

    print("MLflow experiment logged successfully")