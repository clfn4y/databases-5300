import tkinter as tk
import mariadb
import sys


def database_connection():
  try:
    connection = mariadb.connect(
      user="mdmfvz",
      password="my2BOYZ!",
      host="cs-class-db.srv.mst.edu",
      port=3306,
      database="mdmfvz"
    )

  except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

  return connection

def button_creation(label):
  button = tk.Button(
    text=label,
    width=25,
    height=5,
    bg="green",
    fg="black",
    font=("Arial", 15)
  )

  return button


conn = database_connection()
curr = conn.cursor()




#curr.execute(SQL_statement)

#conn.commit()
#conn.close()

window = tk.Tk()
title = tk.Label(
    text="Database Querying Application",
    fg="black",  
    bg="white" ,
    width=50,
    height=5,
    font=("Arial", 20)
)

#books_button = button_creation("Books")
#quality_button = button_creation("Quality")
title.pack()
#books_button.pack()
#quality_button.pack(side=tk.RIGHT)
window.mainloop()



print("Worked")