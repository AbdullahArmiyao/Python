#READING AND WRITING FILES.....LINE 338 to 346
# for reading and writing non python file
first = open("C:\Users\DOLLA\OneDrive\Desktop\C#\FIRST.cs", "r") #to open the file the mode comes after file name,and make sure to close file after use
#r is read, r+ is read and write, a is append, w is write
print(first.readable())
print(first.read())
print(first.readline())
print(first.readlines())
first.close()
