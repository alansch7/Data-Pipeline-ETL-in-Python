import pandas as pd

def extract_data():

    df = pd.read_csv(
        "data/WA_Fn-UseC_-Telco-Customer-Churn.csv"
    )

    print("data extracted")

    return df