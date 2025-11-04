import random


def main():
    rand_num = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = input("Guess a number between 1 and 100: ")

        if user_guess == 'q':
            print("You chose to quit the game. Goodbye!")
            break
        elif not user_guess.isdigit():
            print("Invalid input. Please enter a number between 1 and 100 or 'q' to quit.")
            continue
        user_guess = int(user_guess)
        if user_guess < 1 or user_guess > 100:
            print("Your guess is out of range. Please try again. Your guess must be between 1 and 100.")
            continue

        if user_guess < rand_num:
            print("your guess is too low. Try again.")
            print("Attempts:", attempts + 1)
        elif user_guess > rand_num:
            print("Your guess is too high. Try again.")
            print("Attempts:", attempts + 1)
        else:
            print("Congratulations! You've guessed the correct number:", rand_num)
            print("Attempts:", attempts + 1)
            want_to_play = input("Do you want to play again? (y/n): ").lower()
            if want_to_play == 'y':
                rand_num = random.randint(1, 100)
                attempts = 0
                continue
            else:
                print("Thank you for playing! Goodbye!")
            break
        attempts += 1


if __name__ == "__main__":
    main()