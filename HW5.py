
from bangtal import *

setGameOption(GameOption.INVENTORY_BUTTON,False)
setGameOption(GameOption.MESSAGE_BOX_BUTTON,False)
setGameOption(GameOption.ROOM_TITLE,False)


start = Scene("시작화면","Images\원본.jpg")
gameScene = Scene("게임화면","Images\배경.jpg")




#110,116

startButton = Object("Images\start.png")
startButton.locate(start,640-150,120)
startButton.setScale(3)
startButton.show()


def endcheck():
    global image1_posX,image1_posY,image2_posX,image2_posY,image3_posX,image3_posY,image4_posX,image4_posY,image5_posX,image5_posY,image6_posX,image6_posY,image7_posX,image7_posY,image8_posX,image8_posY,none_posX,none_posY
    if image1_posX+100 == image2_posX and image2_posX+100 == image3_posX and image1_posY -100 == image4_posY and image4_posX +100 == image5_posX and image5_posX+100 == image6_posX and image5_posY-100 == image7_posY and image7_posX +100 == image8_posX:
        showMessage('끝')


image1 = Object("Images\image1.jpg")
image1.locate(gameScene,500,394)
image1.show()
image2 = Object("Images\image2.jpg")
image2.locate(gameScene,600,394)
image2.show()
image3 = Object("Images\image3.jpg")
image3.locate(gameScene,700,394)
image3.show()
image4 = Object("Images\image4.jpg")
image4.locate(gameScene,500,294)
image4.show()
image5 = Object("Images\image5.jpg")
image5.locate(gameScene,600,294)
image5.show()
image6 = Object("Images\image6.jpg")
image6.locate(gameScene,700,294)
image6.show()
image7 = Object("Images\image7.jpg")
image7.locate(gameScene,500,194)
image7.show()
image8 = Object("Images\image8.jpg")
image8.locate(gameScene,600,194)
image8.show()
none = Object("Images\none.jpg")
none.locate(gameScene,700,194)
none.show()

image1_posX=500
image1_posY=394
image2_posX=600
image2_posY=394
image3_posX=700
image3_posY=394
image4_posX=500
image4_posY=294
image5_posX=600
image5_posY=294
image6_posX=700
image6_posY=294
image7_posX=500
image7_posY=194
image8_posX=600
image8_posY=194
none_posX=700
none_posY=194


def startButton_onMouseAction(x,y,action):
    gameScene.enter()

