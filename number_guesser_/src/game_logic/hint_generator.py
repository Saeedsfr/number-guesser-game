def provide_hint(guess, actual_number):
    """Provide a hint based on the guess and the actual number.
    """
    if guess < actual_number:
        return "Try a higher number!"
    elif guess > actual_number:
        return "Try a lower number!"
    else:
        return "Congratulations! You've guessed the correct number!"