#FUNCTIONS
#def (name) is a keyword used in writing a function
def say_hi():
    #the code that goes inside the function must be indented
    print("Hey bruh")

#the code in a function will not run until you call it by doing what was done below..you piece of shit
say_hi() 

#you can create a function for future use and then work other codes before calling the function..little bitch
def loser():
    print("What's up punk")

print("Hey bruh")
loser()
print("bruh, tf")

#giving functions parameters/information
def sayhi(name):
    print("What's up "+ name)
sayhi("Jerry")
sayhi("Joel")
#the name is the parameter

#You can use more than one parameters

def nameage(name, age):
    print("What's up "+ name + ", " + age + " year old programmer")
nameage("Jerry" , "19")
nameage("Joel", "18")


#RETURN KEYWORD...LINE 224 to LINE 235

#this gives information about how a function goes
def cube(num):
    num*num*num #this function must cube the number
print(cube(3))
#it prints out none so in this case when you use the return function, python will execute it

def cube(num):
   return num*num*num
print(cube(3))
#in short it is used to get info from a function, return breaks a function therefore any code after the return code in a function will not be read
