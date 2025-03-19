# two dimensional list
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
# matrix[0][1] = 20
# print(matrix[0][1])
for row in matrix:
  for element in row:
    # print(element, end='')
    print(element)


# remove duplicates value in list
numbers = [1,6,8,2,1,9,10,1,1,1]
uniques = []
for number in numbers:
  if number not in uniques:
    uniques.append(number)
print(uniques)

