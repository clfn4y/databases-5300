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
inner_frame.grid_rowconfigure(7, weight=1)    # Search Button
inner_frame.grid_rowconfigure(8, weight=80)   # row containing the output

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
    search_string = StringVar()
    search_string.set("Enter " + query_string.casefold() + " here")

    # search bar creation
    search = Entry(inner_frame, font=("Arial", 12), justify="center", textvariable=search_string)
    search.grid(row = 0, column = 1, columnspan = 2)
  elif (query_string == "Release Date" or query_string == "Price"):   # Range-based search
    # variables needed for search logic
    lower_bound = StringVar()
    upper_bound = StringVar()

    # depending on query_string, set default text
    if (query_string == "Release Date"):
      lower_bound.set('1980')
      upper_bound.set('1990')
    else:
      lower_bound.set('10')
      upper_bound.set('15')

    # search bar creation
    Label(inner_frame, text="to", font=("Arial", 12)).grid(row = 0, column = 1, columnspan = 2, sticky = "NSEW")
    lower = Entry(inner_frame, font=("Arial", 12), justify="center", textvariable=lower_bound)
    lower.grid(row = 0, column = 0, columnspan = 2)
    upper = Entry(inner_frame, font=("Arial", 12), justify="center", textvariable=upper_bound)
    upper.grid(row = 0, column = 2, columnspan = 2)
  else:   # Dropdown-based search
    # variable needed for search logic
    query_selection = StringVar()
    query_selection.set('SELECT')
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
    query_option = OptionMenu(inner_frame, query_selection, *drop_down_list)
    query_option.config(font=("Arial", 12))
    query_option.grid(row = 0, columnspan = 4)

  # Output selection title
  Label(inner_frame, text="Output Selection:", font=("Arial", 15)).grid(row=1, column=1, columnspan=2, sticky="N")

  # Section labels
  Label(inner_frame, text="Book:", font=("Arial", 12)).grid(row=2, column=0)
  Label(inner_frame, text="Author:", font=("Arial", 12)).grid(row=2, column=1)
  Label(inner_frame, text="Condition:", font=("Arial", 12)).grid(row=2, column=2)
  Label(inner_frame, text="Other:", font=("Arial", 12)).grid(row=2, column=3)

  # checkbuttons for output selection
  # BOOK SECTION
  title_check = Checkbutton(inner_frame, text="Title", font=("Arial", 10), variable=book_title)
  title_check.grid(row=3, column=0)
  title_check.select()  # select book_title by default

  date_check = Checkbutton(inner_frame, text="Date", font=("Arial", 10), variable=book_date)
  date_check.grid(row=4, column=0)

  synopsis_check = Checkbutton(inner_frame, text="Synopsis", font=("Arial", 10), variable=book_synopsis)
  synopsis_check.grid(row=5, column=0)

  origin_check = Checkbutton(inner_frame, text="Origin", font=("Arial", 10), variable=book_origin)
  origin_check.grid(row=6, column=0)

  # AUTHOR SECTION
  name_check = Checkbutton(inner_frame, text="Name", font=("Arial", 10), variable=authors_name)
  name_check.grid(row=3, column=1)
  name_check.select()   # select author_name by default

  notes_check = Checkbutton(inner_frame, text="Notes", font=("Arial", 10), variable=authors_notes)
  notes_check.grid(row=4, column=1)

  # CONDITION SECTION
  binding_check = Checkbutton(inner_frame, text="Binding", font=("Arial", 10), variable=conditions_binding)
  binding_check.grid(row=3, column=2)

  grade_check = Checkbutton(inner_frame, text="Grade", font=("Arial", 10), variable=conditions_grade)
  grade_check.grid(row=4, column=2)

  # OTHER SECTION
  price_check = Checkbutton(inner_frame, text="Price", font=("Arial", 10), variable=other_price)
  price_check.grid(row=3, column=3)

  publisher_check = Checkbutton(inner_frame, text="Publisher", font=("Arial", 10), variable=other_publisher)
  publisher_check.grid(row=4, column=3)

  language_check = Checkbutton(inner_frame, text="Language", font=("Arial", 10), variable=other_language)
  language_check.grid(row=5, column=3)
  
  # search button that executes querying logic
  Button(inner_frame, text='Search', command=search_button_logic).grid(row=7, column=1, sticky="N",columnspan=2)

#         Book                  Authors       Conditions           Other
# Title Date Synopsis Origin | Name Notes | Binding Grade | Price Publisher Language
# 0     0    0        0        0    0       0       0       0     0         0
# 11 bits
# Example: 00001100000, then they want name and notes

def search_button_logic():
  print (getOutput())

# Get string from checkboxes
def getOutput():
  output_string = str(book_title.get()) + str(book_date.get()) + str(book_synopsis.get()) + str(book_origin.get()) + str(authors_name.get()) + str(authors_notes.get()) + str(conditions_binding.get()) + str(conditions_grade.get()) + str(other_price.get()) + str(other_publisher.get()) + str(other_language.get())
  return output_string






# Trace the drop down menu for changes, call inner_frame render when changed
drop_down_var.trace("w", inner_frame_render)

root.mainloop()