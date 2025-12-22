from src.analysis.analyze_helpers import *



def get_transactions_for_exact_amount(df, amount):
    title = f"Transactions For ${amount}"
    df =  df[df["Amount"] == amount]
    print_analysis(df, title)
    return df

def get_transactions_less_than_amount(df, amount, inclusive=False):
    title = f"Transactions Less Than ${amount}"
    if inclusive:
        df = df[df["Amount"] <= amount]
    else:
        df = df[df["Amount"] < amount]
    print_analysis(df, title)
    return df

def get_transactions_greater_than_amount(df, amount, inclusive=False):
    title = f"Transactions Greater Than ${amount}"
    if inclusive:
        df = df[df["Amount"] >= amount]
    else:
        df = df[df["Amount"] > amount]
    print_analysis(df, title)
    return df

def get_transactions_between_amounts(df, lower_amount, upper_amount, inclusive=False):
    title = f"Transactions Between ${lower_amount} And ${upper_amount}"
    if inclusive:
        df = df[(df["Amount"] >= lower_amount) & (df["Amount"] <= upper_amount)]
    else:
        df = df[(df["Amount"] > lower_amount) & (df["Amount"] < upper_amount)]
    print_analysis(df, title)
    return df

def get_transactions_on_date(df, date):
    title = f"Transactions On {date}"
    df =  df[df["Transaction Date"] == date]
    print_analysis(df, title)
    return df

def get_transactions_before_date(df, date, inclusive=False):
    title = f"Transactions Before {date}"
    if inclusive:
        df = df[df["Transaction Date"] >= date]
    else:
        df = df[df["Transaction Date"] > date]
    print_analysis(df, title)
    return df

def get_transactions_after_date(df, date, inclusive=False):
    title = f"Transactions After {date}"
    if inclusive:
        df =  df[df["Transaction Date"] >= date]
    else:
        df =  df[df["Transaction Date"] > date]
    print_analysis(df, title)
    return df

def get_transactions_between_dates(df, start_date, end_date, inclusive=False):
    title = f"Transactions Between {start_date} And {end_date}"
    if inclusive:
        df = df[(df["Transaction Date"] >= start_date) & (df["Transaction Date"] <= end_date)]
    else:
        df = df[(df["Transaction Date"] > start_date) & (df["Transaction Date"] < end_date)]
    print_analysis(df, title)
    return df

def get_transactions_by_description(df, description, start_date=None, end_date=None):
    title = f"{description.title()} Transactions"
    df = df[df["Description"].str.contains(description, case=False)]
    df = get_transactions_for_dates(df, start_date, end_date)
    title = rename_title_for_dates(title, start_date, end_date)
    print_analysis(df, title)
    return df
