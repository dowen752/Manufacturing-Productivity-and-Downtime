import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    file_path = os.path.join('data', 'Manufacturing_Line_Productivity.xlsx')
    df_LP = pd.read_excel(file_path, sheet_name='Line productivity')
    df_Products = pd.read_excel(file_path, sheet_name='Products')
    df_LD = pd.read_excel(file_path, sheet_name='Line downtime')
    df_DF = pd.read_excel(file_path, sheet_name='Downtime factors')
    print(df_LP.head())
    print(df_LP.info())
    print(df_LP.describe())
    print(df_LP["Date"][0:5])
    
    
if __name__ == "__main__":
    main()