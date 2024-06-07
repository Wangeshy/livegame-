import random
import requests

class CurrencyGame:
    def __init__(self, difficulty):
            self.difficulty = difficulty

    def get_money_interval(self):
        # Get the current exchange rate from USD to ILS using the currency API
        response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
        data = response.json()
        exchange_rate = data["rates"]["ILS"]
        t = random.randint(1, 100)
        # Generate an interval based on difficulty and exchange rate
        try:
            if 1 <= t <= 100:
                t = random.randint(1, 100)
                lower_bound = t - (5 - self.difficulty)
                upper_bound = t + (5 - self.difficulty)
                print("The generated USD value is",t)
                return lower_bound * exchange_rate, upper_bound * exchange_rate
            else:
               t = random.randint(1, 100)
        except ValueError:
             print("Invalid input. Please enter a valid number.")
        return lower_bound * exchange_rate, upper_bound * exchange_rate
    def get_guess_from_user(self):
        guess = float(input("Enter your guess for the value in ILS: "))
        return guess

    def play(self):
        print("Welcome to the Currency Game!")
        lower_bound, upper_bound = self.get_money_interval()
        print(f"Guess the value of the generated number in ILS. It's between {lower_bound} and {upper_bound}.")
        t = random.randint(1, 100)
        user_guess = self.get_guess_from_user()
        if t == user_guess:
            print("Congratulations! Your guess is correct.")
            return True
        else:
            print("Sorry, your guess is incorrect. The correct value was between the interval.")
            return False

# Example usage:
def main():
    while True:
        difficulty = input('Choose the level of difficulty: ')
        try:
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:
                game = CurrencyGame(difficulty)
                game.play()

                break  # Exit the loop if a valid difficulty is entered
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    


if __name__ == "__main__":
    main()

