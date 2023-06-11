from math import *
#math is a module...

import os



#PYTHON ABSOLUTE BASICS...LINE 7 to LINE 27

# HELLO WORLD
print("Hello World")

#Drawing Shapes
print("  /|")
print(" / |")
print("/__|")


#Variables and Data Types
name = "Adam";
age = "18";
print("There was a dude who looked like me called " + name +",");
print("he was "+ age + " years old.");
print(name +" really loved his looks,");
print("but didn't like being "+ age +".");


#integers(int) are whole numbers
#floats(float) are numbers with decimal points
#strings(str) are characters



#WORKING WITH STRINGS....LINE 31 to LINE 70

#Uppercases And Lowercases
phrase = "I'm The Best";
print(phrase.upper());
sentence = "THE ONLY ONE WHO CAN BEAT ME IS ME";
print(sentence.lower())

#Checking if it is upper or lowercase
phrase = "I'm The Best";
print(phrase.isupper());
sentence = "THE ONLY ONE WHO CAN BEAT ME IS ME";
print(sentence.islower())

#Merging the two sets above 
#the two will produce true because the first is checking to see if it is UC which it and the second is checking to se if it is LC which also is
phrase = "I'm The Best";
print(phrase.upper().isupper());
sentence = "THE ONLY ONE WHO CAN BEAT ME IS ME";
print(sentence.lower().islower());

#Checking Length/ how many characters are in a phrase
sentence2 = "ANONYMOUSX44";
print(len(sentence2));

#this is me testing something out, don't mind me lol
phrase2 = input("Your name: ");
print(len(phrase2));

#finding a character in a string and note its starts with 0
line = "BATMAN"
print(line[5]) #this will print N

#using .index, tells us where a specific character is located in a string, vice versa of the previous example
line = "BATMAN"
print(line.index("M"))
line = "BATMAN"
print(line.index("MA"))

#using replace, to replace the item in a variable
line = "BATMAN"
print(line.replace("BATMAN", "IRONMAN"))


#WORKING WITH NUMBERS....LINE 75 to LINE 111

#just printing out the number
print(2)
print(2.078)
print(-28.4)
print(-5+85.05)
print(-5*85.05)
print(-5/85.05)
print(-5-85.05)
#changing order of operation
print(3 * 4 + 5) # will print 17
print(3 * (4 + 5)) #will print 27
#using mod
print(10%3) #will print 1...you would have know this if you paid more attention in class dummy

#this next example is for variables but you ain't dumb so I'm skipping

#converting numbers into strings
num1 = 5
print(str(num1) + " is my favourite number")

#functions
num1 = -5.2
print(abs(num1)) #abs for absolute value
print(pow(num1, 3)) #pow for power...this means -5 exponent 3
print(max(num1, 8)) #max for printing the largest of the 2 numbers
print(min(num1, 8)) #min for printing the smallest of the 2 numbers
print(round(num1)) #round for rounding up the number

#to get the rest of the math functions you need to import them with this code: from math import * 
print(floor(num1)) #floor for removing the decimal from the number
print(ceil(num1)) #ceil for rounding up the number to the next number
print(sqrt(4)) #sqrt for square root of the number


#Using input we both know you know how to use this so I'm not gonna give any examples



#WORKING WITH LISTS....LINE 118 to 178

friends = ["Kelvin", "Enoch", "Sampah", "Martin", "Festus"] #you can put a str, bool, int in the list
print(friends)

#accessing elements in the list using their index which also starts with 
print(friends[3]) #will print Martin
print(friends[-1]) #will print Festus, negative starts counting from the back

#selecting elements and selecting a range
print(friends[1:]) #will select elements from Enoch to Festus
print(friends[1:4]) #will select Enoch to Martin 

#making mods
friends[2]= "Jalal"
print(friends[2])

#list functions

friends = ["Kelvin", "Enoch", "Sampah", "Martin", "Festus"]
numbers = [4, 5, 7, 1, 2, 9, 0, 6 ]
friends.extend(numbers) #extend function joins lists
print(friends)

friends1 = ["Kelvin", "Enoch", "Sampah", "Martin", "Festus"]
friends1.append("Desire") #append adds elements to the end of the list
print(friends1)

friends2 = ["Kelvin", "Enoch", "Sampah", "Martin", "Festus"]
friends2.insert(1,"Hajara") #insert adds a value to the list at the specified index but doesnt clear anything only moves them
print(friends2)

friends3 = ["Kelvin", "Enoch", "Sampah", "Martin", "Festus"]
friends3.remove("Sampah") #removes an element from the list
print(friends3)

friends4 = ["Kelvin", "Enoch", "Sampah", "Martin", "Festus"]
friends4.clear() #resets the list
print(friends4)

friends5 = ["Kelvin", "Enoch", "Sampah", "Martin", "Festus"]
friends5.pop() #removes the last element
print(friends5)

friends6 = ["Kelvin", "Enoch", "Sampah", "Martin", "Festus"]
print(friends6.index("Martin"))

friends7 = ["Kelvin", "Enoch", "Enoch", "Sampah", "Martin", "Festus"]
print(friends7.count("Enoch")) #tells how many elements of the mentioned are present

friends8 = ["Kelvin", "Enoch", "Enoch", "Sampah", "Martin", "Festus"]
friends8.sort() #arranges the list in ascending order 
print(friends8)

friends9 = ["Kelvin", "Enoch", "Enoch", "Sampah", "Martin", "Festus"]
friends9.reverse() #reverses the list 
print(friends9)

friends8 = ["Kelvin", "Enoch", "Enoch", "Sampah", "Martin", "Festus"]
friends9 = friends8.copy() #copy 
print(friends8)


#TUPLES....LINE 181 to 189
#can store multiple pieces of info, cannot be changed or modified, WYSIWYG

coordinates = (4, 5)
print(coordinates[0]) #will print out 4

#creating a list of tuples
coordinates1 = [(4, 5), (6, 7), (8, 9)]
print(coordinates1)




#EXPONENT FUNCTION
#this ^ means exponent

def expo(base, power): #creating a function to raise any number to any power
    result = 1
    for index in range(power):
        result = result * base
    return result
print(expo(5, 4))






# TRY EXCEPT
#used to test codes to prevent breaking when it encounters an error
try:
     number = int(input("Enter a number: "))
     print(number)
except:
     print("Invalid Input")
#this will tell the user if his input is wrong or not, but then again this code will also break mistakes from the programmer
#you can create 2 except blocks
# you must always be specific with your errors
try:
    value = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid Input")
























