

import tkinter as tk #toolkit for creating GUI applications in Python
from tkinter import filedialog, messagebox
from tkinter import font

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Aesthetic Text Editor")
        self.root.geometry("900x600")

        # --- Font (clean coding style) ---
        self.font = font.Font(family="Consolas", size=12)

        # --- Text Area ---
        self.text_area = tk.Text(
            root,
            wrap="word", #wrap casually means that the text will wrap to the next line when it reaches the end of the current line , we could use none and char ; none means that the text will not wrap and it will continue on the same line until we hit enter , char means that the text will wrap at the character level so it will break words if necessary to fit the line
            font=self.font,
            undo=True,
            bg="#1e1e1e",
            fg="#d4d4d4",
            insertbackground="white",
            selectbackground="#264f78"
        )
        self.text_area.pack(fill="both", expand=True)

        # --- Scrollbar ---
        scrollbar = tk.Scrollbar(self.text_area)
        scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)

        # --- Menu ---
        self.create_menu()

        # --- Keyboard shortcuts ---
        self.bind_shortcuts()

    # ---------------- MENU ----------------
    def create_menu(self):
        menu_bar = tk.Menu(self.root)

        # File menu
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        # Edit menu
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Clear", command=self.clear_text)
        menu_bar.add_cascade(label="Edit", menu=edit_menu)

        self.root.config(menu=menu_bar)

    # ---------------- FUNCTIONS ----------------
    def new_file(self):
        self.text_area.delete("1.0", tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)

    def save_file(self):
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get("1.0", tk.END))
            messagebox.showinfo("Saved", "File saved successfully!")

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

    # ---------------- SHORTCUTS ----------------
    def bind_shortcuts(self):
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    root = tk.Tk() #Tk() is a function/class that creates the main application window
    app = TextEditor(root)
    root.mainloop()