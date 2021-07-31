global totalX
totalX = 500
global totalY
totalY = 300


def setup():
    size(totalX, totalY)


def mouseOver(positionX, positionY, totalX, totalY, sizeX, sizeY):
    limitX = [(positionX), (sizeX+positionX)]
    limitY = [(positionY), (sizeY+positionY)]
    if mouseX in range(limitX[0], limitX[1]+1) and mouseY in range(limitY[0], limitY[1]+1):
        return True
    return False


def draw():
    positionX = 150
    positionY = 75
    sizeX = 200
    sizeY = 150
    
    if mouseOver(positionX, positionY, totalX, totalY, sizeX, sizeY):
        fill('#EA0C5A')
        rect(positionX, positionY, sizeX, sizeY)
    else:
        fill('#EA2B6E')
        rect(positionX, positionY, sizeX, sizeY)
