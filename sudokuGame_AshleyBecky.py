#Sudoku Game: Ashley & Becky
#http://programarcadegames.com/index.php?chapter=introduction_to_graphics
# http://mcsp.wartburg.edu/zelle/python/graphics/graphics.pdf
#click then fill in squares
from graphics import *
import graphics

##pygame.init()


win = graphics.GraphWin("Sudoku", 800, 800)
tiedye = Image(Point(400,400),"tiedye.gif")
Image.draw(tiedye,win)


#image
##yellowJ = Image(Point(750,50),"GracelandYellowjacketsLogo.png")

#base square
rect = Rectangle(Point(50,50),Point(500,500))
rect.setWidth(4)
rect.setFill('white')
rect.draw(win)


#hint box
rect2 = Rectangle(Point(575,100),Point(700,150))
rect2.draw(win)
rect2.setFill('white')
wordHint = Text(Point(637.5,125),"Hint")
wordHint.draw(win)

#drawIn box
rect3 = Rectangle(Point(575, 175),Point(700,225))
rect3.draw(win)
rect3.setFill('white')
drawIn = Text(Point(637.5,200),"Write In")
drawIn.draw(win)

#numbers
one = Text(Point(50,600),"1")
one.draw(win)
one.setStyle("bold")
one.setSize(18)

two = Text(Point(162.5,600),"2")
two.draw(win)
two.setStyle("bold")
two.setSize(18)

three = Text(Point(275,600),"3")
three.draw(win)
three.setStyle("bold")
three.setSize(18)

four = Text(Point(387.5,600),"4")
four.draw(win)
four.setStyle("bold")
four.setSize(18)

five = Text(Point(500,600),"5")
five.draw(win)
five.setStyle("bold")
five.setSize(18)

six = Text(Point(106.25,660),"6")
six.draw(win)
six.setStyle("bold")
six.setSize(18)

seven = Text(Point(218.75,660),"7")
seven.draw(win)
seven.setStyle("bold")
seven.setSize(18)

eight = Text(Point(331.5,660),"8")
eight.draw(win)
eight.setStyle("bold")
eight.setSize(18)

nine = Text(Point(443.75,660),"9")
nine.draw(win)
nine.setStyle("bold")
nine.setSize(18)

#erase box
rect4 = Rectangle(Point(575, 250),Point(700,300))
rect4.draw(win)
rect4.setFill('white')
eraser = Text(Point(637.5,275),"Erase")
eraser.draw(win)

#undo box
rect5 = Rectangle(Point(575,325),Point(700,375))
rect5.draw(win)
rect5.setFill('white')
drawIn = Text(Point(637.5,350),"Undo")
drawIn.draw(win)

#yellow blocks
r1 = Rectangle(Point(50,50),Point(200,200))
r1.draw(win)


r2 = Rectangle(Point(350,50),Point(500,200))
r2.draw(win)


r3 = Rectangle(Point(200,200),Point(350,350))
r3.draw(win)


r4= Rectangle(Point(50,500),Point(200,350))
r4.draw(win)


r5 = Rectangle(Point(500,500),Point(350,350))
r5.draw(win)



#vertical points
p1 = Point(100,50)
p2 = Point(100,500)

p3 = Point(150,50)
p4 = Point(150,500)

p5 = Point(200,50)
p6 = Point(200,500)

p7 = Point(250,50)
p8 = Point(250,500)

p9 = Point(300,50)
p10 = Point(300,500)

p11 = Point(350,50)
p12 = Point(350,500)

p13 = Point(400,50)
p14 = Point(400,500)

p15 = Point(450,50)
p16 = Point(450,500)

#horizontal points
p17 = Point(50,100)
p18 = Point(500,100)

p19 = Point(50,150)
p20 = Point(500,150)

p21 = Point(50,200)
p22 = Point(500,200)

p23 = Point(50,250)
p24 = Point(500,250)

p25 = Point(50,300)
p26 = Point(500,300)

p27 = Point(50,350)
p28 = Point(500,350)

p29 = Point(50,400)
p30 = Point(500,400)

p31 = Point(50,450)
p32 = Point(500,450)

#vertical lines
line1 = Line(p1, p2)
line1.draw(win)

line2 = Line(p3, p4)
line2.draw(win)

line3 = Line(p5, p6)
line3.setWidth(3)
line3.draw(win)

line4 = Line(p7, p8)
line4.draw(win)

line5 = Line(p9, p10)
line5.draw(win)

line6 = Line(p11, p12)
line6.setWidth(3)
line6.draw(win)

line7 = Line(p13, p14)
line7.draw(win)

line8 = Line(p15, p16)
line8.draw(win)

#horizontal lines
line9 = Line(p17, p18)
line9.draw(win)

line10 = Line(p19, p20)
line10.draw(win)

line11 = Line(p21, p22)
line11.setWidth(3)
line11.draw(win)

line12 = Line(p23, p24)
line12.draw(win)

line13 = Line(p25, p26)
line13.draw(win)

line14 = Line(p27, p28)
line14.setWidth(3)
line14.draw(win)

line15 = Line(p29, p30)
line15.draw(win)

line16 = Line(p31, p32)
line16.draw(win)

#First Row
box1 = Text(Point(75,75),"1")
box1.draw(win)
box1.setStyle("bold")
box1.setSize(18)

box2 = Text(Point(125,75),"8")
box2.draw(win)
box2.setStyle("bold")
box2.setSize(18)

