from tkinter import *
#import mariadb
import sys


# def database_connection():
  # try:
  #   connection = mariadb.connect(
  #     user="mdmfvz",
  #     password="my2BOYZ!",
  #     host="cs-class-db.srv.mst.edu",
  #     port=3306,
  #     database="mdmfvz"
  #   )

  # except mariadb.Error as e:
  #   print(f"Error connecting to MariaDB Platform: {e}")
  #   sys.exit(1)

  # return connection

#conn = database_connection()
#curr = conn.cursor()

#curr.execute(SQL_statement)
#conn.commit()
#conn.close()


#tkinter setup

#window setup
root = Tk()
root.geometry("1280x720")
frame = Frame(root)

#grid setup. row 0 is label, 1 is dropdown, 2 is conditional input field + checkboxes, 3 is table return
#column 1 to center your cell
frame.grid(row=0, column=0, sticky="NESW")
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=2)
frame.grid_rowconfigure(3, weight=10)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#Title Creation
title = Label(frame, text="Database Querying Application", fg="black", font=("Arial", 25))
title.grid(row=0, column=1)

# Dropdown Bar Row

# Label for DD Query Selection
dd_label = Label(frame, text="Query by:", font=("Arial", 15))
dd_label.grid(row=1, column=1, sticky="N")

# Dropdown Bar Creation
drop_down_var = StringVar(frame)
drop_down_var.set('SELECT') # Set default text
dd_choices = ['Title', 'Author', 'Release Date', 'Binding', 'Grade', 'Language', 'Price']
drop_down = OptionMenu(frame, drop_down_var, *dd_choices)
drop_down.config(font=("Arial", 15))
drop_down.grid(row=1, column=1, sticky="S")

# inner_frame creation
inner_frame = Frame(frame)  # an inner frame consisting of rows 2 - 3, columns 0 - 2
inner_frame.grid(row = 2, rowspan = 2, column = 0, columnspan = 3, sticky = "NSEW")

# inner_frame row configuration
inner_frame.grid_rowconfigure(0, weight=10)   # row containing the conditional search field
inner_frame.grid_rowconfigure(1, weight=1)    # Title for output selection
inner_frame.grid_rowconfigure(2, weight=1)    # rows containing the checkboxes (5 row x 4 column grid)
inner_frame.grid_rowconfigure(3, weight=1)
inner_frame.grid_rowconfigure(4, weight=1)
inner_frame.grid_rowconfigure(5, weight=1)
inner_frame.grid_rowconfigure(6, weight=1)
inner_frame.grid_rowconfigure(7, weight=80)   # row containing the output

# inner_frame column configuration
inner_frame.grid_columnconfigure(0, weight=1) # columns containing the checkboxes (5 row x 4 column grid)
inner_frame.grid_columnconfigure(1, weight=1)
inner_frame.grid_columnconfigure(2, weight=1)
inner_frame.grid_columnconfigure(3, weight=1)

# checkbox variables for output selection
book_title = IntVar()
book_date = IntVar()
book_synopsis = IntVar()
book_origin = IntVar()
authors_name = IntVar()
authors_notes = IntVar()
conditions_binding = IntVar()
conditions_grade = IntVar()
other_price = IntVar()
other_publisher = IntVar()
other_language = IntVar()

# Button(inner_frame, text='Quit', command=inner_frame.quit).grid(row=6, sticky=W, pady=4)

query_str1 = StringVar()
query_str2 = StringVar()

