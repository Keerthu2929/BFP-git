## tuple ##
number = (1, 2, 3, 4, 5)
print(number)
print(number[0])
print(len(number))

# Immutable


# delete entire tuple
# del number[1]
# del number
print(number[3])

number_names = ("mani", "sai", "sri")
all_number = number + number_names
print(all_number[0])

# tuple unpacking
(a, b, c) = number_names
print(a)
print(b)
print(c)

# update
b = list(number_names)
b[1] = "moon"
number_names = tuple(b)
print(b)

# add item
d = list(number_names)
d.append("sun")
number_names = tuple(d)
print(number_names)

# remove
e = list(number_names)
e.remove("moon")
number_names = tuple(e)
print(number_names)

# del
# del number_names
# print(number_names)

# Join Two Tuples
# To join two or more tuples you can use the + operator
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# ... #
tuple_of_two_digits = (12, 3456)
print(tuple_of_two_digits)

tuple_of_two_digits += (33,12)
# tuple_of_two_digits = tuple_of_two_digits + (33,12)
print(tuple_of_two_digits)

tuple_of_two_digits += (330, "yellow")
print(tuple_of_two_digits)