def image1_onMouseAction(x,y,action):
    global image1_posX,none_posX
    global image1_posY,none_posY
    if image1_posX+100 == none_posX and image1_posY == none_posY:
        temp=image1_posX
        image1_posX=none_posX
        none_posX=temp
        temp=image1_posY
        image1_posY=none_posY
        none_posY=temp
        image1.locate(gameScene,image1_posX,image1_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image1_posX-100 == none_posX and image1_posY == none_posY:
        temp=image1_posX
        image1_posX=none_posX
        none_posX=temp
        temp=image1_posY
        image1_posY=none_posY
        none_posY=temp
        image1.locate(gameScene,image1_posX,image1_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image1_posX == none_posX and image1_posY +100 == none_posY:
        temp=image1_posX
        image1_posX=none_posX
        none_posX=temp
        temp=image1_posY
        image1_posY=none_posY
        none_posY=temp
        image1.locate(gameScene,image1_posX,image1_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image1_posX == none_posX and image1_posY - 100 == none_posY:
        temp=image1_posX
        image1_posX=none_posX
        none_posX=temp
        temp=image1_posY
        image1_posY=none_posY
        none_posY=temp
        image1.locate(gameScene,image1_posX,image1_posY)
        none.locate(gameScene,none_posX,none_posY)

def image2_onMouseAction(x,y,action):
    global image2_posX,none_posX
    global image2_posY,none_posY
    if image2_posX+100 == none_posX and image2_posY == none_posY:
        temp=image2_posX
        image2_posX=none_posX
        none_posX=temp
        temp=image2_posY
        image2_posY=none_posY
        none_posY=temp
        image2.locate(gameScene,image2_posX,image2_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image2_posX-100 == none_posX and image2_posY == none_posY:
        temp=image2_posX
        image2_posX=none_posX
        none_posX=temp
        temp=image2_posY
        image2_posY=none_posY
        none_posY=temp
        image2.locate(gameScene,image2_posX,image2_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image2_posX == none_posX and image2_posY +100 == none_posY:
        temp=image2_posX
        image2_posX=none_posX
        none_posX=temp
        temp=image2_posY
        image2_posY=none_posY
        none_posY=temp
        image2.locate(gameScene,image2_posX,image2_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image2_posX == none_posX and image2_posY - 100 == none_posY:
        temp=image2_posX
        image2_posX=none_posX
        none_posX=temp
        temp=image2_posY
        image2_posY=none_posY
        none_posY=temp
        image2.locate(gameScene,image2_posX,image2_posY)
        none.locate(gameScene,none_posX,none_posY)

def image3_onMouseAction(x,y,action):
    global image3_posX,none_posX
    global image3_posY,none_posY
    if image3_posX+100 == none_posX and image3_posY == none_posY:
        temp=image3_posX
        image3_posX=none_posX
        none_posX=temp
        temp=image3_posY
        image3_posY=none_posY
        none_posY=temp
        image3.locate(gameScene,image3_posX,image3_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image3_posX-100 == none_posX and image3_posY == none_posY:
        temp=image3_posX
        image3_posX=none_posX
        none_posX=temp
        temp=image3_posY
        image3_posY=none_posY
        none_posY=temp
        image3.locate(gameScene,image3_posX,image3_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image3_posX == none_posX and image3_posY +100 == none_posY:
        temp=image3_posX
        image3_posX=none_posX
        none_posX=temp
        temp=image3_posY
        image3_posY=none_posY
        none_posY=temp
        image3.locate(gameScene,image3_posX,image3_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image3_posX == none_posX and image3_posY - 100 == none_posY:
        temp=image3_posX
        image3_posX=none_posX
        none_posX=temp
        temp=image3_posY
        image3_posY=none_posY
        none_posY=temp
        image3.locate(gameScene,image3_posX,image3_posY)
        none.locate(gameScene,none_posX,none_posY)

def image4_onMouseAction(x,y,action):
    global image4_posX,none_posX
    global image4_posY,none_posY
    if image4_posX+100 == none_posX and image4_posY == none_posY:
        temp=image4_posX
        image4_posX=none_posX
        none_posX=temp
        temp=image4_posY
        image4_posY=none_posY
        none_posY=temp
        image4.locate(gameScene,image4_posX,image4_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image4_posX-100 == none_posX and image4_posY == none_posY:
        temp=image4_posX
        image4_posX=none_posX
        none_posX=temp
        temp=image4_posY
        image4_posY=none_posY
        none_posY=temp
        image4.locate(gameScene,image4_posX,image4_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image4_posX == none_posX and image4_posY +100 == none_posY:
        temp=image4_posX
        image4_posX=none_posX
        none_posX=temp
        temp=image4_posY
        image4_posY=none_posY
        none_posY=temp
        image4.locate(gameScene,image4_posX,image4_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image4_posX == none_posX and image4_posY - 100 == none_posY:
        temp=image4_posX
        image4_posX=none_posX
        none_posX=temp
        temp=image4_posY
        image4_posY=none_posY
        none_posY=temp
        image4.locate(gameScene,image4_posX,image4_posY)
        none.locate(gameScene,none_posX,none_posY)

def image5_onMouseAction(x,y,action):
    global image5_posX,none_posX
    global image5_posY,none_posY
    if image5_posX+100 == none_posX and image5_posY == none_posY:
        temp=image5_posX
        image5_posX=none_posX
        none_posX=temp
        temp=image5_posY
        image5_posY=none_posY
        none_posY=temp
        image5.locate(gameScene,image5_posX,image5_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image5_posX-100 == none_posX and image5_posY == none_posY:
        temp=image5_posX
        image5_posX=none_posX
        none_posX=temp
        temp=image5_posY
        image5_posY=none_posY
        none_posY=temp
        image5.locate(gameScene,image5_posX,image5_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image5_posX == none_posX and image5_posY +100 == none_posY:
        temp=image5_posX
        image5_posX=none_posX
        none_posX=temp
        temp=image5_posY
        image5_posY=none_posY
        none_posY=temp
        image5.locate(gameScene,image5_posX,image5_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image5_posX == none_posX and image5_posY - 100 == none_posY:
        temp=image5_posX
        image5_posX=none_posX
        none_posX=temp
        temp=image5_posY
        image5_posY=none_posY
        none_posY=temp
        image5.locate(gameScene,image5_posX,image5_posY)
        none.locate(gameScene,none_posX,none_posY)

def image6_onMouseAction(x,y,action):
    global image6_posX,none_posX
    global image6_posY,none_posY
    if image6_posX+100 == none_posX and image6_posY == none_posY:
        temp=image6_posX
        image6_posX=none_posX
        none_posX=temp
        temp=image6_posY
        image6_posY=none_posY
        none_posY=temp
        image6.locate(gameScene,image6_posX,image6_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image6_posX-100 == none_posX and image6_posY == none_posY:
        temp=image6_posX
        image6_posX=none_posX
        none_posX=temp
        temp=image6_posY
        image6_posY=none_posY
        none_posY=temp
        image6.locate(gameScene,image6_posX,image6_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image6_posX == none_posX and image6_posY +100 == none_posY:
        temp=image6_posX
        image6_posX=none_posX
        none_posX=temp
        temp=image6_posY
        image6_posY=none_posY
        none_posY=temp
        image6.locate(gameScene,image6_posX,image6_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image6_posX== none_posX and image6_posY - 100 == none_posY:
        temp=image6_posX
        image6_posX=none_posX
        none_posX=temp
        temp=image6_posY
        image6_posY=none_posY
        none_posY=temp
        image6.locate(gameScene,image6_posX,image6_posY)
        none.locate(gameScene,none_posX,none_posY)

def image7_onMouseAction(x,y,action):
    global image7_posX,none_posX
    global image7_posY,none_posY
    if image7_posX+100 == none_posX and image7_posY == none_posY:
        temp=image7_posX
        image7_posX=none_posX
        none_posX=temp
        temp=image7_posY
        image7_posY=none_posY
        none_posY=temp
        image7.locate(gameScene,image7_posX,image7_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image7_posX-100 == none_posX and image7_posY == none_posY:
        temp=image7_posX
        image7_posX=none_posX
        none_posX=temp
        temp=image7_posY
        image7_posY=none_posY
        none_posY=temp
        image7.locate(gameScene,image7_posX,image7_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image7_posX == none_posX and image7_posY +100 == none_posY:
        temp=image7_posX
        image7_posX=none_posX
        none_posX=temp
        temp=image7_posY
        image7_posY=none_posY
        none_posY=temp
        image7.locate(gameScene,image7_posX,image7_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image7_posX == none_posX and image7_posY - 100 == none_posY:
        temp=image7_posX
        image7_posX=none_posX
        none_posX=temp
        temp=image7_posY
        image7_posY=none_posY
        none_posY=temp
        image7.locate(gameScene,image7_posX,image7_posY)
        none.locate(gameScene,none_posX,none_posY)



def image8_onMouseAction(x,y,action):
    global image8_posX,none_posX
    global image8_posY,none_posY
    if image8_posX + 100 == none_posX and image8_posY == none_posY:
        temp=image8_posX
        image8_posX=none_posX
        none_posX=temp
        temp=image8_posY
        image8_posY=none_posY
        none_posY=temp
        image8.locate(gameScene,image8_posX,image8_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image8_posX - 100 == none_posX and image8_posY == none_posY:
        temp=image8_posX
        image8_posX=none_posX
        none_posX=temp
        temp=image8_posY
        image8_posY=none_posY
        none_posY=temp
        image8.locate(gameScene,image8_posX,image8_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image8_posX == none_posX and image8_posY +100 == none_posY:
        temp=image8_posX
        image8_posX=none_posX
        none_posX=temp
        temp=image8_posY
        image8_posY=none_posY
        none_posY=temp
        image8.locate(gameScene,image8_posX,image8_posY)
        none.locate(gameScene,none_posX,none_posY)
    if image8_posX == none_posX and image8_posY - 100 == none_posY:
        temp=image8_posX
        image8_posX=none_posX
        none_posX=temp
        temp=image8_posY
        image8_posY=none_posY
        none_posY=temp
        image8.locate(gameScene,image8_posX,image8_posY)
        none.locate(gameScene,none_posX,none_posY)
 #   endcheck()



image1.onMouseAction=image1_onMouseAction
image2.onMouseAction=image2_onMouseAction
image3.onMouseAction=image3_onMouseAction
image4.onMouseAction=image4_onMouseAction
image5.onMouseAction=image5_onMouseAction
image6.onMouseAction=image6_onMouseAction
image7.onMouseAction=image7_onMouseAction
image8.onMouseAction=image8_onMouseAction

startButton.onMouseAction=startButton_onMouseAction














startGame(start)