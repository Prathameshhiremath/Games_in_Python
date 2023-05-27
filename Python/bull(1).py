import random

class Game:
    def __init__(self):
        self.secret_word = self.get_secret_word()
        self.guesses = 0

    def play(self):
        print("Let's play Bulls and Cows!")
        while True:
            try:
                self.guesses += 1
                guess = self.get_guess()
                bulls, cows = self.evaluate_guess(guess)
                print(f"{bulls} bulls, {cows} cows")
                if bulls == 4:
                    print(f"Congratulations, you guessed the word in {self.guesses} guesses!")
                    break
            except ValueError:
                print("Your guess must be a 4-letter word. Please try again.")
            except KeyboardInterrupt:
                print("\nQuitting game...")
                break

    def get_secret_word(self):
        # Define a list of possible 4-letter words
        words = ["game", "time", "work", "home", "baby", "city", "idea", "life", "away", "word"]
        # Choose a random word from the list
        secret_word = random.choice(words)
        return secret_word

    def get_guess(self):
        # Prompt the user to enter their guess
        guess = input("Enter your guess (a 4-letter word): ")
        # Make sure the guess is a 4-letter word
        if len(guess) != 4:
            raise ValueError
        return guess

    def evaluate_guess(self, guess):
        bulls = 0
        cows = 0
        for i in range(len(guess)):
            if guess[i] == self.secret_word[i]:
                bulls += 1
            elif guess[i] in self.secret_word:
                cows += 1
        return bulls, cows

class MultiplayerGame(Game):
    def __init__(self):
        super().__init__()

    def get_secret_word(self):
        secret_word = input("Enter the secret word (a 4-letter word): ")
        while len(secret_word) != 4:
            secret_word = input("The secret word must be a 4-letter word. Please try again: ")
        return secret_word


    
    
    
    
    
    
    
    