box3 = Text(Point(475,75),"2")
box3.draw(win)
box3.setStyle("bold")
box3.setSize(18)

#Second Row
box4 = Text(Point(75,125),"6")
box4.draw(win)
box4.setStyle("bold")
box4.setSize(18)

box5 = Text(Point(225,125),"4")
box5.draw(win)
box5.setStyle("bold")
box5.setSize(18)

box6 = Text(Point(275,125),"2")
box6.draw(win)
box6.setStyle("bold")
box6.setSize(18)

box7 = Text(Point(325,125),"7")
box7.draw(win)
box7.setStyle("bold")
box7.setSize(18)

box8 = Text(Point(375,125),"9")
box8.draw(win)
box8.setStyle("bold")
box8.setSize(18)

#Third Row
box9 = Text(Point(75,175),"9")
box9.draw(win)
box9.setStyle("bold")
box9.setSize(18)

box10 = Text(Point(125,175),"4")
box10.draw(win)
box10.setStyle("bold")
box10.setSize(18)

box11 = Text(Point(175,175),"2")
box11.draw(win)
box11.setStyle("bold")
box11.setSize(18)

box12 = Text(Point(275,175),"1")
box12.draw(win)
box12.setStyle("bold")
box12.setSize(18)

box13 = Text(Point(325,175),"8")
box13.draw(win)
box13.setStyle("bold")
box13.setSize(18)

box14 = Text(Point(425,175),"6")
box14.draw(win)
box14.setStyle("bold")
box14.setSize(18)

box15 = Text(Point(475,175),"7")
box15.draw(win)
box15.setStyle("bold")
box15.setSize(18)

#fourth row
box16 = Text(Point(125,225),"1")
box16.draw(win)
box16.setStyle("bold")
box16.setSize(18)

box17 = Text(Point(175,225),"9")
box17.draw(win)
box17.setStyle("bold")
box17.setSize(18)

box18 = Text(Point(275,225),"8")
box18.draw(win)
box18.setStyle("bold")
box18.setSize(18)

box19 = Text(Point(375,225),"7")
box19.draw(win)
box19.setStyle("bold")
box19.setSize(18)

box20 = Text(Point(475,225),"5")
box20.draw(win)
box20.setStyle("bold")
box20.setSize(18)
#fifth row
box21 = Text(Point(75,275),"2")
box21.draw(win)
box21.setStyle("bold")
box21.setSize(18)

box22 = Text(Point(225,275),"5")
box22.draw(win)
box22.setStyle("bold")
box22.setSize(18)

box23 = Text(Point(325,275),"9")
box23.draw(win)
box23.setStyle("bold")
box23.setSize(18)

box24 = Text(Point(475,275),"1")
box24.draw(win)
box24.setStyle("bold")
box24.setSize(18)

#sixth row
box25 = Text(Point(75,325),"7")
box25.draw(win)
box25.setStyle("bold")
box25.setSize(18)

box26 = Text(Point(175,325),"8")
box26.draw(win)
box26.setStyle("bold")
box26.setSize(18)

box27 = Text(Point(275,325),"4")
box27.draw(win)
box27.setStyle("bold")
box27.setSize(18)

box28 = Text(Point(375,325),"6")
box28.draw(win)
box28.setStyle("bold")
box28.setSize(18)

box29 = Text(Point(425,325),"2")
box29.draw(win)
box29.setStyle("bold")
box29.setSize(18)
#seventh row
box30 = Text(Point(75,375),"8")
box30.draw(win)
box30.setStyle("bold")
box30.setSize(18)

box31 = Text(Point(125,375),"9")
box31.draw(win)
box31.setStyle("bold")
box31.setSize(18)

box32 = Text(Point(225,375),"2")
box32.draw(win)
box32.setStyle("bold")
box32.setSize(18)

box33 = Text(Point(275,375),"5")
box33.draw(win)
box33.setStyle("bold")
box33.setSize(18)

box34 = Text(Point(375,375),"1")
box34.draw(win)
box34.setStyle("bold")
box34.setSize(18)

box35 = Text(Point(425,375),"7")
box35.draw(win)
box35.setStyle("bold")
box35.setSize(18)

box36 = Text(Point(475,375),"3")
box36.draw(win)
box36.setStyle("bold")
box36.setSize(18)

#eighth row
box37 = Text(Point(175,425),"1")
box37.draw(win)
box37.setStyle("bold")
box37.setSize(18)

box38 = Text(Point(225,425),"8")
box38.draw(win)
box38.setStyle("bold")
box38.setSize(18)

box39 = Text(Point(275,425),"3")
box39.draw(win)
box39.setStyle("bold")
box39.setSize(18)

box40 = Text(Point(325,425),"6")
box40.draw(win)
box40.setStyle("bold")
box40.setSize(18)

box41 = Text(Point(475,425),"4")
box41.draw(win)
box41.setStyle("bold")
box41.setSize(18)
#ninth row
box42 = Text(Point(75,475),"3")
box42.draw(win)
box42.setStyle("bold")
box42.setSize(18)

box43 = Text(Point(425,475),"5")
box43.draw(win)
box43.setStyle("bold")
box43.setSize(18)

box44 = Text(Point(475,475),"6")
box44.draw(win)
box44.setStyle("bold")
box44.setSize(18)

inputbox1 = Entry(Point(175,75),2)
inputbox1.draw(win)

inputbox2 = Entry(Point(225,75),2)
inputbox2.draw(win)
