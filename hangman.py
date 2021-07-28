#--------- MODULES ---------#
import random
#--------- MODULES ---------#

#--------- MAIN CODE ---------#
word = random.choice(['flash','thor','batman','superman','spiderman','ironman','black panther'])
valid = 'abcdefghijklmnopqrstuvwxyz '
letter_by_letter = ''
turns = 10

while len(word) > 0:
    dash = ''

    for letter in word:
        if letter in letter_by_letter:
            dash += letter
        else:
            dash += '_ '

    if dash == word:
        print("Congratulation!!!")
        print("You Win!!!")
        break

    print("Please Try to guess the word: "+dash)
    guess = input()

    if guess in valid:
        letter_by_letter += guess
    else:
        print("Invalid Input")
        guess = input()

    if guess not in word:
            turns -= 1

            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("   \ O /|   ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("   \ O_|/   ")
                print("     |      ")
                print("    / \     ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("     O_|    ")
                print("    /|\      ")
                print("    / \     ")

    if turns == 0:
        print("You Lost!!!")
        print("The word is", word)
        break

#--------- MAIN CODE ---------#