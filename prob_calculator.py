import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.removes=[]
        
        self.contents=[]
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)
               
    def draw(self, number):
        contents_copy = self.contents
        if number > len(contents_copy):
            number = len(contents_copy)
        removed_balls = []
        for i in range(number):
            position = random.randint(0, len(contents_copy) - 1)
            removed_balls.append(contents_copy.pop(position))
        return removed_balls
         
def experiment(hat,expected_balls,num_balls_drawn,num_experiments):
    m=0
    expected=[]
    for keys,val in zip(expected_balls.keys(),expected_balls.values()):
        for i in range(val):
                expected.append(keys)
    for i in range(num_experiments):
        exp=hat.draw(num_balls_drawn)
        check_balls = all( item in exp for item in expected)      
        if check_balls:
            m+=1
    return m/num_experiments