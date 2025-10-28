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

def transform_checking_summary_data(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Beginning Balance"] =  pd.to_numeric(df["Beginning Balance"]
                                             .str.replace(r'[$,]', '', regex=True)
                                             ).apply(lambda x: f"{x:.2f}")
    df["Deposits"] =  pd.to_numeric(df["Deposits"]
                                    .str.replace(r'[$,]', '', regex=True)
                                    ).apply(lambda x: f"{x:.2f}")
    df["ATM Withdrawals"] =  pd.to_numeric(df["ATM Withdrawals"]
                                           .str.replace(r'[$,]', '', regex=True)
                                           .str.replace(r'(-)$', r'\1', regex=True)
                                           .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                           ).apply(lambda x: f"{x:.2f}")
    df["Purchases"] =  pd.to_numeric(df["Purchases"]
                                     .str.replace(r'[$,]', '', regex=True)
                                     .str.replace(r'(-)$', r'\1', regex=True)
                                     .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                     ).apply(lambda x: f"{x:.2f}")
    df["Adjustments"] =  pd.to_numeric(df["Adjustments"]
                                       .str.replace(r'[$,]', '', regex=True)
                                       .str.replace(r'(-)$', r'\1', regex=True)
                                       .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                       ).apply(lambda x: f"{x:.2f}")
    df["Transfers"] =  pd.to_numeric(df["Transfers"]
                                     .str.replace(r'[$,]', '', regex=True)
                                     .str.replace(r'(-)$', r'\1', regex=True)
                                     .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                     ).apply(lambda x: f"{x:.2f}")
    df["Round Up Transfers"] =  pd.to_numeric(df["Round Up Transfers"]
                                              .str.replace(r'[$,]', '', regex=True)
                                              .str.replace(r'(-)$', r'\1', regex=True)
                                              .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                              ).apply(lambda x: f"{x:.2f}")
    df["Fees"] =  pd.to_numeric(df["Fees"]
                                .str.replace(r'[$,]', '', regex=True)
                                .str.replace(r'(-)$', r'\1', regex=True)
                                .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                ).apply(lambda x: f"{x:.2f}")
    df["SpotMe Tips"] =  pd.to_numeric(df["SpotMe Tips"]
                                       .str.replace(r'[$,]', '', regex=True)
                                       .str.replace(r'(-)$', r'\1', regex=True)
                                       .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                       ).apply(lambda x: f"{x:.2f}")
    df["Ending Balance"] =  pd.to_numeric(df["Ending Balance"]
                                          .str.replace(r'[$,]', '', regex=True)
                                          ).apply(lambda x: f"{x:.2f}")
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
