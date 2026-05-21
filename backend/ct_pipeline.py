import pandas as pd
import joblib
import mlflow
import mlflow.sklearn

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load latest dataset
data = pd.read_csv("../data/resumes.csv")

X = data[["experience", "skills", "projects"]]
y = data["shortlisted"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

mlflow.set_experiment("continuous-training-resume-model")

with mlflow.start_run():

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # Save model locally
    joblib.dump(model, "resume_model.pkl")

    # Log with MLflow
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_param("n_estimators", 100)
    mlflow.log_metric("accuracy", accuracy)
    mlflow.sklearn.log_model(model, "resume_model")

    print("Continuous Training Completed")
    print("Model Accuracy:", accuracy)
    print("New model saved as resume_model.pkl")
    print("Experiment logged in MLflow")