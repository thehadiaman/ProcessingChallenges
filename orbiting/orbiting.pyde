import math
def setup():
    fullScreen()
    global theta, radius
    theta = 0
    radius = 200
    
def draw():
    background("#636756")
    high_mass()
    global theta
    x = float(math.cos(math.radians(theta)))*(radius/2)
    y = float(math.sin(math.radians(theta)))*(radius/2)
    print(x, y, theta)
    theta += 1
    if theta >= 360:
        theta = 0
    orbiter(x, y, radius)

def high_mass():
    fill("#D1FF3B")
    noStroke()
    circle(width/2, height/2, 75)


def orbiter(xpos, ypos, radius):
    orbit(radius)
    strokeWeight(0.1)
    fill("#A9A9A9")
    noStroke()
    circle(width/2+xpos, height/2+ypos, 20)


def orbit(orbit):
    stroke("#BABCB3")
    noFill()
    circle(width/2, height/2, orbit)
