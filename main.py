import turtle
import random
import time
import math
from enum import Enum
import is_rearranged
import sorting_helper # custom script holding the parent class "sorting_algorithm"

import keyboard




class STATES(Enum): #states enum, for future graphical interface
    INIT_START = 0
    START = 1
    INIT_RUN = 2
    RUN = 3
    END = 4

class keyboard_listener:
    def __init__(self,listen) -> None:
        self.listen_list = listen
        self.held_down = []
        self.just_down = []
    
    def update(self) -> None:
        self.just_down.clear()
        for key in self.listen_list:
            if keyboard.is_pressed(key) and (not key in self.held_down):
                self.just_down.append(key)
                self.held_down.append(key)
            elif (not keyboard.is_pressed(key)) and (key in self.held_down):
                self.held_down.remove(key)
    def key_just_pressed(self,key) -> bool:
        if key in self.just_down:
            return True
        else:
            return False


state = STATES.INIT_START


#init turtle
screen = turtle.Screen()
t = turtle.Turtle()
screen.screensize(600, 400, "lightblue")
#t.color("black", "lime")
t.ht()
t.pensize(2)
t.speed(0)
screen.tracer(0)





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
class merge_sort(sorting_helper.sorting_algorithm):
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)
        self.job_pointer = 0
        self.job_list = [(0,self.list_len,0)]
        self.currently_solving = False
        self.solve_list_a = []
        self.solve_list_b = []
        self.solved_temp = []
    def get_job_list(self,job:tuple): #gets a snippet of the list, based on this tuple structure (start index, size of snippet inclusive of first index)
        #print("getting current job's list")
        return_list = []
        for i in range(job[1]):
            return_list.append(self.num_list[job[0]+i])
        
        #print(f"job's list: {return_list}")
        return return_list
    
    
    
    def step(self):
        #print("step")
        #is_rearranged.is_rearranged(self.unsorted_list,self.num_list)
        current_job = self.job_list[self.job_pointer] # to emulate the function stacking in the normal merge sort, i am using a dynamic job list that works from left to right to divide the "jobs" into smaller jobs, merge them, then solve.
        #print(f"current job list: {self.job_list}\ncurrent job: {current_job}")
        if self.currently_solving: #this will run when in the process of merging two smaller lists, stored in self.solve_listA/B
            #print("currently solving")
            #print(f"current solved list: {self.solved_temp}\nsolve list a: {self.solve_list_a}\nsolve list b: {self.solve_list_b}")
            if len(self.solve_list_a) != 0 and len(self.solve_list_b) != 0:
                #print("normal solve step")
                if self.solve_list_a[0] < self.solve_list_b[0]:
                    self.solved_temp.append(self.solve_list_a[0])
                    del self.solve_list_a[0]
                else:
                    self.solved_temp.append(self.solve_list_b[0])
                    del self.solve_list_b[0]
                
                
                
                green = []
                green.append(current_job[0]+len(self.solved_temp))
                green.append(current_job[0]+len(self.solved_temp)+len(self.solve_list_a))
                
                #render changes
                render_list = []
                render_list += self.num_list[:current_job[0]]
                render_list += self.solved_temp
                render_list += self.solve_list_a
                render_list += self.solve_list_b
                render_list += self.num_list[(current_job[0]+current_job[1]):]
                self.transfer_list_to_buffer(render_list,red_list=green)
                return
                
                
                
            elif len(self.solve_list_a) > 1 or len(self.solve_list_b) > 1:
                #print("one of the lists empty")
                #print(f"len of a: {len(self.solve_list_a)}\nlen of b: {len(self.solve_list_b)}")
                if len(self.solve_list_a) > 0:
                    self.solved_temp.append(self.solve_list_a[0])
                    del self.solve_list_a[0]
                else:
                    self.solved_temp.append(self.solve_list_b[0])
                    del self.solve_list_b[0]
                green = []
                green.append(current_job[0]+len(self.solved_temp))
                
                render_list = []
                render_list += self.num_list[:current_job[0]]
                render_list += self.solved_temp
                render_list += self.solve_list_a
                render_list += self.solve_list_b
                render_list += self.num_list[(current_job[0]+current_job[1]):]
                self.transfer_list_to_buffer(render_list,red_list=green)
                return
                    
                    
                
            else:
                #print("final solve step")
                if len(self.solve_list_a) > len(self.solve_list_b):
                    self.solved_temp.append(self.solve_list_a[0])
                    del self.solve_list_a[0]
                else:
                    self.solved_temp.append(self.solve_list_b[0])
                    del self.solve_list_b[0]
                
                
                
                self.currently_solving = False
                
                start_index = current_job[0]
                
                self.num_list = self.replace_list(self.num_list,self.solved_temp,start_index)

                self.transfer_list_to_buffer(self.num_list,red_list=[current_job[0]+current_job[1]-1])
                #break out of loop and insert the disconected list into the main list.
                return
        
        
        
        if current_job[2] == 0: # a job can either be dividing or conquering signified by current_job[2] == 0 and current_job[2] == 1 respectivly.
            #here we are dividing the job, until it reaches length 1 (current_job[1] = 1) meaning we set them to conquering mode

            #print("divide")
            prev_size = current_job[1]
            a_size = int(math.ceil(prev_size/2))
            b_size = prev_size - a_size
            
            a_start = current_job[0]
            b_start = a_start + a_size
            
            
            del self.job_list[self.job_pointer]
            
            self.job_list.insert(self.job_pointer, (b_start,b_size,1 if b_size == 1 else 0))
            self.job_list.insert(self.job_pointer, (a_start,a_size,1 if a_size == 1 else 0))
            
            # render these changes
        
            
        else: # if  the current job is trying to merge
            #print("merge")
            if self.job_pointer != len(self.job_list)-1: #if this is not the very right job
                
                if self.job_list[self.job_pointer + 1][2] == 1:  #if the job on the right also wants to merge, it starts the merging process described on line 127
                    #print("merge with right")
                    self.currently_solving = True
                    self.solved_temp= []
                    
                    self.solve_list_a = self.get_job_list(self.job_list[self.job_pointer])
                    self.solve_list_b = self.get_job_list(self.job_list[self.job_pointer+1])
                    
                    job_1 = self.job_list[self.job_pointer]
                    job_2 = self.job_list[self.job_pointer+1]
                    
                    del self.job_list[self.job_pointer]
                    del self.job_list[self.job_pointer]
                    
                    self.job_list.insert(self.job_pointer,(job_1[0],job_1[1]+job_2[1],1))
                    
                    #merge jobs
                    
                    
                elif self.job_list[self.job_pointer + 1][2] == 0 and self.job_pointer != 0: # if cant merge with the job on the right
                    if abs(self.job_list[self.job_pointer - 1][1] - self.job_list[self.job_pointer][1]) < 2:
                        #print("shift left")
                        self.job_pointer -= 1 # if the job_pointer is not on the very left (job_pointer = 0) then go right
                    else:
                        #print("shift right")
                        self.job_pointer += 1 #if it cant merge and cant go left, it goes right
                        
                else:
                    #print("shift right")
                    self.job_pointer += 1 #if it cant merge and cant go left, it goes right
            else:
                #print("went here")
                if len(self.job_list) == 1:
                    #print("solved")
                    self.solved = True
                    self.transfer_list_to_buffer(self.num_list,green_list=sorting_helper.create_acsending_list(self.list_len))
                    return
                else:
                    self.job_pointer -= 1
        
        
        self.transfer_list_to_buffer(self.num_list)
