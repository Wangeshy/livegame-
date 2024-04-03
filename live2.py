def welcome(name):
    print('Hello',name,'and welcome to the World of Games(WoG),\nHere you can find many cool games to play')

welcome(str(input('Please input your name')))



def load_game():
    game_choice = {1: 'Memory game - a sequence of numbers will appear for 1 second and you have to guess it back',
         2: 'Guess Game - guess a number and see if you choose like the computer',
         3: 'Currency Roulette - try and guess the value of a random amount of USD in ILS'}

    print(game_choice[n])

n = int(input('Choose the game to play'))

load_game()



