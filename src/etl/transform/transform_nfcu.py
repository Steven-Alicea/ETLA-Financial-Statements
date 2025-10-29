import re
import pandas as pd
from src.globals.variables import months_dict



def drop_first_row(df):
    return df.drop(df.index[0])

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

def transform_checking_savings_summary_data(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Previous Balance"] = pd.to_numeric(df["Previous Balance"]
                                           .str.replace(r'[$,]', '', regex=True)
                                           .str.replace(r'(-)$', r'\1', regex=True)
                                           .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                           ).apply(lambda x: f"{x:.2f}")
    df["Deposits"] = pd.to_numeric(df["Deposits"]
                                   .str.replace(r'[$,]', '', regex=True)
                                   ).apply(lambda x: f"{x:.2f}")
    df["Withdrawals"] = pd.to_numeric(df["Withdrawals"]
                                      .str.replace(r'[$,]', '', regex=True)
                                      ).apply(lambda x: f"{x:.2f}")
    df["Ending Balance"] = pd.to_numeric(df["Ending Balance"]
                                         .str.replace(r'[$,]', '', regex=True)
                                         .str.replace(r'(-)$', r'\1', regex=True)
                                         .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                         ).apply(lambda x: f"{x:.2f}")
    df["YTD Dividends"] = pd.to_numeric(df["YTD Dividends"]
                                        .str.replace(r'[$,]', '', regex=True)
                                        ).apply(lambda x: f"{x:.2f}")
    return df

def transform_navcheck_summary_data(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Credit Limit"] = pd.to_numeric(df["Credit Limit"]
                                       .str.replace('$', '')
                                       ).apply(lambda x: f"{x:.2f}")
    df["Outstanding Principal Balance"] = pd.to_numeric(df["Outstanding Principal Balance"]
                                                        .str.replace('$', '')
                                                        ).apply(lambda x: f"{x:.2f}")
    df["Outstanding Interest Charge"] = pd.to_numeric(df["Outstanding Interest Charge"]
                                                      .str.replace('$', '')
                                                      ).apply(lambda x: f"{x:.2f}")
    df["Outstanding Fees"] = pd.to_numeric(df["Outstanding Fees"]
                                           .str.replace('$', '')
                                           ).apply(lambda x: f"{x:.2f}")
    df["Total Outstanding Balance"] = pd.to_numeric(df["Total Outstanding Balance"]
                                                    .str.replace('$', '')
                                                    ).apply(lambda x: f"{x:.2f}")
    df["Available Credit"] = pd.to_numeric(df["Available Credit"]
                                           .str.replace('$', '')
                                           ).apply(lambda x: f"{x:.2f}")
    df["Miniumum Amount Due"] = pd.to_numeric(df["Miniumum Amount Due"]
                                              .str.replace('$', '')
                                              ).apply(lambda x: f"{x:.2f}")
    df["Past Due Amount"] = pd.to_numeric(df["Past Due Amount"]
                                          .str.replace('$', '')
                                          ).apply(lambda x: f"{x:.2f}")
    df["Payment Due Date"] = pd.to_datetime(df["Payment Due Date"], format='%m-%d-%y', errors='coerce')
    return df

def transform_navcheck_transaction_data(df):
    df[["Fees", "Interest", "Principal"]] = df[["Fees", "Interest", "Principal"]].fillna('0.00')
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"])
    df["Description"] = df["Description"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]
                                 .str.replace(',', '')
                                 ).apply(lambda x: f"{x:.2f}")
    df["Fees"] = pd.to_numeric(df["Fees"]
                               .str.replace(r'[ ,]', '', regex=True)
                               .str.replace(r'(-)$', r'\1', regex=True)
                               .str.replace(r'^(.*)-$', r'-\1', regex=True)
                               ).apply(lambda x: f"{x:.2f}")
    df["Interest"] = pd.to_numeric(df["Interest"]
                                   .str.replace(r'[ ,]', '', regex=True)
                                   .str.replace(r'(-)$', r'\1', regex=True)
                                   .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                     ).apply(lambda x: f"{x:.2f}")
    df["Principal"] = pd.to_numeric(df["Principal"]
                                    .str.replace(r'[ ,]', '', regex=True)
                                    .str.replace(r'(-)$', r'\1', regex=True)
                                    .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                    ).apply(lambda x: f"{x:.2f}")
    df["Balance"] = pd.to_numeric(df["Balance"]
                                  .str.replace(r'[ ,]', '', regex=True)
                                  .str.replace(r'(-)$', r'\1', regex=True)
                                  .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                  ).apply(lambda x: f"{x:.2f}")
    return df

