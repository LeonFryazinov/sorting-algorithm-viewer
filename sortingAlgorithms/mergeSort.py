import math
import turtle
import sorting_helper

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
            
            self.transfer_list_to_buffer(self.num_list,red_list=list(range(current_job[0],current_job[0]+current_job[1])))
            
            del self.job_list[self.job_pointer]
            
            self.job_list.insert(self.job_pointer, (b_start,b_size,1 if b_size == 1 else 0))
            self.job_list.insert(self.job_pointer, (a_start,a_size,1 if a_size == 1 else 0))
            return
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