class quick_sort(sorting_helper.sorting_algorithm):
    def __init__(self, unsorted_list, turt: turtle.Turtle, screen):
        super().__init__(unsorted_list, turt, screen)       
        self.job_list = [(0,self.list_len)]
        self.job_pointer = 0
        self.current_pivot = -1
        self.pivot_index = -1
        self.pivot_left = []
        self.pivot_right = []
        self.job_num_list = []
        self.fixed_pivots = [] #indicies of sorted pivots
        self.currently_dividing = False
        self.offset = 0
        self.init_len = -1
        
    def extract_list(self,start,length): 
        return_list = []
        for i in range(length):
            return_list.append(self.num_list[start+i])
        
        return return_list
        
    def step(self):
        if len(self.fixed_pivots) == self.list_len:
            print("solved")
            self.solved = True
            self.transfer_list_to_buffer(self.num_list,green_list=self.fixed_pivots)
            return
            
        current_job = self.job_list[self.job_pointer]
        #print(f"jobs: {self.job_list}\ncurrent pivot: {self.current_pivot}\ncurrently dividing: {self.currently_dividing}\njob num list: {self.job_num_list}\nleft: {self.pivot_left}\nright: {self.pivot_right}\n\n\n\n")
        if self.currently_dividing:#
            if len(self.job_num_list) == 0:
                self.currently_dividing = False
                self.fixed_pivots.append(current_job[0])
                #print(f"appened fixed point (final): {self.fixed_pivots[-1]}")

                del self.job_list[0]
                self.transfer_list_to_buffer(self.num_list,green_list=self.fixed_pivots)
                return
            
            split = None
            if len(self.job_num_list) != 1:

                

                if self.job_num_list[0] > self.current_pivot:
                    self.pivot_right.append(self.job_num_list[0])
                    

                else:
                    self.pivot_left.append(self.job_num_list[0])
                    

                
                del self.job_num_list[0]

                

                
                #display
            else:
                if self.job_num_list[0] > self.current_pivot:
                    self.pivot_right.append(self.job_num_list[0])
                    split = "right"
                else:
                    self.pivot_left.append(self.job_num_list[0])
                    split = "left"
                
                del self.job_num_list[0]
                self.currently_dividing = False
                
                #print
                
                if len(self.pivot_left) > 0:
                    self.job_list.append((current_job[0],len(self.pivot_left)))
                    #print(f"added job left: {(current_job[0],len(self.pivot_left))}")
                
                if len(self.pivot_right) > 0:
                    self.job_list.append((current_job[0]+len(self.pivot_left)+1,len(self.pivot_right)))
                    #print(f"added job right: {(current_job[0]+len(self.pivot_left)+1,len(self.pivot_right))}")

                #print(f"\nPIVOTS at end\nPivot:{self.current_pivot}\nLeft:{self.pivot_left}\nRight:{self.pivot_right}\n\n")
                
                sec_list = self.pivot_left.copy()
                sec_list += [self.current_pivot]
                sec_list += self.pivot_right
                
                self.offset = 0

                self.num_list = self.replace_list(self.num_list,sec_list,current_job[0])
                self.fixed_pivots.append(current_job[0]+len(self.pivot_left))
                #print(f"appened fixed point (non final): {self.fixed_pivots[-1]}\n{self.pivot_left}")
                
                del self.job_list[0]
                red_list = []
                precompute = current_job[0]+len(self.job_num_list[:math.ceil(self.init_len/2)-self.offset])+len(self.pivot_left)
                red_list.append(precompute)
                if split == "left":
                    
                    red_list.append(precompute-1)
                    
                else:
                    precompute += len(self.pivot_right)
                    red_list.append(precompute)

                self.transfer_list_to_buffer(self.num_list,red_list=red_list,green_list=self.fixed_pivots)
                
                return
        
            working_list = self.job_num_list[:math.ceil(self.init_len/2)-self.offset]
            working_list += self.pivot_left
            working_list += [self.current_pivot]
            working_list += self.pivot_right
            working_list += self.job_num_list[math.ceil(self.init_len/2)-self.offset:]
            display_list = self.replace_list(self.num_list,working_list,current_job[0])

            red_list = []
            precompute = current_job[0]+len(self.job_num_list[:math.ceil(self.init_len/2)-self.offset])+len(self.pivot_left)
            red_list.append(precompute)
            if split == "left":
                
                red_list.append(precompute-1)
                
            else:
                precompute += len(self.pivot_right)
                red_list.append(precompute)

            self.transfer_list_to_buffer(display_list,red_list=red_list,green_list=self.fixed_pivots)

            if self.offset < math.floor((self.init_len+1)/2):
                self.offset += 1
                
        else:
            
            #select pivot
            self.pivot_index = self.job_list[self.job_pointer][0]+math.floor(self.job_list[self.job_pointer][1]/2)
            #print(self.pivot_index)
            #print(current_job)
            self.current_pivot = self.num_list[self.pivot_index]
            self.currently_dividing = True
            self.job_num_list = self.extract_list(current_job[0],current_job[1])
            #print(self.pivot_index-current_job[0])
            del self.job_num_list[self.pivot_index-current_job[0]]
            self.init_len = len(self.job_num_list)
            self.pivot_left.clear()
            self.pivot_right.clear()
            self.transfer_list_to_buffer(self.num_list,green_list=self.fixed_pivots,red_list=[self.pivot_index])

    


