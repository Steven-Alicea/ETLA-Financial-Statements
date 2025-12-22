from src.analysis.analyze_helpers import *



# Toyota Statement Data Retrieval Functions
def get_statement_on_date(df, date):
    title = f"Statements On {date}"
    df = df[df["Statement Date"] == date]
    print_analysis(df, title)
    return df

def get_statements_before_date(df, date, inclusive=False):
    title = f"Statements Before {date}"
    if inclusive:
        df = df[df["Statement Date"] <= date]
    else:
        df = df[df["Statement Date"] < date]
    print_analysis(df, title)
    return df


def get_statements_after_date(df, date, inclusive=False):
    title = f"Statements After {date}"
    if inclusive:
        df = df[df["Statement Date"] >= date]
    else:
        df = df[df["Statement Date"] > date]
    print_analysis(df, title)
    return df

def get_statements_between_dates(df, start_date, end_date, inclusive=False):
    title = f"Statements Between {start_date} And {end_date}"
    if inclusive:
        df = df[(df["Statement Date"] >= start_date) & (df["Statement Date"] <= end_date)]
    else:
        df = df[(df["Statement Date"] > start_date) & (df["Statement Date"] < end_date)]
    print_analysis(df, title)
    return df


# Toyota Transaction Data Retrieval Functions
def get_transactions_by_status(df, status):
    title = f"Statements With {status} Status"
    df = df[df["Status"].str.contains(status, case=False)]
    print_analysis(df, title)
    return df

