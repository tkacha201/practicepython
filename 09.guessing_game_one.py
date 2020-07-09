import random
print("Guess a random number between 1 and 9 inclusive")
rand_number = random.randint(1, 9)
num_guesses = 0
while True:
    guess = input("Guess a number: ")
    if guess == 'exit':
        print(f'You guessed {num_guesses} times!')
        break
    if int(guess) == rand_number:
        print("That's correct!")
        num_guesses += 1
    elif int(guess) > rand_number:
        print("Go lower!")
        num_guesses += 1
    else:
        print("Go higher!")
        num_guesses += 1

#see extra stuff for this
