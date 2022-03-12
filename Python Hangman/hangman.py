import random
import string
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


def hangman():
    #fetch the valid word from word list
    word = get_valid_word(words)
    # print(word)
    # set() method makes a set of unique char in a word
    word_letters = set(word)
    
    # make a set of all uppercase alphabet
    alphabet = set(string.ascii_uppercase)
    
    # what user has guessed
    used_letters = set()
    
    lives = 5

    #getting user input
    while len(word_letters)>0 and lives>0:
        print(f'You have {lives} lives left!')
        #You have used these letters.. join attach list as string format
        print('You have used these letters: ', ' '.join(used_letters))
        # what current word is 
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives-=1
                print(f'{user_letter} is not in the word!')
        
        elif user_letter in used_letters:
            print(f'you have already used it')

        else:
            print(f'Invalid input! Try again')
    if lives==0:
        print(f'Sorry! You died! The secret word was {word}')
    else:
        print(f'You guessed the word {word} !!')

hangman() 