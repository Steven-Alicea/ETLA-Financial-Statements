import re
import pandas as pd
from src.globals.variables import months_dict


def correct_mismatch_rows(df): 
    for i in range(len(df)):
        if df.isnull().iloc[i, 0]:
            for j in range(2, len(df.columns)):
                if not df.isnull().iloc[i, j]:
                    df.iloc[i - 1, j] = df.iloc[i, j]
            df.iloc[i - 1, 1] = df.iloc[i - 1, 1] + " " + df.iloc[i, 1]
        if i > 1 and df.isnull().iloc[i, 0] and df.isnull().iloc[i - 1, 0]:
            df.iloc[i - 2, 1] = df.iloc[i - 2, 1] + " " + df.iloc[i, 1]
    df = df.dropna(subset=["Transaction Date"])
    return df

def add_year_to_transaction_date_column(df, file):
    file = file.split('-')
    year = int(file[1])
    if file[2] == next(iter(months_dict)):
        for i in range (len(df)):
            if str(df.iloc[i, 0]).startswith(next(reversed(months_dict))):
                df.iloc[i, 0] = str(year - 1) + '-' + df.iloc[i, 0]
            else:
                df.iloc[i, 0] = str(year) + '-' + df.iloc[i, 0]
    else:
        df["Transaction Date"] = str(year) + '-' + df["Transaction Date"]
    return df

def add_statement_period_to_dataframe(df, file):
    file = re.split(r'[-_\s]+', file)
    end_date = f"{file[2]}/{file[3]}/{file[1]}" 
    file[3] = str(int(file[3]) + 1)
    if file[2] == next(iter(months_dict)):
        file[1] = str(int(file[1]) - 1)
        file[2] = next(reversed(months_dict))
    else:
        file[2] = str(int(file[2]) - 1).zfill(2)
    period = f"{file[2]}/{file[3]}/{file[1]} to {end_date}"
    df.insert(loc=0, column="Statement Period", value=period)
    return df

def transform_checking_savings_transaction_data(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Description"] = df["Description"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]
                                 .str.replace(r'[$,]', '', regex=True)
                                 .str.replace(r'(-)$', r'\1', regex=True)
                                 .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                 ).apply(lambda x: f"{x:.2f}")
    df["Balance"] = pd.to_numeric(df["Balance"]
                                  .str.replace(r'[$,]', '', regex=True)
                                  .str.replace(r'(-)$', r'\1', regex=True)
                                  .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                  ).apply(lambda x: f"{x:.2f}")
    return df

def transform_checking_savings_transaction_data(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Description"] = df["Description"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]
                                 .str.replace(r'[$,]', '', regex=True)
                                 .str.replace(r'(-)$', r'\1', regex=True)
                                 .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                 ).apply(lambda x: f"{x:.2f}")
    df["Balance"] = pd.to_numeric(df["Balance"]
                                  .str.replace(r'[$,]', '', regex=True)
                                  .str.replace(r'(-)$', r'\1', regex=True)
                                  .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                  ).apply(lambda x: f"{x:.2f}")
    return df
