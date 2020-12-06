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
dd_choices = {'Title', 'Author', 'Release Date', 'Binding', 'Grade', 'Language', 'Price'}
drop_down = OptionMenu(frame, drop_down_var, *dd_choices)
drop_down.config(font=("Arial", 15))
drop_down.grid(row=1, column=1, sticky="S")

# TODO: Render rows 2 + 3 based on dd_choices.get()

inner_frame = Frame(frame)  # frame consisting of rows 2 - 3, columns 0 - 2
inner_frame.grid(row = 2, rowspan = 2, column = 0, columnspan = 3, sticky = "NSEW")

# inner_frame row configuration
inner_frame.grid_rowconfigure(0, weight=10)  # row containing the conditional search field
inner_frame.grid_rowconfigure(1, weight=1)   # Title for output selection
inner_frame.grid_rowconfigure(2, weight=1)   # rows containing the checkboxes (4x4 grid)
inner_frame.grid_rowconfigure(3, weight=1)
inner_frame.grid_rowconfigure(4, weight=1)
inner_frame.grid_rowconfigure(5, weight=1)
inner_frame.grid_rowconfigure(6, weight=1)
inner_frame.grid_rowconfigure(7, weight=1)   # Search Button
inner_frame.grid_rowconfigure(8, weight=80)

# inner_frame column configuration
inner_frame.grid_columnconfigure(0, weight=1) # columns containing the checkboxes (4x4 grid)
inner_frame.grid_columnconfigure(1, weight=1)
inner_frame.grid_columnconfigure(2, weight=1)
inner_frame.grid_columnconfigure(3, weight=1)

# TODO: Render table based on input/selections from rows 2 + 3 on row 4


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


# Output selection Title
# Label(inner_frame, text="Output Selection:").grid(row=1, sticky=N, column=0)
Label(inner_frame, text="Output Selection:", font=("Arial", 15)).grid(row=1, column=1, sticky="N",columnspan=2)

# Section labels
Label(inner_frame, text="Book:").grid(row=2, column=0)
Label(inner_frame, text="Authors:").grid(row=2, column=1)
Label(inner_frame, text="Conditions:").grid(row=2, column=2)
Label(inner_frame, text="Other:").grid(row=2, column=3)

# Variables and check button
book_title = IntVar()
title_check = Checkbutton(inner_frame, text="Title", variable=book_title)
title_check.grid(row=3, column=0)
title_check.select()
book_date = IntVar()
Checkbutton(inner_frame, text="Date", variable=book_date).grid(row=4, column=0)
book_synopsis = IntVar()
Checkbutton(inner_frame, text="Synopsis", variable=book_synopsis).grid(row=5, column=0)
book_origin = IntVar()
Checkbutton(inner_frame, text="Origin", variable=book_origin).grid(row=6, column=0)

authors_name = IntVar()
name_check = Checkbutton(inner_frame, text="Name", variable=authors_name)
name_check.grid(row=3, column=1)
name_check.select()
authors_notes = IntVar()
Checkbutton(inner_frame, text="Notes", variable=authors_notes).grid(row=4, column=1)

conditions_binding = IntVar()
Checkbutton(inner_frame, text="Binding", variable=conditions_binding).grid(row=3, column=2)
conditions_grade = IntVar()
Checkbutton(inner_frame, text="Grade", variable=conditions_grade).grid(row=4, column=2)

other_price = IntVar()
Checkbutton(inner_frame, text="Price", variable=other_price).grid(row=3, column=3)
other_publisher = IntVar()
Checkbutton(inner_frame, text="Publisher", variable=other_publisher).grid(row=4, column=3)
other_language = IntVar()
Checkbutton(inner_frame, text="Language", variable=other_language).grid(row=5, column=3)


# Button(inner_frame, text='Quit', command=inner_frame.quit).grid(row=6, sticky=W, pady=4)
Button(inner_frame, text='Search', command=search_button_logic).grid(row=7, column=1, sticky="N",columnspan=2)





root.mainloop()