def init_sorting_algorithm(sorting_type,turtle_instance,screen_instance,length,custom_list=[]):
    if len(custom_list) == 0:
        submit_list = []
        for i in range(length):
            submit_list.append(random.randint(1,200))

        new_sort = sorting_type(submit_list,turtle_instance,screen_instance)
        return new_sort
    else:
        new_sort = sorting_type(custom_list,turtle_instance,screen_instance)
        return new_sort


class MAIN:
    def __init__(self):
        self.current_sized = 200
        self.time_sum = 0.0
        self.last_frame_time = time.time()
        self.current_sort = init_sorting_algorithm(merge_sort,t,screen,self.current_sized)
        self.Step = False
        self.break_out = False
    
    def calculate_dt(self):
        current_time = time.time()
        dt = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return dt
    
    def process(self):
        print("test")
        dt = self.calculate_dt()
            #print("frame")
        self.time_sum += dt


        if self.time_sum > self.current_sort.step_delay and not self.Step:
            self.current_sort.process()
            time_sum = 0.0
            time.sleep(0.001)
        if self.Step:
            self.current_sort.process()
        if self.current_sort.solved:
            self.break_out = True
            print("solved")
            print(f"step count: {self.current_sort.step_count}")


main_obj = MAIN()

main_obj.Step = True
INPUT = keyboard_listener(["Right","Space"])
state = STATES.INIT_RUN


while True:
    INPUT.update()
     
    match state:
        case STATES.INIT_START:
            pass
        case STATES.START:
            pass
        case STATES.INIT_RUN:
            main_obj.process()
            state = STATES.RUN
        case STATES.RUN:
            if INPUT.key_just_pressed("Space"):
                main_obj.Step = not main_obj.Step
            if not main_obj.Step:
                main_obj.process()
            else:
                if INPUT.key_just_pressed("Right"):
                    main_obj.process()

            if main_obj.break_out:
                state = STATES.END
                
        case STATES.END:
            pass

    screen.update()

#screen.onscreenclick(fun=click_handler)

#screen.mainloop()
