import pandas as pd
from src.analysis.format_csv_dataframes import *



# Chime CSV Dataframe Retrieval Funcitons
def get_chime_checking_summaries_csv():
    df = pd.read_csv("data/processed/Chime/Chime Checking Summaries.csv")
    df = format_chime_checking_summary_dataframe(df)
    return df

def get_chime_checking_transactions_csv():
    df = pd.read_csv("data/processed/Chime/Chime Checking Transactions.csv")
    df = format_chime_checking_transaction_dataframe(df)
    return df

def get_chime_credit_builder_card_summaries_csv():
    df = pd.read_csv("data/processed/Chime/Chime Credit Builder Card Summaries.csv")
    df = format_chime_credit_builder_card_summary_dataframe(df)
    return df

def get_chime_credit_builder_card_transactions_csv():
    df = pd.read_csv("data/processed/Chime/Chime Credit Builder Card Transactions.csv")
    df = format_chime_credit_builder_transaction_dataframe(df)
    return df

def get_chime_credit_builder_secured_summaries_csv():
    df = pd.read_csv("data/processed/Chime/Chime Credit Builder Secured Summaries.csv")
    df = format_chime_credit_builder_secured_summary_dataframe(df)
    return df

def get_chime_credit_builder_secured_transactions_csv():
    df = pd.read_csv("data/processed/Chime/Chime Credit Builder Secured Transactions.csv")
    df = format_chime_credit_builder_transaction_dataframe(df)
    return df


# NFCU CSV Dataframe Retrieval Funcitons
def get_nfcu_checking_summaries_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Checking Summaries.csv")
    df = format_nfcu_checking_savings_summary_dataframe(df)
    return df

# Note: amount column contains nan values for begining and ending balance rows
def get_nfcu_checking_transactions_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Checking Transactions.csv")
    df = format_nfcu_checking_savings_tranaction_dataframe(df)
    return df

def get_nfcu_credit_payments_and_credits_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Credit Payments and Credits.csv")
    df = format_nfcu_credit_payments_credits_dataframe(df)
    return df

def get_nfcu_credit_summaries_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Credit Summaries.csv")
    df = format_nfcu_credit_summary_dataframe(df)
    return df

def get_nfcu_credit_transactions_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Credit Transactions.csv")
    df = format_nfcu_credit_transaction_dataframe(df)
    return df

# Note: payment due date column contains nan values for certain dates
def get_nfcu_navcheck_summaries_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Navcheck Summaries.csv")
    df = format_nfcu_navcheck_summary_dataframe(df)
    return df

# Note: amount column contains nan values for begining & ending balance rows
def get_nfcu_navcheck_transactions_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Navcheck Transactions.csv")
    df = format_nfcu_navcheck_transaction_dataframe(df)
    return df

def get_nfcu_savings_summaries_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Savings Summaries.csv")
    df = format_nfcu_checking_savings_summary_dataframe(df)
    return df

# Note: amount column contains nan values for begining and ending balance rows
def get_nfcu_savings_transactions_csv():
    df = pd.read_csv("data/processed/NFCU/NFCU Savings Transactions.csv")
    df = format_nfcu_checking_savings_tranaction_dataframe(df)
    return df


# Toyota CSV Dataframe Retrieval Functions
def get_toyota_transaction_history_csv():
    df = pd.read_csv("data/processed/Toyota/Toyota Transaction History.csv")
    df = format_toyota_transaction_dataframe(df)
    return df

def get_toyota_statemets_csv():
    df = pd.read_csv("data/processed/Toyota/Toyota Statements.csv")
    df = format_toyota_statement_dataframe(df)
    return df


# Wells Fargo Tesla CSV Dataframe Retrieval Function
def get_wells_fargo_tesla_transaction_history_csv():
    df = pd.read_csv("data/processed/Wells Fargo Tesla/Tesla Transaction History.csv")
    df = format_wells_fargo_tesla_transaction_dataframe(df)
    return df
