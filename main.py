import turtle
import random
from idlelib.macosx import hideTkConsole

screen = turtle.Screen()
screen.screensize(500,500)
screen.bgcolor('red')
t = turtle.Turtle()

t.penup()
t.goto(0,0)
t.pendown()
t.write("El Ler Say", font=("arial", 30, "italic"), align="center")


#intro screen
t.penup()
t.goto(0,100)
t.pendown()
t.write("intro", font=("Ariel", 30, "italic"), align="center")

t.penup()
t.goto(0,-100)
t.pendown()
t.write("things i like", font=("Ariel", 30, "italic"), align="center")

t.penup()
t.goto(0,300)
t.pendown()
screen.addshape("Untitled drawing.gif")
t.shape("Untitled drawing.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,-247)
t.pendown()
screen.addshape("marines YEH.gif")
t.shape("marines YEH.gif")
t.stamp()
t.shape("classic")

round = input("press enter to continue: ")
t.clear()
screen.bgcolor('white')

t.penup()
t.goto(0,-100)
t.pendown()
t.write("favorite foods", font=("Ariel", 30, "italic"), align="center")
t.penup()

t.penup()
t.goto(0,300)
t.pendown()
screen.addshape("frise.gif")
t.shape("frise.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,-300)
t.pendown()
screen.addshape("burger.gif")
t.shape("burger.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,150)
t.pendown()
screen.addshape("pizza.gif")
t.shape("pizza.gif")
t.stamp()
t.shape("classic")


round = input("press enter to continue: ")
t.clear()
screen.bgcolor('gray')


t.penup()
t.goto(0,-100)
t.pendown()
t.write("hobbies", font=("Ariel", 30, "italic"), align="center")

t.penup()
t.goto(0,150)
t.pendown()
screen.addshape("eating.gif")
t.shape("eating.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,300)
t.pendown()
screen.addshape("watching.gif")
t.shape("watching.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,-300)
t.pendown()
screen.addshape("sleeping.gif")
t.shape("sleeping.gif")
t.stamp()
t.shape("classic")

t.penup()
t.goto(0,-200)
t.pendown()
screen.addshape("playing.gif")
t.shape("playing.gif")
t.stamp()
t.shape("classic")

round = input("press enter to continue: ")
t.clear()



screen.bgcolor('red')
t.penup()
t.goto(0,-300)
t.pendown()
t.write("favorite movie", font=("Ariel", 30, "italic"), align="center")

t.penup()
t.goto(0,100)
t.pendown()
screen.addshape("sicario.gif")
t.shape("sicario.gif")
t.stamp()
t.shape("classic")

round = input("press enter to continue: ")
t.clear()
screen.bgcolor('grey')

t.penup()
t.goto(0,-100)
t.pendown()
t.write("favorite sport ", font=("Ariel", 30, "italic"), align="center")

t.penup()
t.goto(0,150)
t.pendown()
screen.addshape("muay thai.gif")
t.shape("muay thai.gif")
t.stamp()
t.shape("classic")

turtle.done()