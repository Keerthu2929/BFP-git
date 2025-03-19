# basics list
# list are used to store multiple items in a single variable.
# list are ordered, changeable and allow duplicates values.
# list are denoted by square brackets []
# list are mutable
names = ["Sita", "Rani", "Sai", "Abi", "Vij", "Raj"]
names[0] = "Mani" 
print(names)

# slicing operations
print(names[2:4])
print(names[2:])
print(names[-4:-2])

# exercise find the largest number in a list.
numbers = [12,4,8,3,80,23,45]
print(max(numbers))

# or

numbers = [12,4,8,3,90,23,45,99]
max = numbers[0]
for number in numbers:
  if number > max:
    max = number
print(max)



## list method ##
number = [12, 8, 9, 20, 4, 3, 2, 2, 90]
# append() - adds an element to the end of the list
number.append(100)
# extend() - adds multiple elements to the end of the list
number.extend([1, 2, 3, 4, 5])
# insert() - adds an element at a specified position in the list
number.insert(2,10)
# remove() - removes the first occurrence of the element in the list
number.remove(12)
# sort() - sorts the list in ascending order
number.sort()
# reverse() - reverses the list
number.reverse()
# index() - returns the index of the first occurrence of the element in the list
# index operations
x = number.index(8)
print(type(numbers[2]))
del numbers[2]
print(numbers)
# count() - returns the number of occurrences of the element in the list
y = number.count(2)
print(number)
print(x)
print(y)

print(type(number[-1]))
 

print(len(names + numbers))

# merge the contents names , numbers
print(names + numbers + names)
