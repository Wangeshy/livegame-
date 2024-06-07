import random
import time

class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def is_list_equal(self, list1, list2):
        return list1 == list2
    def play(self):
        print("Welcome to the Memory Game!")
        print("You will be shown a sequence of numbers for 0.7 seconds.")
        print("Try to remember them and enter the same sequence afterward.")
        generated_sequence = self.generate_sequence()
        print(generated_sequence, end='', flush=True)  # Print without newline and flush the buffer
        time.sleep(0.9)
        print('\r' + ' ' * len(generated_sequence) + '\r', end='', flush=True)  # Overwrite the printed text
        user_sequence = self.get_list_from_user()
        print("Your sequence:", user_sequence)
        print("Generated sequence:", generated_sequence)
        if self.is_list_equal(user_sequence, generated_sequence):
            print("Congratulations! You won!")
            return True
        else:
            print("Sorry, you lost. Better luck next time!")
            return False

    def generate_sequence(self):
        # Manually specify the sequence here
        return [random.randint(1, 101) for _ in range(self.difficulty)] # Example sequence
        generated_sequence = self.generate_sequence()


    def get_list_from_user(self):

        print("Now enter the numbers you remember:")
        user_sequence = []
        for _ in range(self.difficulty):
            while True:
                try:
                    number = int(input("Enter a number: "))
                    if 1 <= number <= 101:
                        user_sequence.append(number)
                        break
                    else:
                        print("Please enter a number between 1 and 101.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        return user_sequence




# Example usage:
def main():
    while True:
        difficulty = input('Choose the level of difficulty: ')
        try:
            difficulty = int(difficulty)
            if 1 <= difficulty <= 5:
                game = GuessGame(difficulty)
                game.play()
                break  # Exit the loop if a valid difficulty is entered
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    

if __name__ == "__main__":
    main()
