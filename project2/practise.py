



# import tkinter as tk
# from tkinter import messagebox


# window=tk.Tk() #window in which the grid for game is being created 
# window.title("tick tack toe ")

# board=[""] *9 #these are the solts 
# buttons=[]  #we will append the buttons UI in it 
# current_player="X"


# def checkWinner():
#     winning=[(0,1,2) , (3,4,5) , (6,7,8) , (0,3,6) , (1,4,7) , (2,5,8),(0,4,8) , (2,4,6)]

#     for a , b , c in winning:
#         if board[a]==board[b]==board[c]!="":
#             return board[a] #all are same , either X will be there or O
#     return None 
    
# def click(index): #at every click , check if slot is empty then add a player move , 
#     global current_player
#     if board[index]== "":
#         board[index]=current_player
#         buttons[index].config(text=current_player) #for Text UI

#         winner =checkWinner() #keeps checking the wins

#         if winner:
#             messagebox.showinfo("Game Over" , f"the player {current_player} wins!")
#             resetgame()
#             return
#         #if board!= "": #this is wrong line , it means when the board is not empty which can happen at the very first click when one slot is allocated only 
#         if  "" not in board : #now this means when not even one empty seat left in the board 
#             messagebox.showinfo("The Game is Over" , f"the match is draw! ")
#             resetgame()
#             return

#         current_player="O" if current_player=="X" else "X" #switch the existing player everytime before the next click 

# def resetgame():
#     global buttons , board , current_player #changing the same variables 
#     board=[""]*9
#     current_player="X"
#     for btn in buttons: #this is for UI so remove the text on button  remvoe X or O
#         btn.config(text="") #removing text for next game

# # now actually creating the buttons 
# for i in range(9): #creating 9 required buttons
#     btn=tk.Button(
#         window ,
#         text="" ,
#         width=5,
#         height=2,
#         font=("Arial" , 24),
#         command= lambda i=i: click(i)
#         )
#     btn.grid(row= i//3 , column= i%3) #intrsting way to change UI through maths 
#     buttons.append(btn)
# window.mainloop() #finally running the app created in window 
##and the app never stops running becuase of this line as well 


# lambda working   : lamda is just a function without a name and it can take any number of arguments but can only have one expression
# x=lambda : print("hello")
# x()

# in the game : 
# Instead of this:
# command=click(i)
# you are effectively doing:
# def temp():
#     click(i)
# command=temp




# funcs=[]
# for i in range(3):
#     funcs.append(lambda : print(i))

# for f in funcs:
#     f()


# output: 
# 2
# 2
# 2

# as lambda just store the reference , not immediately  executes the function  , but later on 

# solution : but yes we can copy the current value of iteration like this 
funcs=[]
for i in range(3):
    funcs.append(lambda i=i : print(i))

for f in funcs:
    f() # as functions are stored here so we called f() like that 
