import random

def guessing_number():
  print("Welcome to the Number Guessing Number")
  print("I am thinking of a number between 1 and 100")

  secret_number=random.randint(1,100)
  attempts=0

  while True:
    guess=input("Take a guess")

    if not guess.isdigit():
      print("Please enter a valid number")
      continue

    guess=int(guess)
    attempts+=1


    if guess<secret_number:
      print("Too Low")
    elif guess>secret_number:
      print("Too High")
    else:
      print(f"Congrats you have found {attempts} attempts")

    
if __name__=="__main__":
  guessing_number()
  