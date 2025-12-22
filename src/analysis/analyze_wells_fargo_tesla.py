from src.analysis.analyze_helpers import *



def get_transactions_on_post_date(df, date):
    title = f"Transactions On Post {date}"
    df =  df[df["Post Date"] == date]
    print_analysis(df, title)
    return df

def get_transactions_before_post_date(df, date, inclusive=False):
    title = f"Transactions Posted Before {date}"
    if inclusive:
        df =  df[df["Post Date"] <= date]
    else:
        df =  df[df["Post Date"] < date]
    print_analysis(df, title)
    return df

def get_transactions_after_post_date(df, date, inclusive=False):
    title = f"Transactions Posted After {date}"
    if inclusive:
        df =  df[df["Post Date"] >= date]
    else:
        df =  df[df["Post Date"] > date]
    print_analysis(df, title)
    return df

def get_transactions_between_post_dates(df, start_date, end_date, inclusive=False):
    title = f"Transactions Posted Between {start_date} And {end_date}"
    if inclusive:
        df = df[(df["Post Date"] >= start_date) & (df["Post Date"] <= end_date)]
    else:
        df = df[(df["Post Date"] > start_date) & (df["Post Date"] < end_date)]
    print_analysis(df, title)
    return df