def inner_frame_render(*args):
  # clear the inner_frame for the purpose of re-rendering everything based on drop_down above
  for widget in inner_frame.winfo_children():
    widget.destroy()

  # re-render inner_frame:
  # 1. conditional search method based on query_string
  # 2. checkboxes for output selection

  # grab query_string
  query_string = drop_down_var.get()

  # render certain widgets based on string
  if (query_string == "Title" or query_string == "Author"):   # String-based search
    # variable needed for search logic
    query_str1.set("Enter " + query_string.casefold() + " here")

    # search bar creation
    search = Entry(inner_frame, font=("Arial", 12), justify="center", textvariable=query_str1)
    search.grid(row = 0, column = 1, columnspan = 2)
  elif (query_string == "Release Date" or query_string == "Price"):   # Range-based search
    # depending on query_string, set default text
    if (query_string == "Release Date"):
      query_str1.set('1980')
      query_str2.set('1990')
    else:
      query_str1.set('10')
      query_str2.set('15')

    # search bar creation
    Label(inner_frame, text="to", font=("Arial", 12)).grid(row = 0, column = 1, columnspan = 2, sticky = "NSEW")
    lower = Entry(inner_frame, font=("Arial", 12), justify="center", textvariable=query_str1)
    lower.grid(row = 0, column = 0, columnspan = 2)
    upper = Entry(inner_frame, font=("Arial", 12), justify="center", textvariable=query_str2)
    upper.grid(row = 0, column = 2, columnspan = 2)
  else:   # Dropdown-based search
    # variable needed for search logic
    query_str1.set('SELECT')
    drop_down_list = []

    # depending on query_string, set drop_down_list
    if (query_string == "Binding"):
      drop_down_list = ['paperback', 'hardcover', 'cloth / hardboard', 'leather', 'magazine', 'soft cover', 'staple bound', 'unknown binding', 'wraps', 'no binding', 'no data']
    elif (query_string == "Grade"):
      drop_down_list = ['new', 'fine / like new', 'near fine', 'good', 'fair', 'poor', 'reading copy only', 'no data']
    else: # query_string == "Language"
      drop_down_list = ['Danish', 'Dutch', 'English', 'English', 'Finish', 'French', 'German', 'Hindi', "Italian", 'Japanese', 'Mandarin', 'Nepali', 'Polish', "Portuguese", 'Romanian', 'Russian', 'Spanish', 'Swedish', 'Turkish']
    
    # dropdown creation
    Label(inner_frame, text="Please select from\n the menu:", font=("Arial", 12)).grid(row = 0, column = 0, columnspan = 2)
    query_option = OptionMenu(inner_frame, query_str1, *drop_down_list)
    query_option.config(font=("Arial", 12))
    query_option.grid(row = 0, columnspan = 4)

  # Output selection title
  Label(inner_frame, text="Output Selection:", font=("Arial", 15)).grid(row=1, column=1, columnspan=2, sticky="N")

  # Section labels
  Label(inner_frame, text="Book:", font=("Arial", 12)).grid(row=2, column=0, sticky="W")
  Label(inner_frame, text="Author:", font=("Arial", 12)).grid(row=2, column=1, sticky="W")
  Label(inner_frame, text="Condition:", font=("Arial", 12)).grid(row=2, column=2, sticky="W")
  Label(inner_frame, text="Other:", font=("Arial", 12)).grid(row=2, column=3, sticky="W")

  # checkbuttons for output selection
  # BOOK SECTION
  title_check = Checkbutton(inner_frame, text="Title", font=("Arial", 10), variable=book_title)
  title_check.grid(row=3, column=0, sticky="W")
  title_check.select()  # select book_title by default

  date_check = Checkbutton(inner_frame, text="Date", font=("Arial", 10), variable=book_date)
  date_check.grid(row=4, column=0, sticky="W")

  synopsis_check = Checkbutton(inner_frame, text="Synopsis", font=("Arial", 10), variable=book_synopsis)
  synopsis_check.grid(row=5, column=0, sticky="W")

  origin_check = Checkbutton(inner_frame, text="Origin", font=("Arial", 10), variable=book_origin)
  origin_check.grid(row=6, column=0, sticky="W")

  # AUTHOR SECTION
  name_check = Checkbutton(inner_frame, text="Name", font=("Arial", 10), variable=authors_name)
  name_check.grid(row=3, column=1, sticky="W")
  name_check.select()   # select author_name by default

  notes_check = Checkbutton(inner_frame, text="Notes", font=("Arial", 10), variable=authors_notes)
  notes_check.grid(row=4, column=1, sticky="W")

  # CONDITION SECTION
  binding_check = Checkbutton(inner_frame, text="Binding", font=("Arial", 10), variable=conditions_binding)
  binding_check.grid(row=3, column=2, sticky="W")

  grade_check = Checkbutton(inner_frame, text="Grade", font=("Arial", 10), variable=conditions_grade)
  grade_check.grid(row=4, column=2, sticky="W")

  # OTHER SECTION
  price_check = Checkbutton(inner_frame, text="Price", font=("Arial", 10), variable=other_price)
  price_check.grid(row=3, column=3, sticky="W")

  publisher_check = Checkbutton(inner_frame, text="Publisher", font=("Arial", 10), variable=other_publisher)
  publisher_check.grid(row=4, column=3, sticky="W")

  language_check = Checkbutton(inner_frame, text="Language", font=("Arial", 10), variable=other_language)
  language_check.grid(row=5, column=3, sticky="W")
  
  # search button that executes querying logic
  Button(inner_frame, text='Search', command=search_button_logic).grid(row=4, column=3)

#         Book                  Authors       Conditions           Other
# Title Date Synopsis Origin | Name Notes | Binding Grade | Price Publisher Language
# 0     0    0        0        0    0       0       0       0     0         0
# 11 bits
# Example: 00001100000, then they want name and notes

