class student:
    def __init__(self, name, major, gpa, is_on_probation): #initialize function, helps map out certain attributes the class should have
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation
    #Using Functions In Class
    def on_honor_roll(self):
        if self.gpa >=3.5:
            return True
        else:
            return False

class school:
    def __init__(self, name1, rank, population):
        self.name = name1
        self.rank = rank
        self.population = population

