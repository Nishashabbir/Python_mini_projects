
# we are going to make it user friendly through GUI ,  using tkiter library 

import tkinter as tk
from time import strftime

window =tk.Tk()
window.title("Digital Clock")

def time():
    string= strftime('%H:%M:%S %p \n %D')
    label.config(text=string) #here config casually means that we are configuring the label to show the time that we got from strftime function
    label.after(1000, time)
# label is just being created but to visualize it we will use pack 
label= tk.Label(window, font=('calibari' , 50 , 'bold') , background="Green" , foreground="white")
label.pack(anchor='center') #here we used pack becuase to visually show the label that we created 

time()
window.mainloop()
    






# practise again 
















import tkinter as tk
from time import strftime

window=tk.Tk()
window.title("Digital Clock")

def time():
    string=strftime('%H:%M:%S \n %D')
    label.config(text=string)
    label.after(1000, time)

label=tk.Label(window , font=('calibari' , 50 , "bold" ) , background="yellow" , foreground="black")
label.pack(anchor="center")






time()
window.mainloop()