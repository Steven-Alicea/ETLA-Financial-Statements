import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv
from src.globals.functions import create_directory, join_directory_and_file
from src.etl.load.load import load_to_csv_indexed
from src.analysis.get_csv_dataframes import get_toyota_statemets_csv, get_toyota_transaction_history_csv
from src.analysis.get_csv_report_dataframe import *
from src.analysis.analyze import *
from src.analysis.analyze_toyota import *



pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)

load_dotenv()

source_1 = os.getenv("SOURCE_1")
incident_date = os.getenv("INCIDENT_DATE")

toyota_statements = get_toyota_statemets_csv()
toyota_transactions = get_toyota_transaction_history_csv()

report_file_list = [f"Chime Checking Transfers From Erica Totals.csv",
                    f"Chime Checking Transfers To {source_1} Totals.csv",
                    f"NFCU Checking Transfers From {source_1} Totals.csv",
                    f"NFCU Checking Transfers To {source_1} Totals.csv",
                    f"NFCU Savings Transfers From {source_1} Totals.csv",
                    f"NFCU Savings Transfers To {source_1} Totals.csv"]


def generate_toyota_payment_history_report():
    # get transactions and statements after specific date
    df_transactions = get_transactions_after_date(toyota_transactions, incident_date)
    df_stmt = get_statements_after_date(toyota_statements, incident_date)

    # get transactions with status
    df_paid = get_transactions_by_status(df_transactions, "Paid")
    df_returned = get_transactions_by_status(df_transactions, "Refund Payment")
    df_fees = get_transactions_by_status(df_transactions, "Refund Fee")

    # select necessary columns
    df_paid = df_paid[["Transaction Date", "Amount"]]
    df_returned = df_returned[["Transaction Date", "Amount"]]
    df_fees = df_fees[["Transaction Date", "Amount"]]
    df_stmt = toyota_statements[["Statement Date",
                                 "Past Due Payment Amount",
                                 "Unpaid Late Charges",
                                 "Total Amount Due",
                                 "Payment Due Date",
                                 "Last Transaction Amount",
                                 "Date of Last Transaction",
                                 "Outstanding Balance"]]

    # rename columns for uniformity and applicability
    df_paid.rename(columns={"Transaction Date": "Date", "Amount": "Payment"}, inplace=True)
    df_returned.rename(columns={"Transaction Date": "Date", "Amount": "Returned Payment"}, inplace=True)
    df_fees.rename(columns={"Transaction Date": "Date", "Amount": "Late Fee Charge"}, inplace=True)
    df_stmt.rename(columns={"Statement Date": "Date",
                            "Past Due Payment Amount": "Past Due Amount",
                            "Unpaid Late Charges": "Unpaid Late Fee Charges",
                            "Date of Last Transaction": "Last Transaction Date"}, inplace=True)

    # set date as the index
    df_paid.set_index("Date", inplace=True)
    df_returned.set_index("Date", inplace=True)
    df_fees.set_index("Date", inplace=True)
    df_stmt.set_index("Date", inplace=True)

    # join dataframes
    df = df_paid.join(df_returned, how="outer")
    df = df.join(df_fees, how="outer")
    df = df.join(df_stmt, how="outer")

    # reorder columns for readability and understanding
    df = df[["Payment",
             "Returned Payment",
             "Late Fee Charge",
             "Unpaid Late Fee Charges",
             "Past Due Amount",
             "Total Amount Due",
             "Payment Due Date",
             "Last Transaction Date",
             "Last Transaction Amount",
             "Outstanding Balance"]]
    
    # format report
    decimal_columns = ["Payment",
                       "Returned Payment",
                       "Late Fee Charge",
                       "Unpaid Late Fee Charges",
                       "Past Due Amount",
                       "Total Amount Due",
                       "Last Transaction Amount",
                       "Outstanding Balance"]
    df.loc[:, decimal_columns] = df.loc[:, decimal_columns].map(lambda x: f"${x:,.2f}")
    df.loc[:, decimal_columns] = np.where(df.loc[:, decimal_columns] == f"${np.nan}", np.nan, df.loc[:, decimal_columns])
    print(df) 
    return df


def main():
    target_directory = "data/reports"
    csv_file = "Toyota Payment History.csv"
    create_directory(target_directory)
    csv_file = join_directory_and_file(target_directory, csv_file)

    df_toyota_payment_history = generate_toyota_payment_history_report()
    load_to_csv_indexed(df_toyota_payment_history, csv_file)


if __name__ == '__main__':
    main()
