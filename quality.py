def run_quality_checks(df):

    print("running quality checks")

    # null validation
    print(df.isnull().sum())

    # duplicate validation
    duplicates = df.duplicated().sum()

    print(f"duplicates: {duplicates}")

    # schema validation
    expected_columns = [
        "customerID",
        "gender",
        "tenure"
    ]

    for col in expected_columns:

        if col not in df.columns:

            raise Exception(
                f"missing column: {col}"
            )

    print("quality checks passed")