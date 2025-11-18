import pandas as pd



def transform_wells_fargo_tesla(df):
    df.rename(columns={"Posting Date": "Post Date"}, inplace=True)
    df.rename(columns={"Transaction Description": "Description"}, inplace=True)
    df.rename(columns={"Transaction Amount": "Amount"}, inplace=True)
    date_columns = ["Post Date", "Next Due Date"]
    numeric_columns = ["Amount", 
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
