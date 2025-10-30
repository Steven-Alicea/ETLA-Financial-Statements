from analysis.analyze_helpers import *



def get_transactions_for_exact_amount(df, amount):
    title = f"Transactions for {amount}"
    df =  df[(df["Amount"] == amount)]
    print_analysis(df, title)
    return df

def get_transactions_for_amounts(df, lower_amount, upper_amount):
    if lower_amount and upper_amount:
        df = df[(df["Amount"] >= lower_amount) & (df["Amount"] <= upper_amount)]
    elif lower_amount and not upper_amount:
        df = df[(df["Amount"] >= lower_amount)]
    elif not lower_amount and lower_amount:
        df = df[(df["Amount"] <= upper_amount)]
    return df

def get_transactions_on_date(df, date):
    title = f"Transactions on {date}"
    df =  df[(df["Transaction Date"] == date)]
    print_analysis(df, title)
    return df

# create function to check the input format for dates 
# (yyyy-mm-dd | mm/dd/yyyy | jan dd, yyyy | jan d, yyyy | january dd, yyyy | january d, yyyy)
def get_transactions_for_dates(df, start_date, end_date):
    if start_date and end_date:
        df = df[(df["Transaction Date"] >= start_date) & (df["Transaction Date"] <= end_date)]
    elif start_date and not end_date:
        df = df[(df["Transaction Date"] >= start_date)]
    elif not start_date and end_date:
        df = df[(df["Transaction Date"] <= end_date)]
    return df

def get_transactions_by_description(df, description, start_date=None, end_date=None):
    title = f"{description.title()} Transactions"
    df = df[df["Description"].str.contains(description, case=False)]
    df = get_transactions_for_dates(df, start_date, end_date)
    title = rename_title_for_dates(title, start_date, end_date)
    print_analysis(df, title)
    return df
