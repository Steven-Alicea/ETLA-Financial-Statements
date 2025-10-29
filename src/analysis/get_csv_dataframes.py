import pandas as pd
from src.analysis.format_dataframes import *



# Get Chime Dataframe Funcitons
def get_chime_checking_summaries():
    df = pd.read_csv("data/processed/Chime/Chime Checking Summaries.csv")
    df = format_chime_checking_summary_dataframe(df)
    return df

def get_chime_checking_transactions():
    df = pd.read_csv("data/processed/Chime/Chime Checking Transactions.csv")
    df = format_chime_checking_transaction_dataframe(df)
    return df

def get_chime_credit_builder_card_summaries():
    df = pd.read_csv("data/processed/Chime/Chime Credit Builder Card Summaries.csv")
    df = format_chime_credit_builder_card_summary_dataframe(df)
    return df

def get_chime_credit_builder_card_transactions():
    df = pd.read_csv("data/processed/Chime/Chime Credit Builder Card Transactions.csv")
    df = format_chime_credit_builder_transaction_dataframe(df)
    return df

def get_chime_credit_builder_secured_summaries():
    df = pd.read_csv("data/processed/Chime/Chime Credit Builder Secured Summaries.csv")
    df = format_chime_credit_builder_secured_summary_dataframe(df)
    return df

def get_chime_credit_builder_secured_transactions():
    df = pd.read_csv("data/processed/Chime/Chime Credit Builder Secured Transactions.csv")
    df = format_chime_credit_builder_transaction_dataframe(df)
    return df

# Get NFCU Dataframe Funcitons
def get_nfcu_checking_summaries():
    df = pd.read_csv("data/processed/NFCU/NFCU Checking Summaries.csv")
    df = format_nfcu_checking_savings_summary_dataframe(df)
    return df

# Note: amount column contains nan values for begining and ending balance rows
def get_nfcu_checking_transactions():
    df = pd.read_csv("data/processed/NFCU/NFCU Checking Transactions.csv")
    df = format_nfcu_checking_savings_tranaction_dataframe(df)
    return df

def get_nfcu_credit_payments_and_credits():
    df = pd.read_csv("data/processed/NFCU/NFCU Credit Payments and Credits.csv")
    df = format_nfcu_credit_payments_credits_dataframe(df)
    return df

def get_nfcu_credit_summaries():
    df = pd.read_csv("data/processed/NFCU/NFCU Credit Summaries.csv")
    df = format_nfcu_credit_summary_dataframe(df)
    return df

def get_nfcu_credit_transactions():
    df = pd.read_csv("data/processed/NFCU/NFCU Credit Transactions.csv")
    df = format_nfcu_credit_transaction_dataframe(df)
    return df

# Note: payment due date column contains nan values for certain dates
def get_nfcu_navcheck_summaries():
    df = pd.read_csv("data/processed/NFCU/NFCU Navcheck Summaries.csv")
    df = format_nfcu_navcheck_summary_dataframe(df)
    return df

# Note: amount column contains nan values for begining & ending balance rows
def get_nfcu_navcheck_transactions():
    df = pd.read_csv("data/processed/NFCU/NFCU Navcheck Transactions.csv")
    df = format_nfcu_navcheck_transaction_dataframe(df)
    return df

def get_nfcu_savings_summaries():
    df = pd.read_csv("data/processed/NFCU/NFCU Savings Summaries.csv")
    df = format_nfcu_checking_savings_summary_dataframe(df)
    return df

# Note: amount column contains nan values for begining and ending balance rows
def get_nfcu_savings_transactions():
    df = pd.read_csv("data/processed/NFCU/NFCU Savings Transactions.csv")
    df = format_nfcu_checking_savings_tranaction_dataframe(df)
    return df

def main():
    #test
    # df = get_chime_checking_summaries()
    # df = get_chime_checking_transactions()
    # df = get_chime_credit_builder_card_summaries()
    # df = get_chime_credit_builder_card_transactions()
    # df = get_chime_credit_builder_secured_summaries()
    # df = get_chime_credit_builder_secured_transactions()
    
    # df = get_nfcu_checking_summaries()
    # df = get_nfcu_checking_transactions()
    # df = get_nfcu_credit_payments_and_credits()
    # df = get_nfcu_credit_summaries()
    # df = get_nfcu_credit_transactions()
    # df = get_nfcu_navcheck_summaries()
    # df = get_nfcu_navcheck_transactions()
    # df = get_nfcu_savings_summaries()
    df = get_nfcu_savings_transactions()
    print(df.info())
    print(df)


if __name__ == '__main__':
    main()