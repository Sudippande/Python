
#program to count the number of vowel in the string
# a="sudipa aeiou"
# b='a','e','i','o','u'
# count=0
# for i in b:
#     for j in a:
#         if i==j:
#             count+=1
# print(count)

# a="sudip anand"
# count=0
# for j in a:
#         if j =='a'or 'e' or 'i' or 'o'or 'u':
#     # if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
#             count+=1
# print(count)

# def fibo(n):
#     a=b=1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# for x in fibo(10):
#     print(x)

# def hi(name='ram'):
#     def greet():
#         return'Hi my name is sudip' 
    
#     def hii():
#         return"Op"
    
#     if name=='ram':
#         return greet
#     else:
#         return hii

# a=hi('ram')
# print(a())
# from ctypes import *
# a=6
# print('hi',a)

import tkinter as tk
from tkinter import messagebox, filedialog

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x450")
        self.root.resizable(False, False)

        # Title
        tk.Label(root, text="My To-Do List", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Entry field
        self.task_entry = tk.Entry(root, font=("Helvetica", 14), width=28)
        self.task_entry.pack(pady=5)

        # Add Task button
        tk.Button(root, text="Add Task", width=20, command=self.add_task).pack(pady=5)

        # Listbox
        self.task_listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=10)
        self.task_listbox.pack(pady=10)

        # Buttons for delete, save, load
        tk.Button(root, text="Delete Selected Task", width=20, command=self.delete_task).pack(pady=5)
        tk.Button(root, text="Save Tasks", width=20, command=self.save_tasks).pack(pady=5)
        tk.Button(root, text="Load Tasks", width=20, command=self.load_tasks).pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task != "":
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected)
        else:
            messagebox.showwarning("Selection Error", "No task selected.")

    def save_tasks(self):
        tasks = self.task_listbox.get(0, tk.END)
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "w") as f:
                for task in tasks:
                    f.write(task + "\n")
            messagebox.showinfo("Save Successful", "Tasks saved successfully.")

    def load_tasks(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            self.task_listbox.delete(0, tk.END)
            with open(file, "r") as f:
                for line in f:
                    self.task_listbox.insert(tk.END, line.strip())

# Create main window
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()

