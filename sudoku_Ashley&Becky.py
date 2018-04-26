import graphics
from graphics import *

win = graphics.GraphWin("Sudoku", 800, 800)
tiedye = Image(Point(400,400),"tiedye.gif")
Image.draw(tiedye,win)
peace = Image(Point(650,290),"smiley.gif")
Image.draw(peace,win)


#sets the background to white
rect = Rectangle(Point(50,50),Point(500,500))
rect.setWidth(4)
rect.setFill('white')
rect.draw(win)

#Sudoku word
S = Image(Point(125,650),"S.gif")
Image.draw(S,win)
U = Image(Point(225,650),"U.gif")
Image.draw(U,win)
D = Image(Point(325,650),"D.gif")
Image.draw(D,win)
O = Image(Point(425,650),"O.gif")
Image.draw(O,win)
K = Image(Point(525,650),"K.gif")
Image.draw(K,win)
U = Image(Point(625,650),"U.gif")
Image.draw(U,win)

##class sudoku():
##
##    def __init__(self,letters,p1x,p1y,picture):
##        self.p1 = Point(p1x,p1y)
##        self.message = message 
##        letters = Image(self.p1,picture)
##        letters.draw(win)
##
##S = sudoku(300,700,"S.gif")

class draw_box():

    def __init__(self,name,p1x,p1y,p2x,p2y):
        self.p1 = Point(p1x,p1y)
        self.p2 = Point(p2x,p2y)
        name = Rectangle(self.p1,self.p2)
        name.draw(win)

class draw_line():

    def __init__(self,name,p1x,p1y,p2x,p2y):
        self.p1 = Point(p1x,p1y)
        self.p2 = Point(p2x,p2y)
        name = Line(self.p1,self.p2)
        name.setWidth(3)
        name.draw(win)
        
class box():

    def __init__(self,boxes,p1x,p1y,message):
        self.p1 = Point(p1x,p1y)
        self.message = message 
        boxes = Text(self.p1,message)
        boxes.setStyle("bold")
        boxes.setSize(18)
        boxes.draw(win)

class text():

    def __init__(self,boxes,p1x,p1y,sizeOfBox):
        self.p1 = Point(p1x,p1y)
        self.sizeOfBox = sizeOfBox 
        boxes = Entry(self.p1,sizeOfBox)
        boxes.setSize(18)
        boxes.setTextColor("blue")
        boxes.draw(win)
        
#drawsbox      
#row1   
boxed1 = draw_box("rand",100,100,50,50)
boxed2 = draw_box("rand",150,100,50,50)
boxed1 = draw_box("rand",200,100,50,50)
boxed2 = draw_box("rand",250,100,50,50)
boxed1 = draw_box("rand",300,100,50,50)
boxed2 = draw_box("rand",350,100,50,50)
boxed1 = draw_box("rand",400,100,50,50)
boxed2 = draw_box("rand",450,100,50,50)
boxed1 = draw_box("rand",500,100,50,50)

#row2
boxed1 = draw_box("rand",100,150,50,50)
boxed2 = draw_box("rand",150,150,50,50)
boxed1 = draw_box("rand",200,150,50,50)
boxed2 = draw_box("rand",250,150,50,50)
boxed1 = draw_box("rand",300,150,50,50)
boxed2 = draw_box("rand",350,150,50,50)
boxed1 = draw_box("rand",400,150,50,50)
boxed2 = draw_box("rand",450,150,50,50)
boxed1 = draw_box("rand",500,150,50,50)

#row3
boxed1 = draw_box("rand",100,200,50,50)
boxed2 = draw_box("rand",150,200,50,50)
boxed1 = draw_box("rand",200,200,50,50)
boxed2 = draw_box("rand",250,200,50,50)
boxed1 = draw_box("rand",300,200,50,50)
boxed2 = draw_box("rand",350,200,50,50)
boxed1 = draw_box("rand",400,200,50,50)
boxed2 = draw_box("rand",450,200,50,50)
boxed1 = draw_box("rand",500,200,50,50)

#row4
boxed1 = draw_box("rand",100,250,50,50)
boxed2 = draw_box("rand",150,250,50,50)
boxed1 = draw_box("rand",200,250,50,50)
boxed2 = draw_box("rand",250,250,50,50)
boxed1 = draw_box("rand",300,250,50,50)
boxed2 = draw_box("rand",350,250,50,50)
boxed1 = draw_box("rand",400,250,50,50)
boxed2 = draw_box("rand",450,250,50,50)
boxed1 = draw_box("rand",500,250,50,50)

#row5
boxed1 = draw_box("rand",100,300,50,50)
boxed2 = draw_box("rand",150,300,50,50)
boxed1 = draw_box("rand",200,300,50,50)
boxed2 = draw_box("rand",250,300,50,50)
boxed1 = draw_box("rand",300,300,50,50)
boxed2 = draw_box("rand",350,300,50,50)
boxed1 = draw_box("rand",400,300,50,50)
boxed2 = draw_box("rand",450,300,50,50)
boxed1 = draw_box("rand",500,300,50,50)

#row6
boxed1 = draw_box("rand",100,350,50,50)
boxed2 = draw_box("rand",150,350,50,50)
boxed1 = draw_box("rand",200,350,50,50)
boxed2 = draw_box("rand",250,350,50,50)
boxed1 = draw_box("rand",300,350,50,50)
boxed2 = draw_box("rand",350,350,50,50)
boxed1 = draw_box("rand",400,350,50,50)
boxed2 = draw_box("rand",450,350,50,50)
boxed1 = draw_box("rand",500,350,50,50)

