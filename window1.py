# First file fo the python file 
import tkinter as tk    #importing the library for pop-up window
from tkinter import messagebox as mb 


def login():
    global username
    global password
    
    username = entry_username.get()
    password = entry_password.get()

    if username == "admin" and password =="123":
        global logged_on

        logged_on = 1
        mb.showinfo("Login Succesful" , "Welcome, " +  username + "!")
        print("Logged-in Succesfully.")
        window.destroy()                     # this can be commented-out if I want the main window not to be destroyed.
        

    else:
        logged_on = 2
        mb.showerror("Login failed!" , "Invalid Credentials.")
        print("Login Failed.")


logged_on = 0

window = tk.Tk()                             #initializez the creation of the GUI window
window.configure(bg = "#EFAEA1")             #sets the color of the backround to a light brown
window.geometry("400x200")                  #sets the size of the GUI window to 1000x800
window.title("Excel-Reader-Application")     #sets the title of the window to "Excel-Reader-Application"



label_username = tk.Label(window, text="Username:", bg="#C4A484")             # #C4A484 is a more dark brown color code
label_password = tk.Label(window, text="Password:", bg="#C4A484")
entry_username = tk.Entry(window)
entry_password = tk.Entry(window, show="*")

button_login = tk.Button(window, text="Login", command=login)


window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)

label_username.grid(row=0, column=0, padx=5, pady=5, sticky="e")
label_password.grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_username.grid(row=0, column=1, padx=5, pady=5, sticky="w")
entry_password.grid(row=1, column=1, padx=5, pady=5, sticky="w")
button_login.grid(row=2, column=0, columnspan=2, pady=5)


if logged_on == 0:
    print("You are in the process of loggining in.")                  #initial message when running the app. afterwards the logged_on variable is changed and doesn't show again the msg.



window.mainloop()                            #triggers the loop so that the window is running until closure (or something like that)

if logged_on == 1:

    print("Going into the main window.")

    main = tk.Tk()
    main.configure(bg = "#EFAEA1")             
    main.geometry("800x400")                  
    main.title("Excel-Reader-Application -- " + username)     

    main.mainloop()
