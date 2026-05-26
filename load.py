from sqlalchemy import create_engine

def load_data(df):

    engine = create_engine(
        "postgresql://postgres:postgres123@localhost:5432/postgres"
    )

    df.to_sql(
        "telco_customers",
        engine,
        if_exists="replace",
        index=False
    )

    print("data loaded")