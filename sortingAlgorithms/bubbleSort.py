import turtle
import sorting_helper

class bubble_sort(sorting_helper.sorting_algorithm): 
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)
        self.pointer = 0 # a variable that holds the index of the item being compared
        self.solved_amount = 0 # bubble sort ensures that the final n numbers are solved (where n is the current pass) so they dont have to be itterated

    def create_decsending_list(self,total_items:int,items:int): # a function for getting the final n numbers for easy colouring 
        decsend_list = []
        for i in range(items):
            decsend_list.append(total_items-i)
        
        return decsend_list
        
    
    


    def step(self):
        if self.list_len < 2: # if the list has less than 2 items, it is already solved, instantly set solved to true
            self.solved = True
            if self.list_len == 1:
                self.transfer_list_to_buffer(self.num_list,green_list=[0]) # display the solved list
                return


        if self.pointer == (self.list_len-1)-self.solved_amount: #returns the pointer back to the start if it has reached the end of the list.
            self.solved_amount += 1
            if self.solved_amount == self.list_len-1: # if the amount of solved numbers = the amount of numbers in list, then it is solved
                #print("solved")
                self.solved = True
                green_list = sorting_helper.create_acsending_list(self.list_len)
                self.transfer_list_to_buffer(self.num_list,green_list=green_list)
                return
            
            self.pointer = 0
        
        if self.num_list[self.pointer] > self.num_list[self.pointer+1]: # if l(s) > l(s+1) then they have to be swapped
            temp = self.num_list[self.pointer]
            self.num_list[self.pointer] = self.num_list[self.pointer+1]
            self.num_list[self.pointer+1] = temp
        
        green_list = self.create_decsending_list(self.list_len-1,self.solved_amount) # the list of indexes that have been solved, then display that


        self.transfer_list_to_buffer(self.num_list,green_list=green_list,red_list=[self.pointer,self.pointer+1]) # function that displays the list
        
        self.pointer += 1