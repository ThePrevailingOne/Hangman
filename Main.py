from time import sleep
from random import randint
import csv

def readcsv(csvfilename):
    if not csvfilename:
        return 'csv file name not valid'

    with open(csvfilename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter = ',')
        word_list = []
        for row in csv_reader:
            word_list.append(row)

        return word_list

class Player:
    def __init__(self, name):
        self.name = name
        self.lives = 5
        self.score = 0

    def get_name(self):
        return self.name

    def get_lives(self):
        return self.lives

    def reduce_lives(self):
        self.lives -= 1

    def reset_lives(self):
        self.lives = 5

    def add_score(self):
        self.score += 1

    def get_score(self):
        return self.score

def game_time(player, word, hint):
    def blanks():
        blank = ""
        for char in word:
            if char in chars_guessed:
                blank += char
                continue

            if char == ' ':
                blank += ' '
                continue

            blank += "_"

        return blank

    valid_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                    'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    chars_guessed = ()
    while blanks() != word:
        print("Guess this word:  ", ' '.join(blanks()))
        print(f"Remaining lives: {player.get_lives()}, hint: {hint}")
        guess = input('Enter your guess: ')
        guess = guess.lower()
        
        if not guess:
            print("No input entered. Please enter a character.")
            continue

        if guess == 'skip':
            return 'Skipping game...'

        if len(guess) > 1:
            print("Please enter just one character at a time.")
            continue

        if guess not in valid_chars:
            print("Please enter just latin characters (a-z).")
            continue

        if guess in chars_guessed:
            print("You already guessed this character.")
            continue

        if guess not in word:
            player.reduce_lives()

        if player.get_lives() == 0:
            return f"Game lost... (answer: {word})"

        chars_guessed += (guess,)

    player.add_score()
    print(f"You guessed it, it's {word}.")
    return f"Game winned!! Current score: {player.get_score()}"



def main():
    input("Welcome to BC Hangman!!")
    input("Before getting into the game, there's a few rule:")
    input("1. First, you can only input latin characters, and just one character per guess.")
    input("2. Play until you guess the word, if you don't feel like finishing the game, type 'quit'.")
    input("3. Finally, Have fun while playing!! :)")

    word_list = readcsv('words.txt')
    new_player_name = input('Do tell us your name: ')
    new_player = Player(new_player_name)
    still_playing = True

    while still_playing and word_list:
        word_index = randint(0, len(word_list)-1)
        random_word = word_list[word_index]

        print(game_time(new_player, *random_word))

        while True:
            again = input("Would you like to continue? (y/n) ")
            again = again.lower()

            if again == 'y':
                still_playing = True
                break

            if again == 'n':
                still_playing = False
                break

            print("please enter either 'n' or 'y'.")

        word_list.pop(word_index)

    print(f"Congratulations {new_player.get_name()}, your score is {new_player.get_score()}.")
    print("See you next time :)")


main()
