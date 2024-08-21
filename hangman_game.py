import random

word_list = ["python", "hangman", "challenge", "programming", "developer"]

def choose_word(word_list):
    return random.choice(word_list).upper()

def hangman():
    word = choose_word(word_list)
    word_letters = set(word)
    used_letters = set()
    lives = 6

    while word_letters and lives:
        print(f'Lives: {lives}, Used letters: {" ".join(used_letters)}')
        current_word = [letter if letter in used_letters else '-' for letter in word]
        print('Word: ', ' '.join(current_word))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in word_letters:
            word_letters.remove(user_letter)
        elif user_letter not in used_letters:
            lives -= 1
            print('Wrong guess!')
        
        used_letters.add(user_letter)

    if lives:
        print(f'Congratulations! You guessed the word: {word}')
    else:
        print(f'Sorry, you lost. The word was: {word}')

if __name__ == "__main__":
    hangman()