#row7
boxed1 = draw_box("rand",100,400,50,50)
boxed2 = draw_box("rand",150,400,50,50)
boxed1 = draw_box("rand",200,400,50,50)
boxed2 = draw_box("rand",250,400,50,50)
boxed1 = draw_box("rand",300,400,50,50)
boxed2 = draw_box("rand",350,400,50,50)
boxed1 = draw_box("rand",400,400,50,50)
boxed2 = draw_box("rand",450,400,50,50)
boxed1 = draw_box("rand",500,400,50,50)

#row 8
boxed1 = draw_box("rand",100,450,50,50)
boxed2 = draw_box("rand",150,450,50,50)
boxed1 = draw_box("rand",200,450,50,50)
boxed2 = draw_box("rand",250,450,50,50)
boxed1 = draw_box("rand",300,450,50,50)
boxed2 = draw_box("rand",350,450,50,50)
boxed1 = draw_box("rand",400,450,50,50)
boxed2 = draw_box("rand",450,450,50,50)
boxed1 = draw_box("rand",500,450,50,50)

#row 9
boxed1 = draw_box("rand",100,500,50,50)
boxed2 = draw_box("rand",150,500,50,50)
boxed1 = draw_box("rand",200,500,50,50)
boxed2 = draw_box("rand",250,500,50,50)
boxed1 = draw_box("rand",300,500,50,50)
boxed2 = draw_box("rand",350,500,50,50)
boxed1 = draw_box("rand",400,500,50,50)
boxed2 = draw_box("rand",450,500,50,50)
boxed1 = draw_box("rand",500,500,50,50)

#vertical line
line1 = draw_line("line",200,50,200,500)
line2 = draw_line("line",350,50,350,500)
#horizontal line
line3 = draw_line("line",50,200,500,200)
line3 = draw_line("line",50,350,500,350)

#boxes with numbers
#row1
box1 = box("box",75,75,"1")
box2 = box("box",125,75,"8")
box3 = text("num",175,75,2)
box4 = text("num",225,75,2)
box5 = text("num",275,75,2)
box6 = text("num",325,75,2)
box7 = text("num",375,75,2)
box8 = text("num",425,75,2)
box9 = box("box",475,75,"2")

#row 2
box10 = box("box",75,125,"6")
box11 = text("num",125,125,2)
box12 = text("num",175,125,2)
box13 = box("box",225,125,"4")
box14 = box("box",275,125,"2")
box15 = box("box",325,125,"7")
box16 = box("box",375,125,"9")
box17 = text("num",425,125,2)
box18 = text("num",475,125,2)

#row3
box19 = box("box",75,175,"9")
box20 = box("box",125,175,"4")
box21 = box("box",175,175,"2")
box22 = text("num",225,175,2)
box23 = box("box",275,175,"1")
box24 = box("box",325,175,"8")
box25 = text("num",375,175,2)
box26 = box("box",425,175,"6")
box27 = box("box",475,175,"7")

#row4
box28 = text("num",175,225,2)
box29 = box("box",125,225,"1")
box30 = box("box",175,225,"9")
box31 = text("num",225,225,2)
box32 = box("box",275,225,"8")
box33 = text("num",325,225,2)
box34 = box("box",375,225,"7")
box35 = text("num",425,225,2)
box36 = box("box",475,225,"5")

#row5
box37 = box("box",75,275,"2")
box38 = text("num",125,275,2)
box39 = text("num",175,275,2)
box40 = box("box",225,275,"5")
box41 = text("num",275,275,2)
box42 = box("box",325,275,"9")
box43 = text("num",375,275,2)
box44 = text("num",425,275,2)
box45 = box("box",475,275,"1")

#row6
box46 = box("box",75,325,"7")
box47 = text("num",125,325,2)
box48 = box("box",175,325,"8")
box49 = text("num",225,325,2)
box50 = box("box",275,325,"4")
box51 = text("num",325,325,2)
box52 = box("box",375,325,"6")
box53 = box("box",425,325,"2")
box54 = text("num",475,325,2)

#row7
box55 = box("box",75,375,"8")
box56 = box("box",125,375,"9")
box57 = text("num",175,375,2)
box58 = box("box",225,375,"2")
box59 = box("box",275,375,"5")
box60 = text("num",325,375,2)
box61 = box("box",375,375,"1")
box62 = box("box",425,375,"7")
box63 = box("box",475,375,"3")

#row8
box64 = text("num",75,425,2)
box65 = text("num",125,425,2)
box66 = box("box",175,425,"1")
box67 = box("box",225,425,"8")
box68 = box("box",275,425,"3")
box69 = box("box",325,425,"6")
box70 = text("num",375,425,2)
box71 = text("num",425,425,2)
box72 = box("box",475,425,"4")

#row9
box73 = box("box",75,475,"3")
box74 = text("num",125,75,2)
box75 = text("num",175,475,2)
box76 = text("num",225,475,2)
box77 = text("num",275,475,2)
box78 = text("num",325,475,2)
box79 = text("num",375,475,2)
box80 = box("box",425,475,"5")
box81 = box("box",475,475,"6")
