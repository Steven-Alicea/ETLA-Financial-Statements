import pandas as pd



def extract_from_csv(csv_file): 
    return pd.read_csv(csv_file) 

def extract_from_csv_without_header(csv_file):
    return pd.read_csv(csv_file, header=None)
