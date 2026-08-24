
# DAY1 
# PART 1 //////////////////////////////////////////////


import tkinter as tk

# root = tk.Tk()
# # you can add the title and the geometry to the window as well  
# root.title("Nisha's workspace ")
# root.geometry("500x500")   
# root.configure(bg="lightpink")
# root.mainloop()  #name of the window that we created 


# PART 2                     /////////////////////////////////////////////////////////
#  2: Widgets

# Now we get into the actual building blocks of a GUI.
# The most important idea:
# A Tkinter application is basically a window containing widgets.
# For example:

# Window
# │
# ├── Label ; just like the heading 
# ├── Entry ; the input area 
# ├── Button ; 
# └── Checkbutton

# Windows widgets are small, interactive panels on your computer that show real-time information and updates at a glance
# provide quick updates: Show live weather forecasts, sports scores, stock prices, and traffic updates.


# root=tk.Tk()
# root.title("My Window")
# root.geometry("500x400")
# root.configure(bg="lightblue")


# label=tk.Label(root , text="Enter your name here : " , fg="black" , bg="pink" )
# label.pack() #pack means , keep label inside the window 

# entry=tk.Entry(root )
# entry.pack() #keep entery inside the window
# it creates a text area , the user can type into it 

# get the text from this area 
# name = entry.get()
# print(name)

# button= tk.Button(root , text="Submit ")
# button.pack()

# now clicking this button doesn't do anything , we need to write a function that this button should perform when we click it 

# def onclick():
#     print(f"Hello!,{entry.get()}")

# btn= tk.Button(root , text="Click!" , command=onclick) #remember we are not calling this function right now  , but we are giving its control to the button click , whenever that clicks , it is called otherwise not 
# btn.pack()
# # now after clicking this , you can see in the terminal the function output 




# root.mainloop()


# Remember this:////////////////

# tk.Label()    → creates a label
# tk.Entry()    → creates an input box
# tk.Button()   → creates a button

# .pack()       → puts widget on screen

# .get()        → gets Entry's value

# command=      → tells Button what function to run

# That's the core.


# //////////////////////////////////////////

# PART 3  Geometry Managers

# pack() basically arranges widgets along a side. and you can change the direction of the sides top , left , right , bottom 

window = tk.Tk()
window.title("New window")
window.geometry("400x400")

# pack() basically arranges widgets along a side.

# you can change the directions along the side in the pack 

# label1=tk.Label(window , text="side1" )
# label1.pack(side="left")
# label2=tk.Label(window , text="side2")
# label2.pack(side="right")
# label3=tk.Label(window , text="side3")
# label3.pack(side="bottom")
# label4=tk.Label(window , text="side4")
# # label4.pack(side="top" , padx=20  , pady=20)
# label4.pack(side="top") #without padding , see the difference of space around the label 

# btn=tk.Button(window , text="click")
# btn.pack(fill="x" , expand=True)



# GRID  ////////////////////////////////////////////
# it keeps the widgets along the table (row and column )  unlike pack which keeps along the side top  , bottom , left , right 

l1=tk.Label(window , text="username")
l1.grid(row=0 , column=0)
e1=tk.Entry(window )
e1.grid(row=0 , column=1)


l2=tk.Label(window , text="email")
l2.grid(row=1 , column=0)
e2=tk.Entry(window )
e2.grid(row=1, column=1)

l3=tk.Label(window , text="password")
l3.grid(row=2 , column=0)
e3=tk.Entry(window )
e3.grid(row=2 , column=1 , padx=20 , pady=20 , sticky="n")




window.mainloop()







