import pandas as pd
import great_expectations as ge

def validate_data():

    df = pd.DataFrame({
        "experience": [1, 2, 3, 4, 5],
        "skills": [3, 5, 7, 9, 10],
        "projects": [1, 2, 3, 4, 5]
    })

    gdf = ge.from_pandas(df)

    # expectations (data quality rules)
    assert gdf["experience"].min() >= 0
    assert gdf["skills"].min() >= 0
    assert gdf["projects"].min() >= 0

    print("Data Validation Passed ✔")

if __name__ == "__main__":
    validate_data()