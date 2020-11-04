import random

print('H A N G M A N')
option = ""
while option != "exit":
    option = input("Type \"play\" to play the game, \"exit\" to quit:")
    if option == "play":
        words = 'python', 'java', 'kotlin', 'javascript'
        random_word = random.choice(words)
        word = '-'.split() * len(random_word)
        letters = set(random_word)
        repeated_words = []
        tries = 0
        while tries < 8:
            if len(letters) == 0:
                print(f"\n{''.join(word)}")
                break
            x = input(f"\n{''.join(word)}\nInput a letter: ")
            if len(x) == 1:
                if x.islower():
                    if x in letters:
                        letters.discard(x)
                        repeated_words.append(x)
                        for n in range(len(random_word)):
                            if random_word[n] == x:
                                word[n] = x
                    elif x in repeated_words:
                        print("You've already guessed this letter")
                    else:
                        repeated_words.append(x)
                        print("That letter doesn't appear in the word")
                        tries += 1
                else:
                    print("Please enter a lowercase English letter")
            else:
                print("You should input a single letter")

        if tries < 8:
            print("You guessed the word!\nYou survived!")
        else:
            print("You lost!")

