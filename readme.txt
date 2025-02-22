#python?
## python is a popular programming language.
## python is a high-level language.
## python can be used on a server to create web application.

# variables?
## variables are used to store data in a program.(or)
## variables are containers for storing data values.

# data types?
a = "hello world!" # str
print(type(a))

b = 234 # int
print(type(b))

c = 12.90 # float
print(type(c))

d = True # bool (True or False.)
print(type(d))

e = [1,"egg",2,"orange",3,4,5] # list
print(type(e))

f = (1,"apple",2,"tree") # tuple
print(type(f))

g = {1,"apple",2,"tree"} # set
print(type(g))

h = { 
    "name" : "rani",
    "age" : 23 ,
    "add" : "uk"
} # dict
print(type(h))
 
# user input (it python allows for user input.)
user_input = input("Enter your name: ")
print(user_input)

# casting (converting one datatype into another datatype.)
a = int("90")
b = int("23")
c = a + b
print(c)

# control statement?
## Control statements are used to control the flow of a program's execution. 
## They allow you to make decisions, repeat tasks, and skip over code.
# if and else;
a = 10
if a > 15:
  print("True")
else:
  print("False")

# if and elif and else;
a = 34
if a > 90:
  print("greater than")
elif a < 90:
  print("less than")
else:
  print("equal to")

# for loop;
loop = [1,2,3,6,7,8,9]
for i in loop:
  print(i)

# range
for i in range(0,10):
  print(i)


