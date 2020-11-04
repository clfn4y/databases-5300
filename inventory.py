#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Jack Dixon III

import os
import sys
import numpy
import pandas

# inventory.csv attributes:

#             book   title  author binding  pubdate publisher  isbn10   isbn13
# data_type  int64  object  object  object  float64    object  object  float64
# has_null   False    True   False    True     True      True    True     True

#            condition dustjacket  signed edition   price   descr synopsis
# data_type     object     object  object  object  object  object   object
# has_null        True       True    True    True    True    True     True

#            about_auth
# data_type      object
# has_null         True




# TODO: figure out what is going on with location

# TODO: logic for insering authors
# TODO: logic for insering publishers
# TODO: logic for insering quality
# TODO: logic for insering prices
# TODO: logic for insering publications

# I think sanitization can be handled by the MariaDB module if that is
# used to send SQL commands to the database directly instead of saving
# statment as a string first!




def generate_SQL(data):
    statements = [] # List
    # Remember publishers with this set
    publishers = {} # Set
    # Remember authors with this set
    authors = {} # Set
    author_id = 0
    for row in data.itertuples():
        author_id += 1

        statements += insert_books(row)
        statements += insert_publishers(row, publishers, author_id)
        statements += insert_quality(row)
        statements += insert_languages(row)
        statements += insert_authors(row, authors, author_id)

    return statements





def insert_books(row):
    book_id = row.book
    title = '"' + row.title + '"' if isinstance(row.title, str) else 'NULL'
    release_date = row.pubdate if not numpy.isnan(row.pubdate) else 'NULL'
    location = '"???"'

    return [f"INSERT INTO Books (Book_ID, Title, Release_Date, Location)" \
                 f" VALUES ({book_id}, {title}, {release_date}, " \
                 f"{location});"]
    

def insert_publishers(row, publishers, author_id):
    book_id = row.book
    publisher = '"' + row.publisher + '"' if isinstance(row.publisher, str) else 'NULL'

    return [f"INSERT INTO Publishers (Book_ID, Publisher)" \
                f" VALUES ({book_id}, {publisher});"]

def insert_quality(row):
    return []

def insert_languages(row):
    return []

def insert_authors(row, authors, author_id):
    return []

# Loads a CSV file
# Returns a Pandas dataframe and a table of information about each column
def load_csv(filename, encoding = 'utf_8'):
    data = pandas.read_csv(
        encoding = encoding,
        filepath_or_buffer = filename,
        sep = ','
    )
    table = pandas.DataFrame(
        columns = data.columns,
        data = (
            # Data types
            tuple(data.dtypes),
            # Detection of null values
            [data[column].isnull().values.any() for column in data.columns]
        ),
        index = ('data_type', 'has_null')
    )
    return data, table

def main(args):
    print('START')
    if not os.path.exists('inventory.csv'):
        print('"inverntory.csv" is missing')
        exit(1)
    data, table = load_csv('inventory.csv', 'cp1252')
    print(table, end = '\n\n')
    statements = generate_SQL(data)
    with open(encoding = 'utf-8', file = 'output.txt', mode = 'w') as f:
        for i in statements:
            f.write(i + '\n')
    print('END OF LINE')
    return

if __name__ == '__main__': main(sys.argv)
