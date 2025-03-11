# string
name = "jennifer"
print(name[1:-1])


# making format-string
first = "John"
last = "Smith"
msg = f"{first} [{last}] is a code."
print(msg)


# string method
course = "Python for Beginners "

# len (this is general purpose function built into python (we also have specific functions for string))
print(len(course))

# Uppercase it converting a capital letter string 
print(course.upper())

# lowercase it converting a small letter string
print(course.lower())

# title method string
print(course.title())

# find method (which returns the index of a character or sequence of characters.) 
print(course.find("Beginners"))

# replace method for replacing characters and words in a string.
print(course.replace("Beginners","Absolute Beginners"))

# in operator (it like boolean characters in string)
print("Python" in course)
