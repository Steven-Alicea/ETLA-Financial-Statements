# Analysis Output Helper
def print_analysis(df, title):
    print(title)
    print(df)


# Title Modification Helpers
def rename_title_for_dates(title, start_date, end_date):
    if start_date and end_date:
        title = f"{title} Between {start_date} and {end_date}"
    elif start_date and not end_date:
        title = f"{title} After {start_date}"
    elif not start_date and end_date:
        title = f"{title} Before {end_date}"
    return title


# Data Retrieval Helpers
def get_statements_for_dates(df, start_date, end_date):
    if start_date and end_date:
        df = df[(df["Statement Date"] >= start_date) & (df["Statement Date"] <= end_date)]
    elif start_date and not end_date:
        df = df[df["Statement Date"] >= start_date]
    elif not start_date and end_date:
        df = df[df["Statement Date"] <= end_date]
    return df

def get_transactions_for_amounts(df, lower_amount, upper_amount):
    if lower_amount and upper_amount:
        df = df[(df["Amount"] >= lower_amount) & (df["Amount"] <= upper_amount)]
    elif lower_amount and not upper_amount:
        df = df[(df["Amount"] >= lower_amount)]
    elif not lower_amount and lower_amount:
        df = df[(df["Amount"] <= upper_amount)]
    return df

def get_transactions_for_dates(df, start_date, end_date):
    if start_date and end_date:
        df = df[(df["Transaction Date"] >= start_date) & (df["Transaction Date"] <= end_date)]
    elif start_date and not end_date:
        df = df[df["Transaction Date"] >= start_date]
    elif not start_date and end_date:
        df = df[df["Transaction Date"] <= end_date]
    return df
