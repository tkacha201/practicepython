import random
print("Guess a random number between 1 and 9 inclusive")
rand_number = random.randint(1, 9)
while True:
    guess = int(input("Guess a number: "))
    if guess == rand_number:
        print("That's correct!")
        break
    elif guess > rand_number:
        print("Go lower!")
    else:
        print("Go higher!")

#see extra stuff for this
