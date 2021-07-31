def setup():
    size(500, 400)
    global ball
    ball = Ball('#CE14D8', 100, 50, 15, 500, 400)

def draw():
    background('#1FFFEE')
    global ball
    ball.create()
    ball.fall()

class Ball:
    def __init__(self, colour, xpos, ypos, radius, xborder, yborder):
        self.colour = colour
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.xborder = xborder
        self.yborder = yborder
        self.xdown = True
        self.ydown = True
        
    def create(self):
        stroke(self.colour)
        fill(self.colour)
        circle(self.xpos, self.ypos, self.radius)
    
    def fall(self):
        if self.xpos >= self.xborder:
            self.xdown = False
        elif self.xpos <= 0:
            self.xdown = True
        
        if self.ypos >= self.yborder:
            self.ydown = False
        elif self.ypos <= 0:
            self.ydown = True
        
        if self.xdown:
            self.xpos += 1
        else:
            self.xpos -= 1
        
        if self.ydown:
            self.ypos += 1
        else:
            self.ypos -= 1
        
        self.create()