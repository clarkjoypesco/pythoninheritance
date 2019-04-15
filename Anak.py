import Magulang

class Child(Magulang.Parent):
    
    def __init__(self,last_name,eye_color, number_of_toys):
        print 'Child Constructor Called!'
        Magulang.Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print ' Last Name - ' + self.last_name
        print ' Eye Color - ' + self.eye_color
        print ' Number of Toys - ' + str(self.number_of_toys)

