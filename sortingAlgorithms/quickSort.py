import math
import turtle
import sorting_helper


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
