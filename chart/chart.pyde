from time import sleep

def setup():
    fullScreen()
    background('#0F077C')
    global chart, values, z, zz, zzz, chart2, values2, chart3, values3

    chart = Chart("Chart A", 100, 500, "time", "velocity", "t", "km2", 20, 50, 150, 150)
    chart.setup_chart()
    values = [(6, 1, 8, 2), (8, 2, 10, 3), (10, 3, 15, 4), (15, 4, 17, 20)]

    chart2 = Chart("Chart B", 550, 500, "speed", "velocity", "cm", "m", 20, 90, 300, 200)
    chart2.setup_chart()
    values2 = [(6, 1, 4, 2), (4, 2, 10, 10), (10, 10, 15, 40), (15, 40, 17, 70)]

    chart3 = Chart("Chart C", 1000, 500, "speed", "velocity", "cm", "m", 20, 90, 300, 200)
    chart3.setup_chart()
    values3 = [(6, 9, 4, 9), (4, 9, 10, 20), (10, 20, 15, 40), (15, 40, 17, 70)]

    z = 0
    zz = 0
    zzz = 0

def draw():
    sleep(0.3)
    chart.first_line(0, 0, 6, 1)
    chart2.first_line(0, 0, 6, 1)
    chart3.first_line(0, 0, 6, 9)
    global z, zz, zzz

    if z < len(values):
        chart.draw_line(values[z][0], values[z][1], values[z][2], values[z][3])
    z += 1

    if zz < len(values2):
        chart2.draw_line(values2[zz][0], values2[zz][1], values2[zz][2], values2[zz][3])
    zz += 1

    if zzz < len(values3):
        chart3.draw_line(values3[zzz][0], values3[zzz][1], values3[zzz][2], values3[zzz][3])
    zzz += 1

class Chart:
    def __init__(self, name, xpos, ypos, xname, yname, xunit, yunit, xmax, ymax, xsize, ysize):
        self.name = name
        self.xpos = xpos
        self.ypos = ypos
        self.xname = xname
        self.yname = yname
        self.xunit = xunit
        self.yunit = yunit
        self.xmax = xmax
        self.ymax = ymax
        self.xsize = xsize
        self.ysize = ysize

    def setup_chart(self):
        stroke('#FFFFFF')
        # Drawing and setup X
        line(self.xpos, self.ypos, self.xpos+self.xsize*11/10, self.ypos)
        for unit in range(11):
            line(self.xpos+unit*self.xsize/10, self.ypos+2, self.xpos+unit*self.xsize/10, self.ypos-2)

        # Drawing and setup Y
        line(self.xpos, self.ypos, self.xpos, self.ypos-self.ysize*11/10)
        for unit in range(11):
            line(self.xpos+2, self.ypos-unit*self.ysize/10, self.xpos-2, self.ypos-unit*self.ysize/10)

        # Setting scale
        text("(0, 0)", self.xpos-40, self.ypos+20)

        for letter in range(10):
            val = str(self.xmax-(self.xmax-(self.xmax*(letter+1)/10)))
            text(val, self.xpos-(len(val)*3.5)+self.xsize*(letter+1)/10, self.ypos+20)

        for letter in range(10):
            val = str(self.ymax-(self.ymax-(self.ymax*(letter+1)/10)))
            text(val, self.xpos-(len((val))*10), self.ypos+5-self.ysize*(letter+1)/10)
        
        text(self.xname+" "+self.xunit, self.xpos+(self.xsize-(len(self.xname+" "+self.xunit)))/2, self.ypos+35)
        rotate(radians(270))
        text(self.yname+" "+self.yunit, -self.ypos-self.xmax+self.ysize/2, self.xpos-25)
        rotate(radians(90))
        text(self.name, (self.xpos+self.xsize/2)-len(self.name)*2, self.ypos-self.ysize*1.1)
        self.box()

    def first_line(self, firstx, firsty, x, y):
        line(self.xpos+firstx, self.ypos+firsty, self.xpos+x*(self.xsize/self.xmax), self.ypos-y*(self.ysize/self.ymax))

    def draw_line(self, firstx, firsty, x, y):
        line(self.xpos+firstx*(self.xsize/self.xmax), self.ypos-firsty*(self.ysize/self.ymax), self.xpos+x*(self.xsize/self.xmax), self.ypos-y*(self.ysize/self.ymax))

    def box(self):
        line(self.xpos-50, self.ypos-self.ysize*1.2, self.xpos+self.xsize*1.2, self.ypos-self.ysize*1.2)
        line(self.xpos-50, self.ypos-self.ysize*1.2, self.xpos-50, self.ypos*1.1)
        line(self.xpos-50, self.ypos*1.1, self.xpos+self.xsize*1.2, self.ypos*1.1)
        line(self.xpos+self.xsize*1.2, self.ypos-self.ysize*1.2, self.xpos+self.xsize*1.2, self.ypos*1.1)