import pandas as pd



def transform_wells_fargo_tesla(df):
    date_columns = ["Posting Date", "Next Due Date"]
    numeric_columns = ["Transaction Amount", 
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
    df[numeric_columns] = df[numeric_columns].fillna(0).apply(lambda x: x.apply(lambda y: f"{y:.2f}".format(y)))
    df[date_columns] = df[date_columns].apply(lambda x: pd.to_datetime(x, format='%Y-%m-%d'))
    return df
