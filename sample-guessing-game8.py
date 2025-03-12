secret_number = 9
Guess_count = 0
Guess_limit = 3
while Guess_count < Guess_limit:
  Guess = int(input("Guess: "))
  Guess_count += 1
  if Guess == secret_number:
    print("You won!")
    break
else:
  print("Sorry, You failed!")
