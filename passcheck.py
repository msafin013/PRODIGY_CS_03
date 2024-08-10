import re
import tkinter as tk
from tkinter import messagebox

def check_password_strength(password):
    # Initialize strength level
    strength = 0
    feedback = []
    
    # Check length
    if len(password) >= 10:
        strength += 1
    else:
        feedback.append("Password should be at least 10 characters long.")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")
    
    # Check for numbers
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number.")
    
    # Check for special characters
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character.")
    
    # Determine strength message
    strength_message = ""
    if strength == 5:
        strength_message = "Password is very strong."
    elif strength == 4:
        strength_message = "Password is strong."
    elif strength == 3:
        strength_message = "Password is moderate."
    elif strength == 2:
        strength_message = "Password is weak."
    else:
        strength_message = "Password is very weak."
    
    return strength_message, feedback

def validate_password():
    password = entry.get()
    strength_message, feedback = check_password_strength(password)
    
    result_label.config(text=strength_message)
    feedback_list.delete(0, tk.END)
    for fb in feedback:
        feedback_list.insert(tk.END, fb)

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")

# Create and place the widgets
tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, padx=10, pady=10)

validate_button = tk.Button(root, text="Check Strength", command=validate_password)
validate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

feedback_list = tk.Listbox(root, width=50, height=5)
feedback_list.grid(row=3, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()
