
import random
number = random.randint(1,10)
userguess = int(input("Take a guess from 1 to 10!"))
counter = 0
while (userguess != number): 
    userguess = int(input("That's unfortunate. Try again."))
    counter += 1
    if counter >10 :
        print("Damn, are you unlucky?")

print("Well done!")