def search_button_logic():
  # dict of <table name, inclusion flag>. if value is 0, not included in query. included if 1. default to 0
  flags = {'Books' : 0, 'Publications' : 0, 'Authors' : 0, 'Quality' : 0, 'Prices' : 0, 'Publishers' : 0, 'Languages' : 0}

  bin_str = getOutput()         # checkboxes
  book_str = bin_str[0:4]       # corresponding to Books table
  auth_str = bin_str[4:6]       # corresponding to Authors table
  qua_str = bin_str[6:8]        # corresponding to Quality table
  query_str = 'SELECT '         # SQL string to generate for usage in DB
  query_type_str = ''           # for checking actual query
  results_list = []             # container of columns to return for SELECT clause
  tables_list = []              # container of tables to query on for FROM clause
  where_list = []               # container of conditionals for WHERE clause
  
  # include table corresponding to query selection
  dd_var = drop_down_var.get()
  # query by book title, searches by substring
  if dd_var == 'Title':
    flags['Books'] = 1

    if 'mdmfvz.Books b' not in tables_list:
      tables_list.append('mdmfvz.Books b')
    
    query_type_str += 'b.Title LIKE \'%'
    query_type_str += query_str1.get()
    query_type_str += '%\''
    where_list.append(query_type_str)
  # query by release year
  elif dd_var == 'Release Date':
    flags['Books'] = 1

    if 'mdmfvz.Books b' not in tables_list:
      tables_list.append('mdmfvz.Books b')
    
    # equal but neither empty OR second is empty, use single value
    if (query_str1.get() == query_str2.get() and query_str1.get() != '' and query_str2.get() != '') or (query_str1.get() != '' and query_str2.get() == ''):
      query_type_str += 'b.Date = '
      query_type_str += query_str1.get()
      where_list.append(query_type_str)
    # first is empty, use single value
    elif query_str1.get() == '' and query_str2.get() != '':
      query_type_str += 'b.Date = '
      query_type_str += query_str2.get()
      where_list.append(query_type_str)
    # both empty, default to 0 (should return nothing from the db)
    elif query_str1.get() == '' and query_str2.get() == '':
      query_type_str += 'b.Date = 0'
      where_list.append(query_type_str)
    # neither empty
    else:
      query_type_str += 'b.Date > '
      query_type_str += query_str1.get()
      query_type_str += '\n\tAND b.Date < '
      query_type_str += query_str2.get()
      where_list.append(query_type_str)
  # query by author name/names, searches by substring
  elif dd_var == 'Author':
    flags['Authors'] = 1

    if 'mdmfvz.Authors a' not in tables_list:
      tables_list.append('mdmfvz.Authors a')
    
    query_type_str += 'a.Name LIKE \'%'
    query_type_str += query_str1.get()
    query_type_str += '%\''
    where_list.append(query_type_str)
  # query by type of binding of the book
  elif dd_var == 'Binding':
    flags['Quality'] = 1

    if 'mdmfvz.Quality q' not in tables_list:
      tables_list.append('mdmfvz.Quality q')
    
    query_type_str += 'q.Binding = \''
    query_type_str += query_str1.get()
    query_type_str += '\''
    where_list.append(query_type_str)
  # query by the condition the book is in
  elif dd_var == 'Grade':
    flags['Quality'] = 1

    if 'mdmfvz.Quality q' not in tables_list:
      tables_list.append('mdmfvz.Quality q')
    
    query_type_str += 'q.Grade = \''
    query_type_str += query_str1.get()
    query_type_str += '\''
    where_list.append(query_type_str)
  # query by language of the book, one at a time
  elif dd_var == 'Language':
    flags['Languages'] = 1

    if 'mdmfvz.Languages L' not in tables_list:
      tables_list.append('mdmfvz.Languages L')
    
    query_type_str += 'L.Language = \''
    query_type_str += query_str1.get()
    query_type_str += '\''
    where_list.append(query_type_str)
  # query by book price
  elif dd_var == 'Price':
    flags['Prices'] = 1

    if 'mdmfvz.Prices pr' not in tables_list:
      tables_list.append('mdmfvz.Prices pr')
    
    # equal but neither empty OR second is empty, use single value
    if (query_str1.get() == query_str2.get() and query_str1.get() != '' and query_str2.get() != '') or (query_str1.get() != '' and query_str2.get() == ''):
      query_type_str += 'pr.Price = '
      query_type_str += query_str1.get()
      where_list.append(query_type_str)
    # first is empty, use single value
    elif query_str1.get() == '' and query_str2.get() != '':
      query_type_str += 'pr.Price = '
      query_type_str += query_str2.get()
      where_list.append(query_type_str)
    # both empty, default to 0 (should return nothing from the db)
    elif query_str1.get() == '' and query_str2.get() == '':
      query_type_str += 'pr.Price = 0'
      where_list.append(query_type_str)
    # neither empty
    else:
      query_type_str += 'pr.Price > '
      query_type_str += query_str1.get()
      query_type_str += '\n\tAND pr.Price < '
      query_type_str += query_str2.get()
      where_list.append(query_type_str)
  
  # check each bit in binary string to determine which results to include
  # if the corresponding table is not already greenlit, greenlight it
  
  # Book

  # "Title" checked
  if bin_str[0] == '1':
    flags['Books'] = 1
    results_list.append('b.Title')

    if 'mdmfvz.Books b' not in tables_list:
      tables_list.append('mdmfvz.Books b')
  
  # "Date" checked
  if bin_str[1] == '1':
    flags['Books'] = 1
    results_list.append('b.Date')

    if 'mdmfvz.Books b' not in tables_list:
      tables_list.append('mdmfvz.Books b')
  
  # "Synopsis" checked
  if bin_str[2] == '1':
    flags['Books'] = 1
    results_list.append('b.Synopsis')

    if 'mdmfvz.Books b' not in tables_list:
      tables_list.append('mdmfvz.Books b')

  # "Origin" checked
  if bin_str[3] == '1':
    flags['Books'] = 1
    results_list.append('b.Location_of_Origin')

    if 'mdmfvz.Books b' not in tables_list:
      tables_list.append('mdmfvz.Books b')

  # Author

  # "Name" checked
  if bin_str[4] == '1':
    flags['Authors'] = 1
    results_list.append('a.Name')

    if 'mdmfvz.Authors a' not in tables_list:
      tables_list.append('mdmfvz.Authors a')

  # "Notes" checked
  if bin_str[5] == '1':
    flags['Authors'] = 1
    results_list.append('a.Notes')
    
    if 'mdmfvz.Authors a' not in tables_list:
      tables_list.append('mdmfvz.Authors a')

  # Condition

  # "Binding" checked
  if bin_str[6] == '1':
    flags['Quality'] = 1
    results_list.append('q.Binding')

    if 'mdmfvz.Quality q' not in tables_list:
      tables_list.append('mdmfvz.Quality q')
  
  # "Grade" checked
  if bin_str[7] == '1':
    flags['Quality'] = 1
    results_list.append('q.Grade')

    if 'mdmfvz.Quality q' not in tables_list:
      tables_list.append('mdmfvz.Quality q')

  # Other

  # "Price" checked
  if bin_str[8] == '1':
    flags['Prices'] = 1
    results_list.append('pr.Price')

    if 'mdmfvz.Prices pr' not in tables_list:
      tables_list.append('mdmfvz.Prices pr')
  
  # "Publisher" checked
  if bin_str[9] == '1':
    flags['Publishers'] = 1
    results_list.append('pu.Publisher')

    if 'mdmfvz.Publishers pu' not in tables_list:
      tables_list.append('mdmfvz.Publishers pu')
  
  # "Language" checked
  if bin_str[10] == '1':
    flags['Languages'] = 1
    results_list.append('L.Language')

    if 'mdmfvz.Languages L' not in tables_list:
      tables_list.append('mdmfvz.Languages L')
  
  # if Authors table and any other table are greenlit, greenlight Publications
  if flags['Authors'] and (flags['Books'] or flags['Quality'] or flags['Prices'] or flags['Publishers'] or flags['Languages']):
    flags['Publications'] = 1
    tables_list.append('mdmfvz.Publications pn')
    where_list.append('b.ID = pn.Book_ID')
    where_list.append('a.ID = pn.Author_ID')
  
  # check possible joins
  if flags['Books'] and flags['Quality']:
    where_list.append('b.ID = q.Book_ID')
  
  if flags['Books'] and flags['Prices']:
    where_list.append('b.ID = pr.Book_ID')
  
  if flags['Books'] and flags['Publishers']:
    where_list.append('b.ID = pu.Book_ID')

  if flags['Books'] and flags['Languages']:
    where_list.append('b.ID = L.Book_ID')
  
  # SELECT clause
  for i in range(0,len(results_list)):
    query_str += results_list[i]

    if i < (len(results_list) - 1):
      query_str += ', '
  
  # FROM clause
  query_str += '\nFROM '
  for i in range(0,len(tables_list)):
    query_str += tables_list[i]

    if i < (len(tables_list) - 1):
      query_str += ', '
  
  # WHERE clause
  query_str += '\nWHERE '
  for i in range(0,len(where_list)):
    query_str += where_list[i]

    if i < (len(where_list) - 1):
      query_str += '\n\tAND '

# Get string from checkboxes
def getOutput():
  output_string = str(book_title.get()) + str(book_date.get()) + str(book_synopsis.get()) + str(book_origin.get()) + str(authors_name.get()) + str(authors_notes.get()) + str(conditions_binding.get()) + str(conditions_grade.get()) + str(other_price.get()) + str(other_publisher.get()) + str(other_language.get())
  return output_string






# Trace the drop down menu for changes, call inner_frame render when changed
drop_down_var.trace("w", inner_frame_render)

root.mainloop()