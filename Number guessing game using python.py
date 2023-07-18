import random
n=random.randrange(1,20)
guess=  int(input("Enter your number:"))
while n != guess:
    if n > guess:
          print("the number is too high")
          guess = int(input("Enter your number again :"))
    elif n < guess:
          print("The number is too low")
          guess= int(input("Enter your number :"))
    else:
      break  
print("YOU GUESSED IT'S RIGHT")     