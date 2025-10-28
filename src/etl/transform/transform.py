import pandas as pd



def convert_dataframe_to_string(df):
    df = df.astype("string")
    return df

def transpose_dataframe(df):
    data = df.iloc[:, 1:]
    df = data.T
    return df

def rename_columns(df, column_names):
    df.columns = column_names
    return df
