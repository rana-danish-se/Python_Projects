import random

randomNumber = random.randint(1, 100)
def guess_number():
   while True:
      guess=input("Guess a number between 1 and 100: ")
      global attempts
      attempts += 1
      if not guess.isdigit():
         print("Please enter a valid number.")
         continue
      guess = int(guess)
      if guess < 1 or guess > 100:
         print("Your guess is out of range. Please try again.")
         continue
      if guess < randomNumber:
         print("Your guess is too low. Try again.")     
      elif guess > randomNumber:
         print("Your guess is too high. Try again.")
      else:
         print(f"Congratulations! You've guessed the number {randomNumber} in {attempts} attempts.")
         break  
if __name__ == "__main__":
   attempts = 0
   print("Welcome to the Guess the Number Game!")
   guess_number()
   print("Thanks for playing!")
      