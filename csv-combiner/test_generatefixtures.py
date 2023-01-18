#!/usr/bin/env python3

"""
Copy of generatefixtures.py for csv-combiner unit testing
"""

import csv
import hashlib
import os.path as path
import random

DIR = path.abspath(path.dirname(__file__))
FILES = {
    'clothing.csv': ('Blouses', 'Shirts', 'Tanks', 'Cardigans', 'Pants', 'Capris', '"Gingham" Shorts',),
    'accessories.csv': ('Watches', 'Wallets', 'Purses', 'Satchels',),
    'household_cleaners.csv': ('Kitchen Cleaner', 'Bathroom Cleaner',),
}

LARGE_FILE_CLOTHING = {
    'gt_2gb_clothing.csv': ('Blouses', 'Shirts', 'Tanks', 'Cardigans', 'Pants', 'Capris', '"Gingham" Shorts',),
}
LARGE_FILE_ACCESSORIES = {
    'gt_2gb_accessories.csv': ('Watches', 'Wallets', 'Purses', 'Satchels',),
}


def write_file(writer, length, categories):
    writer.writerow(['email_hash', 'category'])
    for i in range(0, length):
        writer.writerow([
            hashlib.sha256('tech+test{}@pmg.com'.format(i).encode('utf-8')).hexdigest(),
            random.choice(categories),
        ])


def write_large_file(writer, length, categories):
    """
    Modification of write_file() to produce CSV file >= 2GB
    """
    writer.writerow(['email_hash', 'Clothing', 'Accessories'])
    for i in range(0, length):
        writer.writerow([
            hashlib.sha256('tech+test{}@pmg.com'.format(i).encode('utf-8')).hexdigest(),
            random.choice(categories),
        ])


def main():
    for fn, categories in FILES.items():
        with open(path.join(DIR, 'fixtures', fn), 'w', encoding='utf-8') as fh:
            write_file(
                csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL),
                10,
                categories
            )

    # # Generate Large Clothing File
    # for fn, categories in LARGE_FILE_CLOTHING.items():
    #     with open(path.join(DIR, 'fixtures', fn), 'w', encoding='utf-8') as fh:
    #         write_file(
    #             csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL),
    #             30000000,
    #             categories
    #         )

    # # Generate Large Accessories File
    # for fn, categories in LARGE_FILE_ACCESSORIES.items():
    #     with open(path.join(DIR, 'fixtures', fn), 'w', encoding='utf-8') as fh:
    #         write_file(
    #             csv.writer(fh, doublequote=False, escapechar='\\', quoting=csv.QUOTE_ALL),
    #             30000000,
    #             categories
    #         )


if __name__ == '__main__':
    main()