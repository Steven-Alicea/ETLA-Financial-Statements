import pandas as pd
from globals.functions import join_directory_and_file



directory = "reports"


def get_csv_report(file_name):
    report_file = join_directory_and_file(directory, file_name)
    return pd.read_csv(report_file, skipfooter=3, engine='python')
