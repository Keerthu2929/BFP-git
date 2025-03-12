numbers = [5, 2, 5, 2, 2]
for i in numbers:
  print("x" * i)

# (or)

numbers = [5, 2, 5, 2, 2]
for i in numbers:
  output = ''
  for count in range(i):
    output += 'x'
  print(output)



numbers = [5, 4, 3, 2, 1]
for i in numbers:
  print("*" * i)


# number = [6, 5, 4, 3, 2, 1]
# for x in number:
#   x += 1
#   print("*" * x)