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
inner_frame.grid_rowconfigure(0, weight=4)  # row containing the conditional search field
inner_frame.grid_rowconfigure(1, weight=1)  # rows containing the checkboxes (4x4 grid)
inner_frame.grid_rowconfigure(2, weight=1)
inner_frame.grid_rowconfigure(3, weight=1)
inner_frame.grid_rowconfigure(4, weight=1)

# inner_frame column configuration
inner_frame.grid_columnconfigure(0, weight=1) # columns containing the checkboxes (4x4 grid)
inner_frame.grid_columnconfigure(1, weight=1)
inner_frame.grid_columnconfigure(2, weight=1)
inner_frame.grid_columnconfigure(3, weight=1)

# TODO: Render table based on input/selections from rows 2 + 3 on row 4






root.mainloop()