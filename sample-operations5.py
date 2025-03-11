# Arithmetic operations
x = 12
y = x + 3
print(y) ## 15

# assignment operations
y += 5
print(y) ## 20


# operator precedence
x = 10 + 3 * 2 ** 2 ## 22
a = 2 ** 2  # 4 (exponentiation)  
b = 3 * 4  # 12
c = 10 + 12 # 22
print(f"{a}\n{b}\n{c}\n{x}")


x = (2 + 3) * 10 - 3 ## 47
a = 2 + 3 # 5
b = 5 * 10 # 50
c = 50 - 3 # 47
print(f"{a}\n{b}\n{c}\n{x}") 


#  math functions
x = 2.9
print(round(x)) ## 3
print(abs(-2.9)) ## 2.9

## module ##
import math
# ceiling function is the smallest integer greater than or equal to x 
print(math.ceil(2.9))
# floor function is the largest integer less than or equal to x 
print(math.floor(2.9))
