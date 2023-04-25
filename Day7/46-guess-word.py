import random
words = ["hello", "round", "army"]
choosen_word = random.choice(words)
print(choosen_word)


letter = len(choosen_word)
print(letter)
for letter in choosen_word:
    guess = input("Guess a letter ")
    if guess in choosen_word:
        print("Right")
    else:
        print("wrong")
    