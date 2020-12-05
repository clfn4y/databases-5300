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

def button_creation(label):
  button = Button(
    text=label,
    width=25,
    height=5,
    bg="green",
    fg="black",
    font=("Arial", 15)
  )

  return button


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

#grid setup. row 0 is label, 1 is search field, 2 is checkboxes?, 3 is table return
#column 2 to center your cell
frame.grid(row=0, column=0, sticky="NESW")
frame.grid_rowconfigure(0, weight=1)
frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=2)
frame.grid_rowconfigure(3, weight=10)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

#Title Creation
title = Label(
    frame,
    text="Database Querying Application",
    fg="black",  
    bg="white",
    font=("Arial", 25)
)
#Positioning 
title.grid(row=0, column=2)

#Dropdown Bar Creation
#Too small rn, set the size how you like

drop_down_var = StringVar(frame)
#Default Value
drop_down_var.set('Title')
dd_choices = { 'Title', 'Author', 'Release Date', 'Binding', 
'Grade', 'Language', 'Price'}
drop_down = OptionMenu(frame, drop_down_var, *dd_choices)
#Positioning
drop_down.grid(row=1,column=2)









root.mainloop()