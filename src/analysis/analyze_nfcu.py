from src.analysis.analyze_helpers import *



def get_nfcu_transfers(df, direction, source_or_destination, start_date=None, end_date=None):
    title = f"NFCU Transfers {direction.capitalize()} {source_or_destination.title()}"
    if direction.lower() == "to":
        df = df[(df["Description"].str.contains(f"transfer {direction}", case=False)) & 
                (df["Description"].str.contains(source_or_destination, case=False)) & 
                (df["Amount"] < 0)]
    elif direction.lower() == "from":
        df = df[(df["Description"].str.contains(f"transfer {direction}", case=False)) & 
            (df["Description"].str.contains(source_or_destination, case=False)) & 
            (df["Amount"] > 0)]
    df = get_transactions_for_dates(df, start_date, end_date)
    title = rename_title_for_dates(title, start_date, end_date)
    print_analysis(df, title)
    return df

def get_nfcu_zelle_transfers(df, direction, source_or_destination, start_date=None, end_date=None):
    title = f"NFCU Zelle Transfers {direction.capitalize()} {source_or_destination.title()}"
    if (direction.lower() == "to"):
        df = df[(df["Description"].str.contains("Zelle")) &
                (df["Description"].str.contains(source_or_destination, case=False)) &
                (df["Amount"] < 0)]
    elif (direction.lower() == "from"):
        df = df[(df["Description"].str.contains("Zelle")) &
                (df["Description"].str.contains(source_or_destination, case=False)) &
                (df["Amount"] > 0)]
    df = get_transactions_for_dates(df, start_date, end_date)
    title = rename_title_for_dates(title, start_date, end_date)
    print_analysis(df, title)
    return df

def get_nfcu_cash_withdrawals(df):
    title = "NFCU Cash Withdrawals"
    df = df[df["Description"].str.contains("Cash Withdrawal", case=False)]
    print_analysis(df, title)
    return df

def get_nfcu_atm_withdrawals(df):
    title = "NFCU ATM Withdrawals"
    df = df[df["Description"].str.contains("ATM Withdrawal", case=False)]
    print_analysis(df, title)
    return df