import os
import pandas as pd
import sys

CHUNK_SIZE = 50000


def combine_csvs():
    """
    Takes in multiple CSV arguments, combines the CSVs into one 
    outputting the results into a a new CSV file to stdout
    Author: Abishek Kannan
    """
    df_list = []

    for csv_file in sys.argv[1:]:
        # Read CSV by chunks to handle memory issues
        df = pd.read_csv(csv_file, chunksize=CHUNK_SIZE)
        df = pd.concat(df, ignore_index=True)
        df.loc[:, "filename"] = os.path.basename(csv_file)
        df_list.append(df)

    # Merging all dataframes
    combined_dfs = pd.concat(df_list)

    # Converting merged dataframe with CSV data back to CSV form
    print(combined_dfs.to_csv(index=False))

def main(*argv):
    combine_csvs()

if __name__ == '__main__':
    main(sys.argv)
