import random

def generate_secret_number():
    return random.randint(1000, 9999)

def evaluate_guess(secret_number, guess):
    secret_str = str(secret_number)
    guess_str = str(guess)

    if secret_str == guess_str:
        return "Correct!"

    hints = []
    for i in range(4):
        if guess_str[i] == secret_str[i]:
            hints.append("circle")
        elif guess_str[i] in secret_str:
            hints.append("x")
    
    if hints:
        return " ".join(hints)
    else:
        return "0"

def play_game():
    secret_number = generate_secret_number()
    attempts = 0

    print("Welcome to Guess the Number!")

    while True:
        guess = input("Enter your 4-digit guess (or 'quit' to exit): ")
        
        if guess.lower() == "quit":
            break
        
        try:
            guess = int(guess)
            if 1000 <= guess <= 9999:
                attempts += 1
                result = evaluate_guess(secret_number, guess)
                print(f"Result: {result}")
                if result == "Correct!":
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
            else:
                print("Please enter a valid 4-digit number.")
        except ValueError:
            print("Invalid input. Please enter a 4-digit number.")

if __name__ == '__main__':
    play_game()
