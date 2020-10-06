import string
import random
import requests

class Game():
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        check_word = requests.get(f'https://wagon-dictionary.herokuapp.com/{word}')
        if check_word.status_code == 200:
            return check_word.json().get('found')
        return True
