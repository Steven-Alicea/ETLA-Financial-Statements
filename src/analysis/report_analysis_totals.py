from src.analysis.report_helpers import *
from src.globals.functions import create_directory, join_directory_and_file
from src.etl.load.load import load_to_csv



target_directory = "data/reports"


def print_totals_report(df, title):
    df = format_dataframe_for_totals_report(df)
    count_total = get_total_count(df)
    amount_total = get_total_amount(df)
    df = format_dataframe_for_totals_report(df, currency=True)
    print(title)
    print(df)
    print(f"{count_total[0]} = {count_total[1]}")
    print(f"{amount_total[0]} = {amount_total[1]}")

def generate_totals_csv_report(df, title):
    df = format_dataframe_for_totals_report(df)
    count_total = get_total_count(df)
    amount_total = get_total_amount(df)
    df = format_dataframe_for_totals_report(df, currency=True)
    file_name = f"{title}.csv"
    create_directory(target_directory)
    csv_file = join_directory_and_file(target_directory, file_name)
    load_to_csv(df, csv_file)
    write_totals_to_csv(csv_file, count_total, amount_total)
    print(f"Report: {csv_file}")
