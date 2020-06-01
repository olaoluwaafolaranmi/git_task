import random
import string
def hangman():
    secretwords = random.choice(["weird", "drive", "school", "lioness", "engineer","correction"])
    validletters = string.ascii_letters
    guesscount = 10
    guessmade = " "
    while True:
        main = " "
        for letter in secretwords:
            if letter in guessmade:
                main = main + letter

            else:
                main = main + "_" + " "

        if main == secretwords:
            print(main)
            print("you win ")
            break
        print("make your guess", main)
        guess = input()
        if guess in main:
            print("you already enetered that letter kindly enter another letter ")
        if guess in validletters:
            guessmade = guessmade + guess
        else:
            print("enter a valid letter ")
            guess = input()

        if guess not in secretwords:
            guesscount = guesscount - 1
            if guesscount == 9:
                print("9 turns left ")
                print("----------")
            if guesscount == 8:
                print("8 turns left ")
                print("----------")
                print("    o     ")
            if guesscount == 7:
                print("7 turns left ")
                print("----------")
                print("    o     ")
                print("    |     ")
            if guesscount == 6:
                print("6 turns left ")
                print("----------")
                print("    o     ")
                print("    |     ")
                print("   /      ")
            if guesscount == 5:
                print("5 turns left ")
                print("----------")
                print("    o     ")
                print("    |     ")
                print("   / \    ")
            if guesscount == 4:
                print("4 turns left ")
                print("----------")
                print("  \ o     ")
                print("    |     ")
                print("   / \    ")
            if guesscount == 3:
                print("3 turns left ")
                print("----------")
                print("   \o/    ")
                print("    |     ")
                print("   / \    ")
            if guesscount == 2:
                print("2 turns left ")
                print("----------")
                print("   \o/ |  ")
                print("    |     ")
                print("   / \    ")
            if guesscount == 1:
                print("1 turn left ")
                print("----------")
                print("   \o_|/ ")
                print("    |     ")
                print("   / \    ")
            if guesscount == 0:
                print("you lose ")
                print(username + " you let the kind man die ")
                print("out of turns ")
                print("----------")
                print("   o_| ")
                print("  /|\     ")
                print("  / \    ")
                break



username = input("enter your name ")
print("welcome " + username)
print(":::::::::::::::::::::::::::::")
print("Try to guess the word in less than 10 attempts ")
hangman()