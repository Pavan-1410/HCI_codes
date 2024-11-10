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
   

# Username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
