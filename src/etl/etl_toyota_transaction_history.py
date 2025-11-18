from src.globals.functions import *
from src.etl.extract.extract import extract_from_csv
from src.etl.transform.transform_toyota import drop_duplicate_header_rows, correct_mismatch_rows, transform_toyota_transactions
from src.etl.load.load import load_to_csv



source_file = "data/raw/Toyota/Transactions/tabula-transaction_history.csv"
target_directory = "data/processed/Toyota"
target_file = "Toyota Transaction History.csv"


def etl_toyota_transaction_history(csv_file):
    df = extract_from_csv(csv_file)
    df = drop_duplicate_header_rows(df)
    df = correct_mismatch_rows(df)
    df = transform_toyota_transactions(df)
    print(df)

    create_directory(target_directory)
    csv_file_path = join_directory_and_file(target_directory, target_file)
    load_to_csv(df, csv_file_path)


def main():
    etl_toyota_transaction_history(source_file)


if __name__ == '__main__':
    main()
