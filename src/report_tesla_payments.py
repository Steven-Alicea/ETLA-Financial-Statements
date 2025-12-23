import pandas as pd
import os
from dotenv import load_dotenv
from src.globals.functions import create_directory, join_directory_and_file
from src.etl.load.load import load_to_csv
from src.analysis.get_csv_dataframes import get_nfcu_checking_transactions_csv, get_wells_fargo_tesla_transaction_history_csv
from src.analysis.analyze import *
from src.analysis.analyze_nfcu import *



load_dotenv()

destination = os.getenv("DESTINATION_1")
gray_tesla_purchase_date = os.getenv("GRAY_TESLA_PURCHASE_DATE")
gray_tesla_down_payment_date = os.getenv("GRAY_TESLA_DOWNPAYMENT_DATE")
gray_tesla_down_payment_description = os.getenv("GRAY_TESLA_DOWNPAYMENT_DESCRIPTION")
gray_tesla_online_payment_description = os.getenv("GRAY_TESLA_ONLINE_PAYMENT_DESCRIPTION")
gray_tesla_transfer_amount = os.getenv("GRAY_TESLA_TRANSFER_AMOUNT")
white_tesla_payment_description = os.getenv("WHITE_TESLA_PAYMENT_DESCRIPTION")

nfcu_transactions = get_nfcu_checking_transactions_csv()
gray_tesla_transactions = get_wells_fargo_tesla_transaction_history_csv()

def format_report(df):
    df.drop("Balance", axis=1, inplace=True)
    df["Amount"] = df["Amount"].abs().apply(lambda x: f"${x:,.2f}")
    return df

def generate_gray_tesla_payment_report():
    # get down-payment
    down_payment = get_transactions_by_description(nfcu_transactions, gray_tesla_down_payment_description)
    down_payment = get_transactions_on_date(down_payment, gray_tesla_down_payment_date)
    # get transfers for payments
    transfers = get_nfcu_transfers(nfcu_transactions, "To", destination, start_date=gray_tesla_purchase_date)
    transfers = get_transactions_less_than_amount(transfers, float(gray_tesla_transfer_amount))
    # get online payments
    online_payments = get_transactions_by_description(nfcu_transactions, gray_tesla_online_payment_description)
    # get withdrawal for in-person teller payment
    teller_payment = get_nfcu_cash_withdrawals(nfcu_transactions)
    # concatenate dataframes
    dataframes = [down_payment, transfers, online_payments, teller_payment]
    df_tesla_payments = pd.concat(dataframes)
    # format dataframe
    df = format_report(df_tesla_payments)
    print(df)
    return df

def generate_white_tesla_payment_report():
    df_tesla_payments = get_transactions_by_description(nfcu_transactions, white_tesla_payment_description).copy()
    df = format_report(df_tesla_payments)
    print(df)
    return df


def main():
    target_directory = "data/reports"
    gray_tesla_csv_file = "Gray Tesla Payment History.csv"
    white_tesla_csv_file = "White Tesla Payment History.csv"
    create_directory(target_directory)
    gray_tesla_csv_file = join_directory_and_file(target_directory, gray_tesla_csv_file)
    white_tesla_csv_file = join_directory_and_file(target_directory, white_tesla_csv_file)

    df_gray_tesla_payment_history = generate_gray_tesla_payment_report()
    load_to_csv(df_gray_tesla_payment_history, gray_tesla_csv_file)

    df_white_tesla_payment_history = generate_white_tesla_payment_report()
    load_to_csv(df_white_tesla_payment_history, white_tesla_csv_file)


if __name__ == '__main__':
    main()