def transform_credit_payments_credits(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], format='%m/%d/%y')
    df["Post Date"] = pd.to_datetime(df["Post Date"], format='%m/%d/%y')    
    df["Description"] = df["Description"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]
                                 .str.replace(r'[$,]', '', regex=True)
                                 ).apply(lambda x: f"{x:.2f}")
    return df

def transform_credit_summary_data(df):
    df.loc[df["Available Credit"] == "NONE", "Available Credit"] = '0.00'
    df.loc[df["Minimum Payment Due"] == "NONE", "Minimum Payment Due"] = '0.00'
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Previous Balance"] = pd.to_numeric(df["Previous Balance"]
                                           .str.replace(r'[$,]', '', regex=True)
                                           ).apply(lambda x: f"{x:.2f}")
    df["Payments"] = pd.to_numeric(df["Payments"]
                                   .str.replace(r'[$,]', '', regex=True)
                                   ).apply(lambda x: f"{x:.2f}")
    df["Other Credits"] = pd.to_numeric(df["Other Credits"]
                                        .str.replace(r'[$,]', '', regex=True)
                                        ).apply(lambda x: f"{x:.2f}")
    df["Purchases"] = pd.to_numeric(df["Purchases"]
                                    .str.replace(r'[$,]', '', regex=True)
                                    ).apply(lambda x: f"{x:.2f}")
    df["Cash Advances"] = pd.to_numeric(df["Cash Advances"]
                                        .str.replace(r'[$,]', '', regex=True)
                                        ).apply(lambda x: f"{x:.2f}")
    df["Fees Charged"] = pd.to_numeric(df["Fees Charged"]
                                       .str.replace(r'[$,]', '', regex=True)
                                       ).apply(lambda x: f"{x:.2f}")
    df["Interest Charged"] = pd.to_numeric(df["Interest Charged"]
                                      .str.replace(r'[$,]', '', regex=True)
                                      ).apply(lambda x: f"{x:.2f}")
    df["New Balance"] = pd.to_numeric(df["New Balance"]
                                      .str.replace(r'[$,]', '', regex=True)
                                      ).apply(lambda x: f"{x:.2f}")
    df["Past Due Amount"] = pd.to_numeric(df["Past Due Amount"]
                                          .str.replace(r'[$,]', '', regex=True)
                                          ).apply(lambda x: f"{x:.2f}")
    df["Over Limit Amount"] = pd.to_numeric(df["Over Limit Amount"]
                                            .str.replace(r'[$,]', '', regex=True)
                                            ).apply(lambda x: f"{x:.2f}")
    df["Credit Limit"] = pd.to_numeric(df["Credit Limit"]
                                       .str.replace(r'[$,]', '', regex=True)
                                       ).apply(lambda x: f"{x:.2f}")
    df["Available Credit"] = pd.to_numeric(df["Available Credit"]
                                           .str.replace(r'[$,]', '', regex=True)
                                           ).apply(lambda x: f"{x:.2f}")
    df["Cash Limit"] = pd.to_numeric(df["Cash Limit"]
                                     .str.replace(r'[$,]', '', regex=True)
                                     ).apply(lambda x: f"{x:.2f}")
    df["Available Cash"] = pd.to_numeric(df["Available Cash"]
                                         .str.replace(r'[$,]', '', regex=True)
                                         ).apply(lambda x: f"{x:.2f}")
    df["Statement Closing Date"] = pd.to_datetime(df["Statement Closing Date"])
    df["Days in Billing Cycle"] = pd.to_numeric(df["Days in Billing Cycle"]
                                                .str.replace(r'[$,]', '', regex=True)
                                                ).apply(lambda x: f"{x:.2f}")
    df["Minimum Payment Due"] = pd.to_numeric(df["Minimum Payment Due"]
                                              .str.replace(r'[$,]', '', regex=True)
                                              ).apply(lambda x: f"{x:.2f}")
    df["Payment Due Date"] = pd.to_datetime(df["Payment Due Date"])
    return df

def transform_credit_transaction_data(df):
    df["Statement Period"] = df["Statement Period"].astype("string")
    df["Transaction Date"] = pd.to_datetime(df["Transaction Date"], format='%m/%d/%y')
    df["Post Date"] = pd.to_datetime(df["Post Date"], format ='%m/%d/%y')
    df["Description"] = df["Description"].astype("string")
    df["Amount"] = pd.to_numeric(df["Amount"]
                                 .str.replace(r'[$,]', '', regex=True)
                                 ).apply(lambda x: f"{x:.2f}")
    return df
