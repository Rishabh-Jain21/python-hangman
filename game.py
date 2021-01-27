import random
from hangman_life import game_name
from hangman_life import lives
from hangman_guessing import guess_list


guessing_word = random.choice(guess_list).lower()
word_letters_len = len(guessing_word)

game_over = False
tries = 6


print(game_name)
#print(f'The word you guessed is {guessing_word}')

result = ["_"]*word_letters_len

print(result)
while not game_over:
    user_guessing = input("Guess a letter: ")
    if user_guessing in result:
        print(f'The letter you have guessed is {user_guessing}')

    for position in range(word_letters_len):
        letter = guessing_word[position]
        if letter == user_guessing:
            result[position] = letter

    if user_guessing not in guessing_word:
        print(
            f'You guessed {user_guessing}. This is not in word.You lose a try')
        tries -= 1
        if tries == 0:
            print("Game over,You lose game try again letter")
            print(f'The word was {guessing_word}')
            game_over = True

    print(f"{' '.join(result)}")
    if "_" not in result:
        game_over = True
        print('You are a winner,Congratulations')

    print(lives[tries])
