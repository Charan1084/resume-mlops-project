from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
import pandas as pd

def run_drift_check():

    reference_data = pd.DataFrame({
        "experience": [1, 2, 3, 4, 5],
        "skills": [3, 5, 7, 9, 10],
        "projects": [1, 2, 3, 4, 5]
    })

    current_data = pd.DataFrame({
        "experience": [2, 3, 4, 5, 6],
        "skills": [4, 6, 8, 10, 12],
        "projects": [2, 3, 4, 5, 6]
    })

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference_data, current_data=current_data)

    report.save_html("drift_report.html")

    print("Drift report generated")