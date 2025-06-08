import tkinter as tk
from tkinter import messagebox

def show_details():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    course = course_entry.get()

    # Create a new window to display the details
    display_window = tk.Toplevel(root)
    display_window.title("Student Details")

    info = f"Name: {name}\nAge: {age}\nGender: {gender}\nCourse: {course}"
    tk.Label(display_window, text=info, font=("Arial", 12), padx=10, pady=10).pack()

# Main window
root = tk.Tk()
root.title("Student Registration Form")

tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Age:").grid(row=1, column=0, sticky="w")
age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1)

tk.Label(root, text="Gender:").grid(row=2, column=0, sticky="w")
gender_var = tk.StringVar(value="Male")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").grid(row=2, column=2, sticky="w")

tk.Label(root, text="Course:").grid(row=3, column=0, sticky="w")
course_entry = tk.Entry(root)
course_entry.grid(row=3, column=1)

submit_button = tk.Button(root, text="Submit", command=show_details)
submit_button.grid(row=4, column=1, pady=10)

root.mainloop()
