import random
import turtle
import sorting_helper
       
class bogo_sort(sorting_helper.sorting_algorithm):
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)
        self.red_list = sorting_helper.create_acsending_list(len(self.num_list))

    def step(self):
        if self.check_sorted():
            self.solved = True
            self.transfer_list_to_buffer(self.num_list,green_list=self.red_list)
        else:
            random.shuffle(self.num_list)
            #print("list randomized")
            self.transfer_list_to_buffer(self.num_list,red_list=self.red_list)
class miracle_sort(sorting_helper.sorting_algorithm):
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)
        self.red_list = sorting_helper.create_acsending_list(len(self.num_list))

    def step(self):
        if self.check_sorted():
            self.solved = True
            self.transfer_list_to_buffer(self.num_list,green_list=self.red_list)
        self.transfer_list_to_buffer(self.num_list,red_list=self.red_list)
class stalin_sort(sorting_helper.sorting_algorithm): #the well loved stalin sort
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)
        self.pointer = 1
        self.green_list = [0]
        self.step_delay = 0.5

    def step(self):
        
        if self.pointer == self.list_len:
            self.solved = True
            return


        if self.num_list[self.pointer] < self.num_list[self.pointer-1]: # if the next number is smaller than the last, then delete if from the list.

            del self.num_list[self.pointer]
             
            self.recalculate_list_attributes() # recalculate the width of the visual bars
        else:
            self.green_list.append(self.pointer)
            self.pointer += 1

        self.transfer_list_to_buffer(self.num_list,green_list=self.green_list,red_list=[self.pointer])        
