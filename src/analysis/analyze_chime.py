from src.analysis.analyze_helpers import *



def get_chime_checking_account_deposits(df, source=None, start_date=None, end_date=None):
    title = "Chime Checking Account Deposits"
    if source:
        title = f"{title} From {source.title()}"
        df = df[df["Description"].str.contains(source, case=False)]
    df = df[(df["Type"] == "Deposit") & (df["Amount"] > 0)]
    df = get_transactions_for_dates(df, start_date, end_date)
    title = rename_title_for_dates(title, start_date, end_date)
    print_analysis(df, title)
    return df

def get_chime_checking_account_transfers(df, direction, source_or_destination, start_date=None, end_date=None):
    title = f"Chime Checking Account Transfers {direction.capitalize()} {source_or_destination.title()}"
    if direction.lower() == "to":
        df = df[(df["Description"].str.contains(f"transfer {direction} {source_or_destination}", case=False)) & 
                (df["Type"] == "Transfer") &
                (df["Amount"] < 0)]
    elif direction.lower() == "from":
        df = df[(df["Description"].str.contains(f"transfer {direction} {source_or_destination}", case=False)) & 
                (df["Type"] == "Transfer") &
                (df["Amount"] > 0)]
    df = get_transactions_for_dates(df, start_date, end_date)
    title = rename_title_for_dates(title, start_date, end_date)
    print_analysis(df, title)
    return df

def get_chime_purchases(df, purchase_description=None, start_date=None, end_date=None): 
    title = "Chime Purchases"
    if purchase_description:
        title = f"{title} Made At {purchase_description.title()}"
        df = df[df["Description"].str.contains(purchase_description, case=False)]
    df = df[(df["Type"] == "Purchase") & (df["Amount"] < 0)]
    df = get_transactions_for_dates(df, start_date, end_date)
    title = rename_title_for_dates(title, start_date, end_date)
    print_analysis(df, title)
    return df

def get_chime_withdrawals(df, location=None, start_date=None, end_date=None):  
    title = "Chime Withdrawals"
    df = df[df["Type"].str.contains("Withdrawal")]
    if location:
        title = f"{title} Made At {location.title()}"
        df = df[df["Description"].str.contains(location, case=False)]
    df = get_transactions_for_dates(df, start_date, end_date)
    title = rename_title_for_dates(title, start_date, end_date)
    print_analysis(df, title)
    return df
