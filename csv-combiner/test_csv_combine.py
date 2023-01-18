from csv_combine import *
import filecmp
import os.path as path

##Unit test for simple merge with 2 inputs
##Combining accessories.csv and clothing.csv
def merge_simple():
    # combine_csvs()
    return filecmp.cmp("combined.csv", "fixtures\\expected_accessories_clothing.csv")

##Unit test for merge > 2 inputs
def merge_greater_than_two_inputs():
    return filecmp.cmp("combined.csv", "fixtures\\expected_accessories_clothing_household.csv")

##Unit test merge for inputs with different columns
def merge_diff_columns():
    return filecmp.cmp("combined.csv", "fixtures\\diff_col_household_cleaners.csv")

##Unit test for files >2GB
def merge_large_files():
    """
    If above 3 tests pass, and no exception thrown
    during execution this test passes (No file comparision due to size)
    """
    assert merge_simple()
    assert merge_greater_than_two_inputs()
    assert merge_large_files()
    assert combine_csvs()

def test_merge_simple():
    assert merge_simple() == True

def test_merge_greater_than_two_inputs():
    assert merge_greater_than_two_inputs() == True

def test_merge_diff_columns():
    assert merge_diff_columns() == True

def test_merge_large_files():
    assert merge_large_files() == True
