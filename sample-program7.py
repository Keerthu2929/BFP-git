# weight converter program :
User_weight = int(input("Enter your weight: "))
User_input = input("(L)bs or (k)g: ")
if User_input.upper() == "L":
  converted = User_weight * 0.45
  print(f"Your weight in kg is {converted} kg")
else:
  converted = User_weight / 0.45
  print(f"Your weight in Lbs is {converted} Lbs") 
