import tkinter as tk
from tkinter import messagebox

def validate():
    name = e1.get()
    age = e2.get()

    if name == "" or age == "":
        messagebox.showerror("Error", "Please fill all fields")
    elif not age.isdigit():
        messagebox.showerror("Error", "Age must be a number")
    else:
        messagebox.showinfo("Success", "Student details are valid!")

root = tk.Tk()
root.title("Student Validation Form")
root.geometry("300x250")

tk.Label(root, text="Student Validation Form",
         font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Student Name").pack()
e1 = tk.Entry(root)
e1.pack(pady=5)

tk.Label(root, text="Age").pack()
e2 = tk.Entry(root)
e2.pack(pady=5)

tk.Button(root, text="Validate",
          command=validate).pack(pady=15)

root.mainloop()



