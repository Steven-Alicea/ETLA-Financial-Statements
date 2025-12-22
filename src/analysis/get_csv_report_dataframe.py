import pandas as pd
from src.globals.functions import join_directory_and_file
from src.analysis.format_csv_report_dataframes import format_csv_report



directory = "data/reports"


def get_csv_report(file_name):
    report_file = join_directory_and_file(directory, file_name)
    df = pd.read_csv(report_file, skipfooter=3, engine='python')
    format_csv_report(df)
    return df
