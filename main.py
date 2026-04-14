import random  # Importing random module to generate secret numbers


class NumberGuessingGame:
    def __init__(self,player_name):
        self.player_name=player_name.upper()
        self.levels={
            "easy":(1, 20, 5),
            "medium":(1, 50, 7),
            "hard":(1, 100, 10)
        }
    def choose_level(self):
        print("\nChoose Difficulty Level:")
        print("1.Easy(1-20, 5 attempts)")
        print("2.Medium(1-50, 7 attempts)")
        print("3.Hard(1-100, 10 attempts)")
        while True:
            choice=input("Choose Level (easy/medium/hard):").lower().strip()
            if choice in self.levels:
                return choice
            else:
                print("⚠️ Invalid choice! Please select: easy,medium,or hard.")
    def play(self):
        level=self.choose_level()
        min_num, max_num, max_attempts=self.levels[level]
        secret_number=random.randint(min_num, max_num)
        attempts=0
        print(f"\nWelcome {self.player_name} to Number Guessing Game!")
        print(f"Level: {level.upper()}")
        print(f"Guess a number between {min_num}-{max_num}")
        print(f"You have {max_attempts} attempts. Good luck! 🍀")
        
        while attempts < max_attempts:
            try:
                # Taking input from the user and converting to integer
                guess=int(input("Enter your guess: "))
            except ValueError:
                # Error handling for non-numeric inputs
                print("⚠️ Please enter a valid number")
                continue
            if guess < min_num or guess > max_num:
                print(f"Out of range! Choose between {min_num}-{max_num}")
                continue
            attempts +=1 # Incrementing attempts count
            remaining_attempts = max_attempts - attempts
            
            # Comparison Logic
            if guess < secret_number:
                print(f"📉 Too Low! ({remaining_attempts} attempts left)")
            elif guess > secret_number:
                print(f"📈 Too High! ({remaining_attempts} attempts left)")
            else:
                # Winning condition
                print(f"🎉 Congratulations {self.player_name}!")
                print(f"You guessed it in {attempts} attempts on {level.upper()} level.")
                return attempts
            
        print(f"\n💀 Game Over! The number was {secret_number}")
        return None

def main():
    name=input("Enter your name: ")
    best_score=None
    
    while True:
        # Creating a new instance of the game
        game=NumberGuessingGame(name)
        result=game.play()
        if result is not None:
            if best_score is None or result < best_score:
                best_score=result
                print(f"New Best Score: {best_score} attempts!")
        
        # Asking user for a replay
        again=input("\nDo you want to play again? (yes/no): ").lower().strip()
        if again != "yes":
            print("Thanks for Playing!\nGoodbye 👋.")
            break

# Standard Python boilerplate to run the script
if __name__ =="__main__":
    main()
