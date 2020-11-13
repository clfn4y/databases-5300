#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Jack Dixon III

import os
import re
import sys
import numpy
import pandas
import mariadb
from isbnlib import info, is_isbn13

import collections

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

# I think sanitization can be handled by the MariaDB module if that is
# used to send SQL commands to the database directly instead of saving
# statment as a string first!

def generate_SQL(data):
    statements = [] # List
    # Remember publishers with this set
    publishers = {} # Set
    # Remember authors with this set
    authors = dict()
    author_id = 0
    
    #Used for language table
    language_translate = []
    with open(encoding = 'utf-8', file = 'locations.txt', mode = 'r') as f:
        for line in f:          
            language_translate.append(line.rstrip())
    
    clean_authors, table = load_csv('clean_authors.csv')
    
    for row in data.itertuples():
        
        author_id += 1
        rtn_str, location = insert_languages(row, language_translate)
        statements += insert_books(row, location)
        statements += insert_publishers(row, publishers)
        statements += insert_quality(row)
        statements += rtn_str
        statements += insert_authors(row, authors, author_id, clean_authors)
        statements += insert_price(row)
    
    return statements

def insert_books(row, location):
    book_id = row.book
    title = '"' + row.title.replace('\"', "'") + '"' if isinstance(row.title, str) else '"' + 'None' '"'
    if len(title) > 254 : title = title[:254] + '\"' 
    release_date = int(row.pubdate) if not numpy.isnan(row.pubdate) else 'NULL'
    
    return [f"INSERT INTO Books (Book_ID, Title, Release_Date, Location)" \
                 f" VALUES ({book_id}, {title}, {release_date}, " \
                 f"{location});"]

def insert_publishers(row, publishers):
    book_id = row.book
    publisher = '"' + row.publisher.replace('\"', "'") + '"' if isinstance(row.publisher, str) else 'NULL'
    
    if (publisher == 'NA'.casefold() or publisher == 'None'.casefold()):
        publisher = 'NULL'
    
    return [f"INSERT INTO Publishers (Book_ID, Publisher)" \
                f" VALUES ({book_id}, {publisher});"]

def insert_quality(row):
    # get parameters
    book_id = row.book
    binding = '"' + row.binding + '"' if isinstance(row.binding, str) else 'NULL'
    grade = '"' + row.condition + '"' if isinstance(row.condition, str) else 'NULL'
    
    # make everything lower
    binding = binding.lower()
    grade = grade.lower()
    
    # get rid of junk
    if "-" in binding:
        binding = binding.replace("-", " ")
    if "." in binding:
        binding = binding.replace(".", "")
    if "-" in grade:
        grade = grade.replace("-", " ")
    if "." in grade:
        grade = grade.replace(".", "")
    
    # Binding: paperback, hardcover, cloth / hardboard, leather, magazine, no binding, no data, soft cover, staple bound, unknown binding, wraps
    if "paperback" in binding or "paper back" in binding or "market" in binding:
        binding = "\"paperback\""
    elif "cloth" in binding:
        binding = "\"cloth / hardboard\""
    elif "hardcover" in binding or "hc" in binding or "hard" in binding:
        binding = "\"hardcover\""
    elif "unknown" in binding or "book" in binding:
        binding = "\"unknown binding\""
    elif "soft" in binding:
        binding = "\"soft cover\""
    elif "staple" in binding:
        binding = "\"staple bound\""
    elif "leather" in binding:
        binding = "\"leather\""
    elif "textbook" in binding or "school" in binding or "tb" in binding:
        binding = "\"hardcover\""
    elif "wrap" in binding:
        binding = "\"wraps\""
    elif "magazine" in binding:
        binding = "\"magazine\""
    elif "no binding" in binding or "unbound" in binding or "broch" in binding:
        binding = "\"no binding\""
    elif "null" == binding:
        binding = "NULL"
    else:
        binding = "\"unknown binding\""
    
    # Grade: new, fine / like new, near fine, good, fair, poor, no data, reading copy only
    if "vg" in grade:
        grade = "\"fine / like new\""
    elif "very good" in grade:
        grade = "\"fine / like new\""
    elif "good" in grade:
        # grade = "\"good / bon / buone / bueno / buono / bien\""
        grade = "\"good\""
    elif "buone" in grade or "bon" in grade or "bueno" in grade or "buono" in grade or "bien" in grade:
        # grade = "\"good / bon / buone / bueno / buono / bien\""
        grade = "\"good\""
    elif "akzeptabel" in grade or "acceptable" in grade:
        # grade = "\"acceptable / akzeptabel\""
        grade = "\"good\""
    elif "befriedigend" in grade or "satisfactory" in grade or "satisfaisant" in grade or "ausreichend" in grade:
        # grade = "\"satisfactory / befriedigend / satisfaisant\""
        grade = "\"good\""
    elif "fair" in grade:
        grade = "\"fair\""
    elif "near fine" in grade or "nf" in grade:
        grade = "\"near fine\""
    elif "gut" in grade or "fine" in grade:
        grade = "\"fine / like new\""
    elif "like new" in grade or "likenew" in grade or "excellent" in grade:
        grade = "\"fine / like new\""
    elif "new" in grade or "neu" in grade or "nuevo" in grade:
        grade = "\"new\""
    elif "gebraucht" in grade or "used" in grade:
        grade = "\"good\""
    elif "reading copy" in grade:
        grade = "\"reading copy only\""
    elif "poor" in grade or "malo" in grade or "bad" in grade or "schlecht" in grade or "ancien" in grade:
        grade = "\"poor\""
    elif "null" == grade:
        grade = "NULL"
    else:
        grade = "\"good\""
    
    return [f"INSERT INTO Quality (Book_ID, Binding, Grade) VALUES ({book_id}, {binding}, {grade});"]

