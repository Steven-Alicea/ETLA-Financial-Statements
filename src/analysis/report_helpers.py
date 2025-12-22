import csv



def write_totals_to_csv(csv_file, count_total, amount_total):
    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([])
        writer.writerow(count_total)
        writer.writerow(amount_total)

def format_dataframe_for_totals_report(df, currency=None):
    if currency:
        # df.loc[:, "Amount"] = '$' + df["Amount"].astype("string")
        df.loc[:, "Amount"] = df["Amount"].apply(lambda x: f"${x:,.2f}")
    else:
        df = df[["Statement Period", "Transaction Date", "Description", "Amount"]]
        df.loc[:, "Amount"] = df["Amount"].abs()
        df = df.sort_values(by="Transaction Date", ascending=False)
    return df

def get_total_count(df):
    return [f"Total Transactions", len(df)]

def get_total_amount(df):
    return [f"Total Amount", "${:,.2f}".format(df["Amount"].sum())] 
