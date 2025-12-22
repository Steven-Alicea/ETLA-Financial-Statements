import pandas as pd



# Format CSV Report Dataframe Function
def format_csv_report(df):
    date_columns = ["Statement Date",
                    "Transaction Date",
                    "Post Date",
                    "Settlement Date",
                    "Next Due Date",
                    "Payment Due Date",
                    "Date of Last Transaction",
                    "Maturity Date"]
    decimal_columns = ["Amount",
                       "Net Amount",
                       "Balance",
                       "Beginning Balance"
                       "Ending Balance",
                       "Deposits",
                       "Transfers",
                       "Withdrawals",
                       "ATM Withdrawals",
                       "Purchases",
                       "Adjustments",
                       "Round Up Transferes",
                       "Fees",
                       "SpotMe Tips",
                       "YTD Dividends",
                       "Past Due Payment Amount",
                       "Unpaid Late Charges",
                       "Miscellaneous Charges",
                       "Current Payment Due",
                       "Total Amount Due",
                       "Regular Payment Amount",
                       "Last Transaction Amount",
                       "Outstanding Balance",
                       "Principal",
                       "Interest",
                       "CPI",
                       "CPI Interest",
                       "Late Charges",
                       "Other Charges",
                       "Unapplied Amount",
                       "CPI Balance",
                       "Principal Balance",
                       "Payment Variance"]
    string_columns = ["Statement Period",
                      "Description",
                      "Type",
                      "Reference Number",
                      "Submitted By",
                      "Status"]
    for column in date_columns:
        if column in df.columns:
            df[column] = df[column].apply(lambda x: pd.to_datetime(x))
    for column in decimal_columns:
        if column in df.columns:
            df[column] = pd.to_numeric(df[column].str.replace('[\$,]', '', regex=True))
    for column in string_columns:
        if column in df.columns:
            df[column] = df[column].astype("string")
    return df