import pandas as pd



def transform_toyota_statements(df):
    df.rename(columns={"Outstanding Balance*": "Outstanding Balance"}, inplace=True)
    df["Statement Date"] = pd.to_datetime(df["Statement Date"], format='%m/%d/%Y')
    df["Past Due Payment Amount"] = pd.to_numeric(df["Past Due Payment Amount"]
                                                  .str.replace(r'[$,]', '', regex=True)
                                                  .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                                  ).apply(lambda x: f"{x:.2f}")
    df["Unpaid Late Charges"] = pd.to_numeric(df["Unpaid Late Charges"]
                                              .str.replace(r'[$,]', '', regex=True)
                                              .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                              ).apply(lambda x: f"{x:.2f}")
    df["Miscellaneous Charges"] = pd.to_numeric(df["Miscellaneous Charges"]
                                                .str.replace(r'[$,]', '', regex=True)
                                                .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                                ).apply(lambda x: f"{x:.2f}")
    df["Current Payment Due"] = pd.to_numeric(df["Current Payment Due"]
                                              .str.replace(r'[$,]', '', regex=True)
                                              .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                              ).apply(lambda x: f"{x:.2f}")
    df["Total Amount Due"] = pd.to_numeric(df["Total Amount Due"]
                                           .str.replace(r'[$,]', '', regex=True)
                                           .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                           ).apply(lambda x: f"{x:.2f}")
    df["Payment Due Date"] = pd.to_datetime(df["Payment Due Date"], format='%m/%d/%Y')
    df["Regular Payment Amount"] = pd.to_numeric(df["Regular Payment Amount"]
                                                 .str.replace(r'[$,]', '', regex=True)
                                                 .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                                 ).apply(lambda x: f"{x:.2f}")
    df["Last Transaction Amount"] = pd.to_numeric(df["Last Transaction Amount"]
                                                  .str.replace(r'[$,]', '', regex=True)
                                                  .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                                  ).apply(lambda x: f"{x:.2f}")
    df["Date of Last Transaction"] = pd.to_datetime(df["Date of Last Transaction"], format='%m/%d/%Y')
    df["Monthly Payments Made"] = pd.to_numeric(df["Monthly Payments Made"])
    df["Maturity Date"] = pd.to_datetime(df["Maturity Date"], format='%m/%d/%Y')
    df["Outstanding Balance"] = pd.to_numeric(df["Outstanding Balance"]
                                              .str.replace(r'[$,]', '', regex=True)
                                              .str.replace(r'^(.*)-$', r'-\1', regex=True)
                                              ).apply(lambda x: f"{x:.2f}")
    return df
