#2D LISTS AND NESTED LOOPS...LINE 286 to 300
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#2d list above, how to access individual elements
print(number_grid[0][0]) #the first[] is row index, the second is column index to access 1

#nested for loop
for row in number_grid:
    for col in row:
        print(col)
#prints values as separate elements
