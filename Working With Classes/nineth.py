#You can use import to add a library like random,
#math and many more even files such as first

#INHERITANCE
#used to replace copying and pasting every function in a class to another class
#example
from shootingguard import shooting_guard

class point_guard(shooting_guard):
    def dribbles(self):        
        print("Dribbles The Ball")

from nineth import point_guard

myPlayer = point_guard()
myPlayer.passes()
myPlayer.dribbles()
myPlayer.drives()
myPlayer = shooting_guard()
myPlayer.passes()
myPlayer.shoots()
myPlayer.drives()




#notice that you did not have to type all the 
#sooting guard skills in the point guard class