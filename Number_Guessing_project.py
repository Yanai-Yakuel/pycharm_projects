from random import randint


EASY_LEVEL_TURNS = 15
MEDIUM_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



def check_answer(user_guess, actual_answer, turns):
    if user_guess > actual_answer:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {actual_answer}")



def set_difficulty():
    level = input("set the difficulty. Type 'easy' 'medium' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "medium":
        return MEDIUM_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)


    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")




game()