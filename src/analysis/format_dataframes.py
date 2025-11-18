import pandas as pd
from decimal import Decimal



# Format Chime Dataframe Funcitons
def format_chime_checking_summary_dataframe(df):
    decimal_columns = ["Beginning Balance",
                       "Deposits",
                       "ATM Withdrawals",
                       "Purchases",
                       "Adjustments",
                       "Transfers",
                       "Round Up Transfers",
                       "Fees",
                       "SpotMe Tips",
                       "Ending Balance"]
    df["Statement Period"] = df["Statement Period"].astype("string")
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_chime_checking_transaction_dataframe(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Description"] = df["Description"].astype("string")
    df["Type"] = df["Type"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]).apply(lambda x: Decimal(f"{x:.2f}"))
    df["Net Amount"] = pd.to_numeric(df["Net Amount"]).apply(lambda x: Decimal(f"{x:.2f}"))
    df["Settlement Date"] = pd.to_datetime(df["Transaction Date"])
    return df

def format_chime_credit_builder_card_summary_dataframe(df):
    decimal_columns = ["Last Month's Balance",
                       "Payments/Credits",
                       "New Spending",
                       "Fees",
                       "New Balance",
                       "Total Due"]
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Payment Due Date"] = pd.to_datetime(df["Payment Due Date"])
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_chime_credit_builder_secured_summary_dataframe(df):
    decimal_columns = ["Beginning Balance", "Deposits", "Transfers", "Ending Balance"]
    df["Statement Period"] = df["Statement Period"].astype("string")
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_chime_credit_builder_transaction_dataframe(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Description"] = df["Description"].astype("string")
    df["Type"] = df["Type"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]).apply(lambda x: Decimal(f"{x:.2f}"))
    df["Settlement Date"] = pd.to_datetime(df["Settlement Date"])
    return df


# Format NFCU Dataframe Funcitons
def format_nfcu_checking_savings_summary_dataframe(df):
    decimal_columns = ["Previous Balance", "Deposits", "Withdrawals", "Ending Balance", "YTD Dividends"]
    df["Statement Period"] = df["Statement Period"].astype("string")
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_nfcu_checking_savings_tranaction_dataframe(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Description"] = df["Description"].astype("string")
    df["Amount"] = df["Amount"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Balance"] = df["Balance"].apply(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_nfcu_credit_payments_credits_dataframe(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Post Date"] = pd.to_datetime(df["Post Date"])
    df["Reference Number"] = df["Reference Number"].astype("string")
    df["Description"] = df["Description"].astype("string")
    df["Submitted By"] = df["Submitted By"].astype("string")
    df["Amount"] = df["Amount"].apply(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_nfcu_credit_summary_dataframe(df):
    decimal_columns = ["Previous Balance",
                       "Payments",
                       "Other Credits",
                       "Purchases",
                       "Cash Advances",
                       "Fees Charged",
                       "Interest Charged",
                       "New Balance",
                       "Past Due Amount",
                       "Over Limit Amount",
                       "Credit Limit",
                       "Available Credit",
                       "Cash Limit",
                       "Available Cash",
                       "Days in Billing Cycle",
                       "Minimum Payment Due"]
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Statement Closing Date"] = pd.to_datetime(df["Statement Closing Date"])
    df["Payment Due Date"] = pd.to_datetime(df["Payment Due Date"])
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_nfcu_credit_transaction_dataframe(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Post Date"] = pd.to_datetime(df["Post Date"])
    df["Reference Number"] = df["Reference Number"].astype("string")
    df["Description"] = df["Description"].astype("string")
    df["Amount"] = df["Amount"].apply(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_nfcu_navchk_summary_dataframe(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Credit Limit"] = df["Credit Limit"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Outstanding Principal Balance"] = df["Outstanding Principal Balance"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Outstanding Interest Charge"] = df["Outstanding Interest Charge"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Outstanding Fees"] = df["Outstanding Fees"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Total Outstanding Balance"] = df["Total Outstanding Balance"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Available Credit"] = df["Available Credit"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Miniumum Amount Due"] = df["Miniumum Amount Due"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Past Due Amount"] = df["Past Due Amount"].apply(lambda x: Decimal(f"{x:.2f}"))
    df["Payment Due Date"] = pd.to_datetime(df["Payment Due Date"])
    return df

def format_nfcu_navcheck_summary_dataframe(df):
    decimal_columns = ["Credit Limit",
                       "Outstanding Principal Balance",
                       "Outstanding Interest Charge",
                       "Outstanding Fees",
                       "Total Outstanding Balance",
                       "Available Credit",
                       "Miniumum Amount Due",
                       "Past Due Amount"]
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Payment Due Date"] = pd.to_datetime(df["Payment Due Date"])
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_nfcu_navcheck_transaction_dataframe(df):
    decimal_columns = ["Amount", "Fees", "Interest", "Principal", "Balance"]
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    return df


# format Tesla dataframes
def format_toyota_transaction_dataframe(df):
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Status"] = df["Status"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]).apply(lambda x: Decimal(f"{x:.2f}"))
    return df

def format_toyota_statement_dataframe(df):
    date_columns = ["Statement Date",
                    "Payment Due Date",
                    "Date of Last Transaction",
                    "Maturity Date"]
    decimal_columns = ["Past Due Payment Amount", 
                       "Unpaid Late Charges",
                       "Miscellaneous Charges",
                       "Current Payment Due",
                       "Total Amount Due",
                       "Regular Payment Amount",
                       "Last Transaction Amount",
                       "Monthly Payments Made",
                       "Outstanding Balance"]
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    df[date_columns] = df[date_columns].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    df["Monthly Payments Made"] = df["Monthly Payments Made"].astype(int)
    return df


# format Wells Fargo Tesla dataframe
def format_wells_fargo_tesla_transaction_dataframe(df):
    date_columns = ["Posting Date", "Next Due Date"]
    decimal_columns = ["Transaction Amount", 
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
    df[decimal_columns] = df[decimal_columns].map(lambda x: Decimal(f"{x:.2f}"))
    df[date_columns] = df[date_columns].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    df["Transaction Description"] = df["Transaction Description"].astype("string")
    return df
