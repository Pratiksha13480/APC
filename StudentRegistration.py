import tkinter as tk
from tkinter import messagebox

def register():
    name = e1.get()
    age = e2.get()
    course = e3.get()

    if name == "" or age == "" or course == "":
        messagebox.showerror("Error", "Please fill all fields")
    else:
        messagebox.showinfo(
            "Registration",
            "Student Registered Successfully!\n"
            + "Name: " + name
            + "\nAge: " + age
            + "\nCourse: " + course
        )

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("300x300")

tk.Label(root, text="Student Registration",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Student Name").pack()
e1 = tk.Entry(root)
e1.pack(pady=5)

tk.Label(root, text="Age").pack()
e2 = tk.Entry(root)
e2.pack(pady=5)

tk.Label(root, text="Course").pack()
e3 = tk.Entry(root)
e3.pack(pady=5)

tk.Button(root, text="Register",
          command=register).pack(pady=15)

root.mainloop()

