# Mini Greeting App

# Build this yourself:

# ┌────────────────────────────┐
# │        Greeting App        │
# │                            │
# │ Enter your name:           │
# │ [______________________]   │
# │                            │
# │       [ Greet ]            │
# │                            │
# │ Hello, Nishchint!          │
# └────────────────────────────┘

# Requirements:

# Label saying "Enter your name:"
# Entry for the name
# Button "Greet"
# Another Label initially saying something like "...".
# When the button is clicked, the bottom label should change to:
# Hello, <name>!
#  New thing you'll need

# You can change a Label's text using:

# label.config(text="New text")

# So if:

# result = tk.Label(root, text="...")

# you can later do:

# result.config(text="Hello!")

# Try to build the whole thing without copying a solution.


# Solution ***************

import tkinter as tk
window = tk.Tk()
window.title("Greeting App")
window.geometry("500x400") #size of your window 
window.configure(bg="lightpink")

lable= tk.Label(window , text="My Greeting App")
lable.pack()  #keep inside the window 
entry= tk.Entry(window  )
entry.pack()

lable.configure( bg="red" , fg="white" , font=('Arial 10')) #you can make the changes later 

def greet():
    print(f"Hello , {entry.get()}")

btn= tk.Button(window , text="greet" , command=greet) #onclick means command here 
btn.pack()




window.mainloop()