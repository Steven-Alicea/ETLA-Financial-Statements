from src.globals.functions import create_directory, join_directory_and_file
from src.etl.extract.extract import extract_from_csv
from src.etl.transform.transform_wells_fargo_tesla import transform_wells_fargo_tesla
from src.etl.load.load import load_to_csv



source_file = "data/raw/Wells Fargo Tesla/Tesla Transaction History.csv"
target_directory = "data/processed/Wells Fargo Tesla"
target_file = "Tesla Transaction History.csv"


def etl_wells_fargo_tesla(df):
    df = extract_from_csv(df)
    df = transform_wells_fargo_tesla(df)
    print(df)
    create_directory(target_directory)
    csv_file_path = join_directory_and_file(target_directory, target_file)
    load_to_csv(df, csv_file_path)


def main():
    etl_wells_fargo_tesla(source_file)


if __name__ == '__main__':
    main()
