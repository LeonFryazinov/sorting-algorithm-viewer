import turtle
import random
import time
from enum import Enum

import sortingAlgorithms.bubbleSort as bubbleSort
import sortingAlgorithms.insertionSort as insertionSort
import sortingAlgorithms.mergeSort as mergeSort
import sortingAlgorithms.quickSort as quickSort
import sortingAlgorithms.comedySort as comedySort

import keyboard
import customKeyboard

class STATES(Enum): #states enum, for future graphical interface
    INIT_START = 0
    START = 1
    INIT_RUN = 2
    RUN = 3
    END = 4




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


def draw_start(uiSelected,algSelected,listLen,stepping):
    ui.draw_rect(-160,0,300,450,fill=True)
    ui.draw_rect(110,155,200,140,fill=True,secondary_colour="#1fe0ca" if uiSelected == 1 else "white")
    ui.draw_rect(110,12,200,140,fill=True,secondary_colour="#1fe0ca" if uiSelected == 2 else "white")
    ui.draw_rect(110,-150,200,140,fill=True,secondary_colour="#1fe0ca" if uiSelected == 3 else "white")
    
    boxAmount = len(sortingAlgorithms)
    boxHeight = 450/boxAmount
    
    fontSize = round(boxHeight*0.3)
    
    
    for i, alg in enumerate(sortingAlgorithms):
        
        text, class_name = alg
        ui.draw_rect(-160,(225-(i*boxHeight)-(boxHeight/2)),300,boxHeight,fill=True,secondary_colour="#1fe0ca" if (algSelected == i and uiSelected == 0) else "#119989" if algSelected == i and uiSelected != 0 else "white")
        ui.draw_text(-160,(225-(i*boxHeight)-(boxHeight/2)-fontSize/2), text, font_size=fontSize)
    
    
    ui.draw_text(110,180, "List length: ", font_size=15)
    ui.draw_text(110,120, str(listLen), font_size=25)
    
    ui.draw_text(110,0,"Stepping" if stepping else "not Stepping", font_size = 25 if stepping else 18)
    ui.draw_text(110,-170,"Start",font_size = 25)






class draw:
    def __init__(self,t):
        self.turt = t
    
    def clear(self):
        self.turt.clear()
    
    def draw_rect(self,x,y,width,height,fill=False,primary_colour="black",secondary_colour="white"):
        halfWidth = width/2
        halfHeight = height/2
        self.turt.color(primary_colour,secondary_colour) 
        self.turt.up()
        self.turt.goto(x+halfWidth,y+halfHeight)
        if fill:
            self.turt.begin_fill()
        
        self.turt.down()
        self.turt.goto(x+halfWidth,y-halfHeight)
        self.turt.goto(x-halfWidth,y-halfHeight)
        self.turt.goto(x-halfWidth,y+halfHeight)
        self.turt.goto(x+halfWidth,y+halfHeight)
        if fill:
            self.turt.end_fill()
        self.turt.up()
    def draw_polygon(self,point_list:list,fill=False,primary_colour="black",secondary_colour="white"):
        point_amount = len(point_list)
        if point_amount >= 0 and point_amount < 3:
            return
        
        self.turt.color(primary_colour,secondary_colour) 
        self.turt.up()
        self.turt.goto(point_list[0][0],point_list[0][1])
        
        
        if fill:
            self.turt.begin_fill()
        self.turt.down()
        for i in range(1,point_amount):
            x, y = point_list[i]
            self.turt.goto(x,y)
        self.turt.goto(point_list[0][0],point_list[0][1])
        
        if fill:
            self.turt.end_fill()
        self.turt.up()
    
    def draw_text(self,x,y,text,font_size = 20):
        self.turt.up()
        self.turt.goto(x,y)
        self.turt.down()
        self.turt.write(text, align="Center", font=("Courier", font_size, "bold"))
        self.turt.up()




class MAIN:
    def __init__(self):
        self.current_sized = 200
        self.time_sum = 0.0
        self.last_frame_time = time.time()
        self.current_sort = init_sorting_algorithm(bubbleSort.bubble_sort,t,screen,self.current_sized)
        self.Step = False
        self.break_out = False
    
    def calculate_dt(self):
        current_time = time.time()
        dt = current_time - self.last_frame_time
        self.last_frame_time = current_time
        return dt
    
    def process(self):
        #print("test")
        dt = self.calculate_dt()
            #print("frame")
        self.time_sum += dt


        if self.time_sum > self.current_sort.step_delay and not self.Step:
            self.current_sort.process()
            #timeSum = 0.0
            time.sleep(0.001)
        if self.Step:
            self.current_sort.process()
        if self.current_sort.solved:
            self.break_out = True
            print("solved")
            print(f"step count: {self.current_sort.step_count}")




state = STATES.INIT_START

