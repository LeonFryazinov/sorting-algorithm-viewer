import sorting_helper
import turtle

class insertion_sort(sorting_helper.sorting_algorithm): 
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)
        #self.step_delay = 0.1
        self.insert_target = 0
        self.remaining = self.unsorted_list.copy()[1:]
        self.num_list.clear()
        self.num_list.append(self.unsorted_list[0])
    def step(self):
        if len(self.remaining) == 0:
            self.solved = True
            self.transfer_list_to_buffer(self.num_list, green_list=list(range(len(self.unsorted_list))))
            return
            
        if self.remaining[0] < self.num_list[self.insert_target]:
            self.num_list.insert(self.insert_target,self.remaining[0])
            del self.remaining[0]
            self.insert_target = 0
        elif self.insert_target == len(self.num_list)-1:
            self.num_list.append(self.remaining[0])
            del self.remaining[0]
            self.insert_target = 0
        else:
            self.insert_target += 1
        
        #print(f"{self.num_list.copy()}   {self.remaining.copy()}")
        
        display_list = self.num_list.copy() + self.remaining.copy()
        self.transfer_list_to_buffer(display_list, red_list=[self.insert_target,len(self.num_list)])