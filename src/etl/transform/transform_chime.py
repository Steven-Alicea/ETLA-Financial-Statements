import re
import pandas as pd
from src.globals.variables import months_dict



def correct_mismatch_rows(df):
    for i in range(len(df)):
        if df.isnull().iloc[i, 0]:
            df.iloc[i - 1, 1] = df.iloc[i - 1, 1] + " " + df.iloc[i, 1]
    df = df.dropna(subset=["Transaction Date"])
    return df

def add_statement_period_to_dataframe(df, file):
    year = re.split(r'[-.s]+', file)[1]
    month = re.split(r'[-.s]+', file)[2]
    month = months_dict.get(month)
    period = f"{month} {year}"
    df.insert(loc=0, column="Statement Period", value=period)
    return df


def transform_checking_transaction_data(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Description"] = df["Description"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]
                                 .str.replace(r'[$,]', '', regex=True)
                                 .str.replace(r'(-)$', r'\1', regex=True)
                                 .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                 ).apply(lambda x: f"{x:.2f}")
    df["Net Amount"] = pd.to_numeric(df["Net Amount"]
                                     .str.replace(r'[$,]', '', regex=True)
                                     .str.replace(r'(-)$', r'\1', regex=True)
                                     .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                     ).apply(lambda x: f"{x:.2f}")
    df["Settlement Date"] = pd.to_datetime(df["Settlement Date"])
    return df
