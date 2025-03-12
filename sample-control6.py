# control statement #
is_hot = False
is_cold = False
if is_hot:
  print("It's a hot day")
  print("Drink more water")
elif is_cold :
  print("It's a cold day")
  print("Wear warm clothes")
else:
  print("It's a lovely day")
print("Enjoy your day")

# example:
price = 1000000
good_credit = True
if good_credit:
  down_payment = 0.1 * price
else:
  down_payment = 0.2 * price
print(f"Down payment: ${down_payment}")


# logical operators
# and ==> both are true , it true
# or ==> either is true , it true
# not ==> opposite of the statement 
has_good_credit = False
has_criminal_record = False
if has_good_credit and not has_criminal_record:
  print("Eligible for loan")

# comparison operators
temperature = 30
if temperature >= 30:
  print("It's a hot day")
elif temperature <= 10:
  print("It's a cold day")
else:
  print("It's neither hot nor cold")


name = "Sai"
if len(name) <= 3:
  print("Name must be at least 3 characters")
elif len(name) >= 50:
  print("Name can be a maximum of 50 characters")
else:
  print("Name looks good")

# While Loops
i = 1
while i <= 5:
  print(i)
  i += 1
print("done") 


# another example in pattern
i = 1
while i <= 5:
  print("*" * i)
  i += 1


# forloop
for item in 'Python':
  print(item)

for item in ["Apple" , "Rani" , "Orange"]:
  print(item)

for item in [1,2,3,4,5]:
  print(item)

for item in range(1,10,2):
  print(item)

# nested loops
for x in range(4):
  for y in range(3):
    print(f"({x},{y})")
    
  