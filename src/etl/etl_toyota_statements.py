from src.globals.functions import *
from src.etl.extract.extract import extract_from_csv_without_header
from src.etl.transform.transform import transpose_dataframe, rename_columns, combine_dataframes
from src.etl.transform.transform_toyota import transform_toyota_statements
from src.etl.load.load import load_to_csv



target_directory = "data/processed/Toyota"
target_file = "Toyota Statements.csv"


def etl_toyota_statements(start_year, end_year):
    csv_files =[]
    dataframes = []
    for i in range(start_year, end_year + 1):
        csv_directory = f"data/raw/Toyota/Statements/{i}"
        csv_files.extend(get_sorted_csv_files(csv_directory))
    for file in csv_files:
        print(file)
        df = extract_from_csv_without_header(file)
        column_names = df.iloc[:,0].tolist()
        df = transpose_dataframe(df)
        df = rename_columns(df, column_names)
        df = transform_toyota_statements(df)
        dataframes.append(df)
    combined_df = combine_dataframes(dataframes)
    print(combined_df)
    create_directory(target_directory)
    csv_file_path = join_directory_and_file(target_directory, target_file)
    load_to_csv(combined_df, csv_file_path)


def main():
    etl_toyota_statements(2020, 2023)


if __name__ == '__main__':
    main()
