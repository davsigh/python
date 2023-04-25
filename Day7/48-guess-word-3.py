import random
words = ["hellooo", "round", "army"]
choosen_word = random.choice(words)
print(choosen_word)

letter = len(choosen_word)
print(letter)

display = []
for a in range(letter):
    display += "_"
print(display)
for a in range(letter):
    guess = input("\nGuess a letter ")
    for position in range(letter):
        #print(position)
        letter_store = choosen_word[position]
        #print(letter)
        if letter_store == guess:
            display[position] = letter_store
            print(display)
        else:
            print("Ans=wer is wrong")
            print(display)
print(display)   
