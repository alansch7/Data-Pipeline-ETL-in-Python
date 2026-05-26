from extract import extract_data
from transform import transform_data
from quality import run_quality_checks
from load import load_data

def main():

    df = extract_data()

    df = transform_data(df)

    run_quality_checks(df)

    load_data(df)

    print("pipeline completed")

if __name__ == "__main__":
    main()