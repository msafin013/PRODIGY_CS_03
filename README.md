##Password Strength Checker

This is a simple Python application that evaluates the strength of a given password and provides feedback on how to improve it. The application uses `tkinter` for the graphical user interface and `re` for regular expression operations.

Features

- **Password Strength Evaluation**: Checks if the password meets various strength criteria.
- **Feedback**: Provides specific feedback on how to make the password stronger.
- **GUI**: Simple and user-friendly graphical interface built with `tkinter`.

Requirements

- Python 3.x
- `tkinter` (usually included with Python's standard library)

Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/msafin013/PRODIGY_CS_03.git
2. **Navigate to the Project Directory**

   cd PRODIGY_CS_03
3. **Run The Application**

    python passcheck.py

How It Works

    Password Input: Enter a password in the input field.
    Check Strength: Click the "Check Strength" button to evaluate the password.
    Strength Message: The strength of the password will be displayed.
    Feedback: Specific feedback on how to improve the password will be shown in the listbox.

Code Overview
check_password_strength(password)

Evaluates the strength of the given password based on the following criteria:

    Length (minimum 10 characters)
    Presence of at least one uppercase letter
    Presence of at least one lowercase letter
    Presence of at least one number
    Presence of at least one special character

Returns a strength message and a list of feedback items.
validate_password()

Retrieves the password from the entry widget, checks its strength using check_password_strength(), and updates the GUI with the result and feedback.
GUI Setup

    Main Window: Created using tk.Tk()
    Widgets: Label, Entry, Button, Label (for result), and Listbox (for feedback)
    Layout: Widgets are arranged using grid layout
