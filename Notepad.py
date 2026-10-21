import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import subprocess
import sys
import os

class PythonNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Notepad")
        self.root.geometry("900x600")

        self.filename = None
        self.locked = False
        self.password = "1234"

        self.text = tk.Text(
            root, wrap="none", undo=True,
            font=("Consolas", 12)
        )
        self.text.pack(fill="both", expand=True)

        self.status = tk.Label(
            root, text="Ready", anchor="w"
        )
        self.status.pack(fill="x")

        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        # File menu
        file_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(
            label="Save As", command=self.save_as
        )
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit menu
        edit_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo)
        edit_menu.add_command(label="Redo", command=self.redo)
        edit_menu.add_separator()
        edit_menu.add_command(
            label="Cut", command=lambda: self.text.event_generate("<<Cut>>")
        )
        edit_menu.add_command(
            label="Copy", command=lambda: self.text.event_generate("<<Copy>>")
        )
        edit_menu.add_command(
            label="Paste", command=lambda: self.text.event_generate("<<Paste>>")
        )
        edit_menu.add_command(
            label="Select All", command=self.select_all
        )

        # Lock menu
        lock_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Lock", menu=lock_menu)
        lock_menu.add_command(
            label="Lock Editing", command=self.lock_editing
        )
        lock_menu.add_command(
            label="Unlock Editing", command=self.unlock_editing
        )

        # Python menu
        python_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Python", menu=python_menu)
        python_menu.add_command(
            label="Run Code (F5)", command=self.run_code
        )

        self.root.bind("<F5>", lambda event: self.run_code())

    def new_file(self):
        if self.confirm_discard():
            self.text.config(state="normal")
            self.text.delete("1.0", "end")
            self.filename = None
            self.locked = False
            self.status.config(text="New file")

    def open_file(self):
        path = filedialog.askopenfilename(
            filetypes=[
                ("Python files", "*.py"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        if path:
            try:
                with open(path, "r", encoding="utf-8") as file:
                    content = file.read()
                self.text.config(state="normal")
                self.text.delete("1.0", "end")
                self.text.insert("1.0", content)
                self.filename = path
                self.locked = False
                self.status.config(text=f"Opened: {path}")
            except OSError as error:
                messagebox.showerror("Open Error", str(error))

    def save_file(self):
        if not self.filename:
            return self.save_as()

        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(self.text.get("1.0", "end-1c"))
            self.status.config(text=f"Saved: {self.filename}")
            return True
        except OSError as error:
            messagebox.showerror("Save Error", str(error))
            return False

    def save_as(self):
        path = filedialog.asksaveasfilename(
            defaultextension=".py",
            filetypes=[
                ("Python files", "*.py"),
                ("Text files", "*.txt"),
                ("All files", "*.*")
            ]
        )
        if path:
            self.filename = path
            return self.save_file()
        return False

    def undo(self):
        try:
            self.text.edit_undo()
        except tk.TclError:
            pass

    def redo(self):
        try:
            self.text.edit_redo()
        except tk.TclError:
            pass

    def select_all(self):
        self.text.tag_add("sel", "1.0", "end-1c")
        self.text.mark_set("insert", "1.0")
        self.text.see("insert")
        return "break"

    def lock_editing(self):
        if not self.locked:
            self.text.config(state="disabled")
            self.locked = True
            self.status.config(text="Editing locked")
            messagebox.showinfo("Lock", "Editing is now locked.")

    def unlock_editing(self):
        if self.locked:
            entered = simpledialog.askstring(
                "Unlock", "Enter password:", show="*"
            )
            if entered == self.password:
                self.text.config(state="normal")
                self.locked = False
                self.status.config(text="Editing unlocked")
            elif entered is not None:
                messagebox.showerror("Error", "Incorrect password")

    def run_code(self):
        code = self.text.get("1.0", "end-1c")
        if not code.strip():
            messagebox.showwarning("Python", "Write some code first.")
            return

        if not self.filename or not self.filename.endswith(".py"):
            path = filedialog.asksaveasfilename(
                defaultextension=".py",
                filetypes=[("Python files", "*.py")]
            )
            if not path:
                return
            self.filename = path

        if not self.save_file():
            return

        try:
            subprocess.Popen([sys.executable, self.filename])
            self.status.config(text="Python script started")
        except OSError as error:
            messagebox.showerror("Run Error", str(error))

    def confirm_discard(self):
        if self.text.edit_modified():
            answer = messagebox.askyesnocancel(
                "Unsaved Changes",
                "Save changes before continuing?"
            )
            if answer is None:
                return False
            if answer and not self.save_file():
                return False
        self.text.edit_modified(False)
        return True


if __name__ == "__main__":
    root = tk.Tk()
    app = PythonNotepad(root)
    root.mainloop()