#init turtle screen, creates a window that can be drawn to.
screen = turtle.Screen()
screen.screensize(600, 400, "lightblue")


#t.color("black", "lime")
# defines a turtle, which will draw to the screen defined line 164.
t = turtle.Turtle()
t.ht()
t.pensize(2)
t.speed(0)
screen.tracer(0)

main_obj = MAIN() # is responsible for drawing to the screen, and processing the sorting algorithms.


main_obj.Step = False # modifiable in UI, will either step through algorithm or run it with no delay. (true = delay, false = no delay)
state = STATES.INIT_START # state variable, helps the code keep track what is currently going on in the UI
INPUT = customKeyboard.keyboard_listener(["Left","Right","Up","Down","Space","Enter"])
numINPUT = customKeyboard.keyboard_listener(["1","2","3","4","5","6","7","8","9","0","Backspace"])
uiTurtle = turtle.Turtle()
uiTurtle.ht()
uiTurtle.pensize(2)
uiTurtle.speed(0)


ui = draw(uiTurtle)

sortingAlgorithms = [("Bubble sort",bubbleSort.bubble_sort),
                     ("Insertion sort",insertionSort.insertion_sort), 
                     ("Merge sort",mergeSort.merge_sort), 
                     ("Quick sort", quickSort.quick_sort), 
                     ("Miracle sort",  comedySort.miracle_sort), 
                     ("Bogo sort", comedySort.bogo_sort), 
                     ("Stalin sort", comedySort.stalin_sort)]

uiPointer = 0 # in the main UI there are multiple elements. UI pointer keeps track which one is currently being selected
algSelected = 0 # holds what algorithm is currently selected
listLen = 20 # list length, defaults to 20 items in the list 





    
    
while True:
    INPUT.update() # updates the state of the keys passed during declaration of "INPUT".      
    
    match state:
        case STATES.INIT_START: # only ran once at startup, draws inital UI
            #draw_start(uiPointer,algSelected,listLen,main_obj.Step)
            #ui.draw_text()
            state = STATES.START
            
        case STATES.START:
            match uiPointer:
                case 0:
                    if INPUT.key_just_pressed("Up") and algSelected != 0:
                        algSelected -= 1
                    if INPUT.key_just_pressed("Down") and algSelected != len(sortingAlgorithms)-1:
                        algSelected += 1
                    if INPUT.key_just_pressed("Left"):
                        uiPointer = 3
                    if INPUT.key_just_pressed("Right"):
                        uiPointer = 1
                case 1:
                    numINPUT.update() # only updates the state of each key if the box for typing is selected, reducing needless computation
                    
                    if INPUT.key_just_pressed("Down"):
                        uiPointer = 2
                    if INPUT.key_just_pressed("Left"):
                        uiPointer = 0
                    if INPUT.key_just_pressed("Right"):
                        uiPointer = 3
                    
                    
                    for i in range(10):
                        if numINPUT.key_just_pressed(str(i)) and listLen < 100 and uiPointer == 1:
                            if not (keyboard.is_pressed("Right") or keyboard.is_pressed("Left") or keyboard.is_pressed("Up") or keyboard.is_pressed("Down")):
                                listLen = (listLen * 10) + i
                                #print(i)
                    
                    if numINPUT.key_just_pressed("Backspace"):
                        listLen = listLen // 10
                    
                    
                    
                    
                    
                    
                    
                case 2:
                    if INPUT.key_just_pressed("Down"):
                        uiPointer = 3
                    if INPUT.key_just_pressed("Left"):
                        uiPointer = 0
                    if INPUT.key_just_pressed("Up"):
                        uiPointer = 1
                    
                    if INPUT.key_just_pressed("Enter") or INPUT.key_just_pressed("Space"):
                        main_obj.Step = not main_obj.Step
                        
                case 3:
                    if INPUT.key_just_pressed("Up"):
                        uiPointer = 2
                    if INPUT.key_just_pressed("Left"):
                        uiPointer = 0

                    
                    if INPUT.key_just_pressed("Enter") or INPUT.key_just_pressed("Space"):
                        main_obj.current_sized = listLen if listLen > 0 else 20
                        main_obj.current_sort = init_sorting_algorithm(sortingAlgorithms[algSelected][1],t,screen,main_obj.current_sized)
                        state = STATES.INIT_RUN
                    
            
            ui.clear()
            draw_start(uiPointer,algSelected,listLen,main_obj.Step)
        case STATES.INIT_RUN:
            ui.clear()
            main_obj.break_out = False
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
            if INPUT.key_just_pressed("Enter") or INPUT.key_just_pressed("Space"):
                state = STATES.INIT_START
                uiPointer = 0
                t.clear()

    screen.update()

#screen.onscreenclick(fun=click_handler)

#screen.mainloop()
