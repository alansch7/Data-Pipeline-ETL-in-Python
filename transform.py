import pandas as pd

def transform_data(df):

    df["TotalCharges"] = pd.to_numeric(
        df["TotalCharges"],
        errors="coerce"
    )

    df["TotalCharges"] = df[
        "TotalCharges"
    ].fillna(0)

    print("data transformed")

    return df