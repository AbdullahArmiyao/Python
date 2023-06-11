#my simple calculator


#FOR THE USER TO INPUT THE MATH OPERATION WANTS TO PERFORM
x = input("Value1: ")
y = input("operation: ")
z = input("Value2: ")

#SO THAT THE VALUES WON'T BE READ A STRINGS
x = float(x) 
z = float(z)

if y == "*":
    a = x * z
elif y == "+":
    a = x + z
elif y == "-":
    a = x - z
elif y == "/":
    a = x / z
elif y == "%":
    a = x % z

print()
print(a)  
   
#NOTE Indentation is very very important