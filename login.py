import tkinter as tk
from tkinter import messagebox

# Create main application window
root = tk.Tk()
root.title("Login Page")
root.geometry("300x200")

# Function to handle login logic
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    messagebox.showinfo("Login", "Login Successful")
    entry_username.delete(0,tk.END)
    entry_password.delete(0,tk.END)
# Name (title)
title = tk.Label(root, text="Login Page", font=20, bg="red")
title.grid(row=0, column=0, columnspan=2, pady=10)  # title spans across two columns

# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.grid(row=1, column=0, pady=5, padx=10, sticky="e")  # 'e' aligns text to the right

entry_username = tk.Entry(root)
entry_username.grid(row=1, column=1, pady=5, padx=10)

# Password label and entry
label_password = tk.Label(root, text="Password:")
label_password.grid(row=2, column=0, pady=5, padx=10, sticky="e")  # 'e' aligns text to the right

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=2, column=1, pady=5, padx=10)

# Login button
button_login = tk.Button(root, text="Login", command=login)
button_login.grid(row=3, column=0, columnspan=2, pady=20)

# Start the Tkinter event loop
root.mainloop()
