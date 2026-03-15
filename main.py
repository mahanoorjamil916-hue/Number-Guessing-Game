import random  # Importing random module to generate secret numbers


class NumberGuessingGame:
    def __init__(self,player_name):
        self.player_name=player_name.upper()
        self.secret_number=random.randint(1,50) # Computer picks a number between 1-50
        self.attempts=0 # Tracking the number of guesses
    def play(self):
        print(f"\nWelcome {self.player_name} to number Guessing Game!")
        print("Guess a number between 1-50:")
        
        while True:
            try:
                # Taking input from the user and converting to integer
                guess=int(input("Enter your guess: "))
            except ValueError:
                # Error handling for non-numeric inputs
                print("⚠️ Please enter a valid number")
                continue
            self.attempts +=1 # Incrementing attempts count
            
            # Comparison Logic
            if guess < self.secret_number:
                print("📉 Too Low")
            elif guess > self.secret_number:
                print("📈 Too High")
            else:
                # Winning condition
                print(f"🎉 Congratulations {self.player_name}!\nYou guessed it in {self.attempts} attempts.")
                break
def main():
    name=input("Enter your name: ")
    
    while True:
        # Creating a new instance of the game
        game=NumberGuessingGame(name)
        game.play()
        
        # Asking user for a replay
        again=input("\nDo you want to play again? (yes/no): ").lower()
        if again !="yes":
            print("Thanks for Playing!\nGoodbye.")
            break

# Standard Python boilerplate to run the script
if __name__ =="__main__":
    main()
