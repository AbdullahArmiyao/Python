#CLASS AND OBJECTS
#classes function the same way as in other languages

#Class has been set in student.py

#Using the class in any python file
from student import student
student1 = student("Abdullah", "Computer Science", 3.0, False)
print(student1.name, student1.gpa, student1.major)
print(student1.on_honor_roll())


from student import school
school1 = school("KNUST", 1099, 21000)
print(school1.name, school1.population, school1.rank)


