
# arr=[1, 2, 3, 4]

# for i in range( len(arr)):
#     arr[i]+= arr[i-1]  #this is the last element 4 so 1 added to  4 is 5 
# print(arr) 



# 2
# arr = [1, 2, 3, 4]

# for i in range(len(arr)):
#     arr[i] = arr[i] * 2

# print(arr)

# # 3
# arr = [10, 20, 30, 40]

# for i in range(len(arr)):
#     print(arr[i], arr[i-1])

# # 4
# s = "hello" #here string is immutable so we cannot change the value of string but we can change the value of list because list is mutable

# for i in range(len(s)):
#     s[i] = "x"

# print(s)

# 5
# a = [1, 2, 3]
# b = a

# b.append(4)

# print(a)
# print(b)

# # 6
# arr = [1, 2, 3]

# for x in arr:
#     arr.append(x + 10)

# print(arr) #now this will run infinite loop because we are appending the value to the list and we are iterating over the list so it will keep on appending the value to the list and it will never end

# 7

# arr = [1, 2, 3, 4]

# for i in range(len(arr)):
#     arr.append(i)

# print(arr) #this will also run infinite loop because we are appending the value to the list and we are iterating over the list so it will keep on appending the value to the list and it will never end

# # 8
# def func(x, lst=[]):
#     lst.append(x)
#     return lst

# print(func(1))
# print(func(2))
# print(func(3)) #this will print [1], [1, 2], [1, 2, 3] because the default value of lst is mutable so it will keep on appending the value to the list and it will never end


# its solution is to use None as default value and then create a new list inside the function if lst is None
# def func(x, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(x)
#     return lst
# print(func(1))
# print(func(2))
# print(func(3)) #this will print [1], [2], [3] because we are creating a new list inside the function if lst is None so it will not keep on appending the value to the list and it will end after 3 calls

# 9
# x = 10

# def func():
#     x = x + 5
#     return x

# print(func())
# this will raise an UnboundLocalError because we are trying to access the variable x before it is assigned a value inside the function func. To fix this, we can declare x as a global variable inside the function func.

# 10
for i in range(3):
    for j in range(2):
        print(i + j, end=" ")

# this will print 0 1 1 2 2 3 because the outer loop runs 3 times and the inner loop runs 2 times for each iteration of the outer loop. The value of i and j will be added and printed with a space in between.

# 11
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print("\n" , i)
# this will print 0 1 3 because when i is 2, the continue statement will skip the rest of the loop and move to the next iteration. When i is 4, the break statement will exit the loop. So the values 0, 1, and 3 will be printed.
