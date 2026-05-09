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
# ///////////////////////////////////////////////////Guide the use in the game 
# FIRST UNDERSTAND THE PROBLEM
# Suppose:
# def hello():
#     print("Hello")
# Now:
# command=hello
# means:
#  “Store the function”
#  “Run it later when clicked”
# NOT now.
#  THIS IS WRONG
# command=hello()
# Because:
# () means RUN NOW
# function executes immediately
# Then nothing remains for button click later.
#  HUGE CONCEPT
# There is a difference between:
# Code	Meaning
# hello	function itself
# hello()	execute function
#  NOW THE REAL PROBLEM
# Our function needs an argument:
# click(i)
# But button command expects:
# some_function
# NOT:
# some_function(argument)
#  THIS FAILS
# command=click(i)
# Because during button creation:
# loop runs instantly
# click executes instantly
#  So what do we need?
# We need:
#  “A tiny function that waits until click happens”
# That tiny temporary function is:
# lambda
#  SIMPLEST LAMBDA EVER
# lambda: print("Hello")
# Meaning:
#  “create unnamed tiny function”
# Equivalent to:
# def temp():
#     print("Hello")
#  IMPORTANT
# Lambda does NOT run immediately.
# It CREATES a function.
#  YOUR CASE
# lambda: click(i)
# means:
#  “When called later, execute click(i)”
#  VISUALIZE IT
# Instead of this:
# command=click(i)
# you are effectively doing:
# def temp():
#     click(i)
# command=temp
#  NOW THE BIG CONFUSION:
# Why i=i ?
# THIS is the real tricky part.
#  Understand loop problem first
# for i in range(3):
#     funcs.append(lambda: print(i))
# People EXPECT:
# 0
# 1
# 2
# But actual result:
# 2
# 2
# 2
#  WHY?
# Because lambda does NOT store VALUE.
# It remembers VARIABLE REFERENCE.
# Meaning:
#  “I’ll check i later when function runs”
# After loop ends:
# i = 2
# So every lambda sees:
# 2
#  FIX
# lambda i=i: print(i)
# Now current value gets copied permanently.
#  Think of it like snapshot
# Without i=i:
#  lambda remembers live variable
# With i=i:
#  lambda takes photo of current value
#  YOUR BUTTONS CASE
# During loop:
# Iteration 1:
# i = 0
# stores:
# lambda i=0: click(0)
# Iteration 2:
# i = 1
# stores:
# lambda i=1: click(1)
# etc.
#  FINAL UNDERSTANDING
# command=lambda i=i: click(i)
# really means:
#  “Create a tiny function for this button”
#  “Remember this button’s index”
#  “Run click(index) later when user clicks”
#  WHY YOU FORGET LAMBDA
# Because most people memorize:
# lambda x: ...
# instead of understanding:
# lambda = temporary tiny function
# Once THIS clicks,
# syntax becomes much easier.
#  GOLDEN RULE
# Whenever you see lambda, ask:
# Am I creating a tiny function to run later?
# Usually answer is YES.
# //////////////////////////////////////////////////further explanation 



# EXAMPLE 1 — MULTIPLE PARAMETERS
# add = lambda a, b: a + b
# What it means:
#  “Take a and b, return a + b”
# Usage:
# add(2, 3)
# Output:
# 5
#  SAME THING AS NORMAL FUNCTION
# def add(a, b):
#     return a + b
# So lambda is just a short version.
#  EXAMPLE 2 — THREE PARAMETERS
# multiply = lambda a, b, c: a * b * c
# Usage:
# multiply(2, 3, 4)
# Output:
# 24
#  KEY RULE
#  Number of inputs = flexible
#  Output = ONLY one expression
#  WHAT YOU CANNOT DO IN LAMBDA
# # You cannot write:
# lambda x:
#     y = x + 1
#     return y
#  Not allowed
# Because lambda does NOT support multiple statements.
#  WHY ONLY ONE EXPRESSION?
# Because lambda is designed to be:
#  tiny
#  inline
#  quick function
# Not full logic blocks.
#  WHAT IS AN “EXPRESSION”?
# An expression is something that produces a value:
# x + 1
# x * 2
# a > b
# "hello".upper()
#  WHAT IS NOT ALLOWED?
# Statements like:
# if
# for
# while
# assignment (x = 5)
#  EXAMPLE 3 — USING LOGIC INSIDE LAMBDA
# You can still do conditional logic:
# max_value = lambda a, b: a if a > b else b
# Usage:
# max_value(10, 5)
# Output:
# 10
#  EXAMPLE 4 — YOUR TIC TAC TOE STYLE
# lambda i=i: click(i)
# Here:
# Inputs:
# i=i (default parameter trick)
# Expression:
# click(i)
# So it means:
#  “when called, run click(i)”
#  HOW MULTIPLE PARAMETERS + SINGLE EXPRESSION WORK TOGETHER
# Example:
# f = lambda x, y, z: x + y * z
# Break it:
# Inputs:
# x
# y
# z
# Expression (ONLY ONE):
# x + y * z
# Result is a single value.
#  THINK LIKE THIS
# Lambda is like a machine:
# INPUTS  →  ONE FORMULA  →  OUTPUT
# No steps in between.
#  REAL-LIFE ANALOGY
# Think of a vending machine:
# you give inputs (money + button)
# it returns ONE thing (drink)
# You don’t see internal steps.