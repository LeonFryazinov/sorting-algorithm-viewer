import turtle
import random
import math
import time
from enum import Enum

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



def get_list_max(_list):
    maximum = -255
        for num in _list:
            if num > maximum:
                maximum = num
        return maximum

class sorting_algorithm:
    def __init__(self,unsorted_list,turt):
        self.unsorted_list = unsorted_list
        self.num_list = self.unsorted_list.copy()
        self.drawn_list_buffer = {}
        self.t = turt
        self.max_bar_len = 500 #in pixels
        self.max_val = get_list_max(self.unsorted_list)
    
    def send_num_to_buffer(self,num,idx):
        if self.drawn_list_buffer[idx] != None:
            print(f"overwritten value {self.drawn_list_buffer[idx]} at position {idx} in the list")
        self.drawn_list_buffer[idx] = num
    
    def draw_list(self):
        drawn_list = []
        for i in range(len(self.unsorted_list)):
            drawn_list.append(self.drawn_list_buffer[i])
    
    
    def draw_bar(self,num,idx):
        bar_len = int(round(float(num)/float(self.max_val) * self.max_bar_len))
        horiz_offset = int(round(float(idx)/float(len(self.unsorted_list)))) - 
        
        
        
    
    def step(self):
        print("no algorithm implemented")
    
    def check_sorted(self):
        checked_list = self.num_list
        for i in range(len(checked_list)-1):
            if checked_list[i] > checked_list[i+1]:
                return False
        
        return True



screen.mainloop()