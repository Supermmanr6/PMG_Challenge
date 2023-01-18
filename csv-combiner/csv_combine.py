import os
import pandas as pd
import sys
import csv

DIR = os.path.abspath(os.path.dirname(__file__))
CSV_DIR = os.path.join(DIR, 'fixtures')
CHUNK_SIZE = 50

# def combine_csvs();

# def check_args():

def main(*argv):
    print("DIR: " + DIR)
    print("CSV_DIR: " + CSV_DIR)
    
    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))

    header_flag = True


    # First determine the field names from the top line of each input file
    fieldnames = []
    for filename in sys.argv[1:]:
        with open(filename, "r", newline="") as f_in:
            reader = csv.reader(f_in)
            headers = next(reader)
            for h in headers:
                if h not in fieldnames:
                    fieldnames.append(h)
    
    print("fieldnames:")
    print(fieldnames)


    # inputs = sys.argv[1:]
    # print("=====")
    # print(inputs)
    # print("=====")
    # fieldnames = []
    # for filename in inputs:
    #     with open(filename, "r", newline="") as f_in:
    #         reader = csv.reader(f_in)
    #         headers = next(reader)
    #         for h in headers:
    #             if h not in fieldnames:
    #                 fieldnames.append(h)
    # print("=====")
    # print(fieldnames)
    # print("=====")

    # Creating a list of files
    for csv_file in sys.argv[1:]:
        print("current arg in csv_file: " + csv_file)
        print("current CSV file: " + os.path.basename(csv_file))
        if not header_flag:
            skip_row = [0]
        else:
            skip_row = None
        df = pd.read_csv(csv_file, chunksize=CHUNK_SIZE, skiprows=skip_row)
        header_flag = False
        for chunk in df:
            # chunk.insert(column="filename", value=os.path.basename(csv_file))
            chunk.loc[:, "filename"] = os.path.basename(csv_file)
            chunk.to_csv("temp.csv", mode='a', header=False, index=False)
        # header_flag = False
        # chunk_container = pd.read_csv(csv_file, chunksize=CHUNK_SIZE)
        # for chunk in chunk_container:
        #     x = chunk.to_csv("combined.csv", mode="a")

    # Output csv to stdout
    with open("temp.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            print(",".join(row))
    

    # for file in CSV_DIR.items()

if __name__ == '__main__':
    main(sys.argv)
