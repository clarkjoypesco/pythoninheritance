import Magulang

class Child(Magulang.Parent):
    
    def __init__(self,last_name,eye_color, number_of_toys):
        Magulang.Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys


