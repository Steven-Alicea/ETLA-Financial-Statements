from src.globals.functions import *
from src.etl.extract.extract_chime import correct_row_and_extract_csv
from src.etl.transform.transform import convert_dataframe_to_string, rename_columns, combine_dataframes
from src.etl.transform.transform_chime import transform_checking_summary_data
from src.etl.load.load import load_to_csv



column_names = ["Statement Period",
                "Beginning Balance",
                "Deposits",
                "ATM Withdrawals",
                "Purchases",
                "Adjustments",
                "Transfers",
                "Round Up Transfers",
                "Fees",
                "SpotMe Tips",
                "Ending Balance"]

target_directory = f"data/processed/Chime"
target_file = "Chime Checking Summaries.csv"


def etl_chime_checking_summaries(start_year, end_year):
    csv_files = []
    dataframes = []
    for i in range(start_year, end_year + 1):
        csv_directory = (f"data/raw/Chime/Checking/{i}/Summary")
        csv_files.extend(get_sorted_csv_files(csv_directory))
    for file in csv_files:
        print(file)
        df = correct_row_and_extract_csv(file)
        df = convert_dataframe_to_string(df)
        df = rename_columns(df, column_names)
        df = transform_checking_summary_data(df)
        dataframes.append(df)
    combined_df = combine_dataframes(dataframes)
    print(combined_df)
    create_directory(target_directory)
    csv_file_path = join_directory_and_file(target_directory, target_file)
    load_to_csv(combined_df, csv_file_path)


def main():
    etl_chime_checking_summaries(2022, 2023)

if __name__ == '__main__':
    main()
    