secret_word = "Giraffe"
guess = "" #user's guess
guess_count = 0 #number of guesses
guess_limit = 3 #max number of guesses
out_of_guesses = False #boolean saying the person has guesses at the start of th game

while guess != secret_word and not(out_of_guesses): #means while user's guess is not the same as secret word and user is not out of guesses
    if guess_count < guess_limit: #if the number of guesses is < the max number of guesses
        guess = input("Enter guess:") #keep guessing
        guess_count += 1 #every attempt increases the guess
    else:
        out_of_guesses = True #until the number of guesses = max number of guesses

if out_of_guesses: #if you are out of guesses you lose else you win
    print("You Lose")
else:
    print("You win")






