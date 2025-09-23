# Full interactive guessing game

secret_number = 7  # The number to guess
guess = None  # Start with no guess

print("Welcome to the guessing game! 🎮")
print("Try to guess the secret number between 1 and 10.")

# Keep asking until the player guesses correctly
while guess != secret_number:
    guess = int(input("Your guess: "))
    print("You guessed {}. The secret number is {}.".format(guess, secret_number))
    
    if guess < secret_number:
        print("🔼 Too low! Try a bigger number.")
    elif guess > secret_number:
        print("🔽 Too high! Try a smaller number.")
    else:
        print("🎉 Amazing! You guessed it right!")
