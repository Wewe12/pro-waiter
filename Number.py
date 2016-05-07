import Sprite

class Number(Sprite.Sprite):

    # object's constructor overloading

    def __init__(self,x,y,texture_state0,texture_state1,texture_state2,texture_state3):
        super(Number,self).__init__(x,y,texture_state0)
        self.texture_state0 = texture_state0  # black number
        self.texture_state1 = texture_state1  # orange number
        self.texture_state2 = texture_state2  # red number
        self.texture_state3 = texture_state3  # green number

    # changes number's color
    def update(self,state):
        if (state == 1):
            self.image = self.texture_state1
        elif (state == 2):
            self.image = self.texture_state2
        else :
            self.image = self.texture_state3
