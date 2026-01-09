import turtle
import random
from enum import Enum
import sorting_helper

class STATES(Enum):
    START = 0
    RUNNING = 1
    RUNNING_STEP = 2
    END = 3



state = STATES.START


screen = turtle.Screen()
t = turtle.Turtle()
#t.color("black", "lime")
t.ht()
t.pensize(2)
t.speed(0)
screen.tracer(0)

class bubble_sort(sorting_helper.sorting_algorithm):
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)
        self.pointer = 0
    def step(self):
        pass
        




submit_list = []

for i in range(100):
    submit_list.append(random.randint(1,50))

test = bubble_sort(submit_list,t,screen)

test.step()

screen.mainloop()