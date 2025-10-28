import pandas as pd



def load_to_csv(df, file_path): 
    df.to_csv(file_path, index=False) 

def load_to_csv_indexed(df, file_path): 
    df.to_csv(file_path) 
    