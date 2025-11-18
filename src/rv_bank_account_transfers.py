import pandas as pd
from src.analysis.get_csv_dataframes import *
from src.analysis.get_csv_report_dataframe import *
from src.analysis.analyze import *
from src.analysis.analyze_chime import *
from src.analysis.analyze_nfcu import *
from src.analysis.report_analysis_totals import *
from src.analysis.transfers_visualization import *
from src.personal_identifying_information import *



df_chime_checking = get_chime_checking_transactions()
df_nfcu_checking = get_nfcu_checking_transactions()
df_nfcu_savings = get_nfcu_savings_transactions()


def report_and_visualize_bank_account_transfers():
    transaction_dataframe_dict = {f"Chime Checking Transfers From {source_1} Totals": get_chime_checking_account_transfers(df_chime_checking, "from", source_1),
                                  f"Chime Checking Transfers To {destination_1} Totals": get_chime_checking_account_transfers(df_chime_checking, "to", destination_1),
                                  f"NFCU Checking Transfers From {source_1} Totals": get_nfcu_transfers(df_nfcu_checking, "from", source_1),
                                  f"NFCU Checking Transfers To {destination_1} Totals": get_nfcu_transfers(df_nfcu_checking, "to", destination_1),
                                  f"NFCU Saving Transfers From {source_1} Totals": get_nfcu_transfers(df_nfcu_savings, "from", source_1),
                                  f"NFCU Saving Transfers To {destination_1} Totals": get_nfcu_transfers(df_nfcu_savings, "to", destination_1),
                                  f"NFCU Zelle Transfers From {source_2} Totals": get_nfcu_zelle_transfers(df_nfcu_checking, "from", source_2)}
    
    for key in transaction_dataframe_dict:
        account = ' '.join(key.split()[:2]).replace("Zelle", "Checking")
        transaction = ' '.join(key.split()[3:5])
        generate_totals_csv_report(transaction_dataframe_dict.get(key), key)
        transaction_dataframe_dict[key] = get_csv_report(f"{key}.csv")
        transaction_dataframe_dict[key] = transaction_dataframe_dict.get(key).assign(Account=account, Transaction=transaction)
        
    df = pd.concat(list(transaction_dataframe_dict.values()), ignore_index=True)

    # visualiztion (account x amount x transaction)
    generate_transfers_visualization(df, "Bank Account Transfers (Account x Amount)", "Account", "Amount", "Transaction")

    # visualiztion (transaction x account x amount)
    generate_transfers_visualization(df, "Bank Account Transfers (Transaction x Amount)", "Transaction", "Amount", "Account")

    # visualization (transaction x amount)
    generate_transfers_visualization(df, "Bank Account Transfers", "Transaction", "Amount")


def main():
    report_and_visualize_bank_account_transfers()


if __name__ == '__main__':
    main()