def insert_languages(row, ltol):
    alter = ["English", "German", "French", "U.S.S.R", "China"]
    
    isbn13 = str(row.isbn13)[:-2]
    book_id = row.book
    
    location = "United States"
    language = "English"
    
    if is_isbn13(isbn13):
        
        output = info(isbn13)   
        
        location = output
        
        for i in alter:
            if i in output:
                location = i
        
        for i in ltol:
            translate = i.split(",")
            if location == translate[0]:
                language = translate[1]
                if ltol.index(i) < 3:
                    language, location = location, language
                break
    
    location = "'" + location + "'"
    
    rt_str = [f"INSERT INTO Languages (Book_ID, Language)" \
                f" VALUES ({book_id}, '{language}');"]
    
    return rt_str, location

def clean_author(string):
    string = string.lower()
    if re.match('^.*\(.*;.*', string):
        string = re.sub('^.*\(', '', string)
        string = re.sub(';.*', '', string)
    if re.match('^[A-Za-z-]+( )+[A-Za-z-]+,.*', string):
        string = re.sub(',.*', '', string)
    replacements = (
        '( )*[\[(].*[\])].*',
        'sir ( )*',
        ';.*',
        '( )*- aka .*',
        '( )* and .*',
        '( )* et .*',
        '( )* & .*',
        '( )* -.*',
        ', etc .*',
        '[,:;\&-]$'
    )
    for i in replacements:
        string = re.sub(i, '', string)
    x = string.split(',')
    if 1 < len(x):
        string = ' '.join((x[1],) + (x[0],))
    string = re.sub('[ ][ ][ ]*', ' ', string)
    string = string.replace('"', '')
    string = string.title().strip()
    if string == "":
        string = "Default"
    return string

def insert_authors(row, authors, author_id, clean_authors):
    author = 'Default'
    if isinstance(row.binding, str):
        frame = clean_authors.loc[clean_authors['author'] == row.author]
        if frame.empty:
            author = clean_author(row.author)
        else:
            author = str(frame.iloc[0]['clean'])
    actual_id = 0
    result = []
    notes = ""
    if author not in authors:
        authors[author] = author_id
        actual_id = author_id
        if author != 'NULL': author = '\"' + author+ '\"'
        if not isinstance(row.about_auth, str):
            notes = 'NULL'
        else:
            if row.about_auth == 'NA':
                notes = 'NULL'
            else:
                notes = '"' + row.about_auth + '"'
        result += [f"INSERT INTO Authors (Author_ID, Name, Notes) VALUES " \
            f"({actual_id}, {author}, {notes})"]
    else:
        actual_id = authors[author]
    result += [f"INSERT INTO Publications (Author_ID, Book_ID) VALUES " \
            f"({actual_id}, {row.book})"]
    # print(f"result = {result}")
    return result

def insert_price(row):
    # grab book_id and initial price value
    book_id = row.book
    price_init = '"' + row.price + '"' if isinstance(row.price, str) else 'NULL'
    
    # modify price based on if it is NA or not
    if ("US$" in price_init):
        price = price_init.replace("US$ ", "")
    else:
        price = '0.00'
    
    price = price.replace(",","")
    
    return [f"INSERT INTO Prices (Book_ID, Price)" \
                f" VALUES ({book_id}, {price});"]

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
    
    try:
    	conn = mariadb.connect(
    		user="mdmfvz",
    		password="my2BOYZ!",
    		host="cs-class-db.srv.mst.edu",
    		port=3306,
    		database="mdmfvz"
    	)
    
    except mariadb.Error as e:
    	print(f"Error connecting to MariaDB Platform: {e}")
    	sys.exit(1)
    
    curr = conn.cursor()
    
    if not os.path.exists('inventory.csv'):
        print('"inverntory.csv" is missing')
        exit(1)
    
    data, table = load_csv('inventory.csv', 'cp1252')
    print(table, end = '\n\n')
    statements = generate_SQL(data)
    for i in statements:
        try:
            curr.execute(i)
        except mariadb.Error as e:
            print(i)
            print(f"Error: {e}")
    
    conn.commit()
    print('END OF LINE')
    conn.close()
    return

if __name__ == '__main__': main(sys.argv)

