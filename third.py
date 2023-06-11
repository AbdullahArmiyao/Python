#DICTIONARIES
monthConversions = {
    "Jan" : "January",
    "Feb" : "February",
    "Mar" : "March",
} #we use curly brackets for dictionaries

#to access an element in it
print(monthConversions["Jan"]) #this will print out January
#also you can use the get function
print(monthConversions.get("Mar")) #will print out March
#the keys do not necessarily have to be strings
