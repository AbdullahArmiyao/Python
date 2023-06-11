#CREATING A TRANSLATOR
def translate(phrase): #create function
    translation = "" #give the user input
    for letter in phrase: #for the letter in the user value
        if letter in "aeiouAEIOU": #if it is a noun
            if letter.isupper: #if it is a capital letter
                translation = translation + "G"
            else:
                translation = translation + "g"
        else: #if it is a consonant
            translation = translation + letter #just print that same letter
    return translation #give back the translated word
print(translate(input("Enter a phrase: ")))
