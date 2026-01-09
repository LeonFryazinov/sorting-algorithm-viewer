import turtle

def get_list_max(_list):
    maximum = -255
    for num in _list:
        if num > maximum:
            maximum = num
    return maximum



class sorting_algorithm:
    def __init__(self,unsorted_list,turt:turtle.Turtle,screen):
        self.unsorted_list = unsorted_list
        self.num_list = self.unsorted_list.copy()

        self.list_len = len(self.unsorted_list)

        self.drawn_list_buffer = {}

        self.t = turt
        self.screen = screen
        
        self.max_bar_len = 500 #in pixels
        self.base_line = -400
        self.display_width = 1000
        self.max_val = get_list_max(self.unsorted_list)
        self.bar_width = (self.display_width/self.list_len)*0.8

        
    
    def transfer_list_to_buffer(self,buffer_list):
        print("cleared buffer")
        self.drawn_list_buffer = {}
        for i in range(len(buffer_list)):
            self.send_num_to_buffer(buffer_list[i],i)

    def send_num_to_buffer(self,num,idx,col=""):
        if self.drawn_list_buffer[idx] != None:
            print(f"overwritten value {self.drawn_list_buffer[idx]} at position {idx} in the list")

        self.drawn_list_buffer[idx] = (num,col)
    
    def draw_list(self):
        global screen
        drawn_list = []
        for i in range(self.list_len):
            drawn_list.append(self.drawn_list_buffer[i])
        
        for idx, dat in enumerate(drawn_list):
            num = dat[0]
            col = dat[1]
            self.draw_bar(num=num,idx=idx,col=col)
        
        self.screen.update()
        
            
        
        


    
    
    def draw_bar(self,num,idx,col):
        bar_len = int(round(float(num)/float(self.max_val) * self.max_bar_len))
        horiz_offset_decimal = float(idx)/float(self.list_len)
        horiz_offset = (horiz_offset_decimal * self.display_width) - (self.display_width/2)

        self.t.color(col)
        self.t.pensize(2)
        self.t.up()
        self.t.goto(int(round(horiz_offset+(self.bar_width/2))),self.base_line)
        self.t.down()
        self.t.goto(int(round(horiz_offset-(self.bar_width/2))),self.base_line)
        self.t.goto(int(round(horiz_offset-(self.bar_width/2))),self.base_line+bar_len)
        self.t.goto(int(round(horiz_offset+(self.bar_width/2))),self.base_line+bar_len)
        self.t.goto(int(round(horiz_offset+(self.bar_width/2))),self.base_line)
        self.t.up()
        
        





        
        
        
    
    def step(self):
        print("no algorithm implemented")
    
    def check_sorted(self):
        checked_list = self.num_list
        for i in range(len(checked_list)-1):
            if checked_list[i] > checked_list[i+1]:
                return False
        
        return True