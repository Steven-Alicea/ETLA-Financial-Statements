from src.globals.functions import *
from src.etl.extract.extract import extract_from_csv_without_header
from src.etl.transform.transform import transpose_dataframe, convert_dataframe_to_string, rename_columns, combine_dataframes
from src.etl.transform.transform_nfcu import add_statement_period_to_dataframe, transform_navcheck_summary_data
from src.etl.load.load import load_to_csv



column_names = ["Credit Limit",
                "Outstanding Principal Balance",
                "Outstanding Interest Charge",
                "Outstanding Fees",
                "Total Outstanding Balance",
                "Available Credit",
                "Miniumum Amount Due",
                "Past Due Amount",
                "Payment Due Date"]

target_directory = f"data/processed/NFCU"
target_file = "NFCU Navcheck Summaries.csv"


def etl_nfcu_navcheck_summaries(start_year, end_year):
    csv_files = []
    dataframes = []
    for i in range(start_year, end_year + 1):
        csv_directory = (f"data/raw/NFCU/Navcheck/{i}/Summary")
        csv_files.extend(get_sorted_csv_files(csv_directory))
    for file in csv_files:
        df = extract_from_csv_without_header(file)
        df = transpose_dataframe(df)
        df = convert_dataframe_to_string(df)
        df = rename_columns(df, column_names)
        df = add_statement_period_to_dataframe(df, file.name)
        df = transform_navcheck_summary_data(df)
        dataframes.append(df)
    combined_df = combine_dataframes(dataframes)
    print(combined_df)
    create_directory(target_directory)
    csv_file_path = join_directory_and_file(target_directory, target_file)
    load_to_csv(combined_df, csv_file_path)


def main():
    etl_nfcu_navcheck_summaries(2021, 2023)


if __name__ == '__main__':
    main()
