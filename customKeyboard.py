import keyboard

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
