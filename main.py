import turtle
import random
import time
from enum import Enum
import sorting_helper
import winsound

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
        self.solved_amount = 0

    def create_decsending_list(self,total_items:int,items:int):
        decsend_list = []
        for i in range(items):
            decsend_list.append(total_items-i)
        
        return decsend_list
        
    
    def create_acsending_list(self,num):
        returned_list = []
        for i in range(num):
            returned_list.append(i)
        
        return returned_list


    def step(self):
        if self.list_len < 2:
            self.solved = True
            if self.list_len == 1:
                self.transfer_list_to_buffer(self.num_list,green_list=[0])
                return


        if self.pointer == (self.list_len-1)-self.solved_amount:
            self.solved_amount += 1
            if self.solved_amount == self.list_len-1:
                print("solved")
                self.solved = True
                green_list = self.create_acsending_list(self.list_len)
                self.transfer_list_to_buffer(self.num_list,green_list=green_list,red_list=[self.pointer,self.pointer+1])
                return
            
            self.pointer = 0
        
        if self.num_list[self.pointer] > self.num_list[self.pointer+1]:
            temp = self.num_list[self.pointer]
            self.num_list[self.pointer] = self.num_list[self.pointer+1]
            self.num_list[self.pointer+1] = temp
        
        green_list = self.create_decsending_list(self.list_len-1,self.solved_amount)


        self.transfer_list_to_buffer(self.num_list,green_list=green_list,red_list=[self.pointer,self.pointer+1])
        self.pointer += 1
        self.step_count += 1
        
class stalin_sort(sorting_helper.sorting_algorithm):
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)
        self.pointer = 1
        self.green_list = [0]
        self.step_delay = 0.5

    def step(self):
        global gun_sound
        if self.pointer == self.list_len:
            self.solved = True
            return


        if self.num_list[self.pointer] < self.num_list[self.pointer-1]:

            del self.num_list[self.pointer]
            
            self.recalculate_list_attributes()
        else:
            self.green_list.append(self.pointer)
            self.pointer += 1
        

        self.transfer_list_to_buffer(self.num_list,green_list=self.green_list,red_list=[self.pointer])
        




        

not_true = False


submit_list = []

for i in range(20):
    submit_list.append(random.randint(1,100))

test = stalin_sort(submit_list,t,screen)

last_frame_time = time.time()
time_sum = 0.0
non_reset_time_sum = 0.0
while True:
    current_time = time.time()
    dt = current_time - last_frame_time
    last_frame_time = current_time
    
    time_sum += dt
    non_reset_time_sum += dt

    

    if time_sum > test.step_delay:
        #print("frame update")
        test.process()
        time_sum = 0.0
        time.sleep(0.001)


    if test.solved:
        
        break

screen.mainloop()