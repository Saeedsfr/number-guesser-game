from src.utils.input_validator import get_valid_input
from src.game_logic.number_generator import generate_random_number
from src.game_logic.scorer import Scorer

def main():
    scorer = Scorer()
    actual_number = generate_random_number(1, 100)
    while True:
        number = get_valid_input(1, 100)
        if number == actual_number:
            print(f"Congratulations! You've guessed the number {actual_number} with a score of {scorer.get_score()}.")
            break
        else:
            print("Wrong guess. Try again.")
            scorer.update_score(-10)
            if scorer.get_score() <= 0:
                print("Game over! You've run out of score.")
                break


if __name__ == "__main__":
    main()