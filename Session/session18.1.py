# Turtules 
# use this coomand for install turtle pip3 install turtles
# turtle is like the tkinter 
# turtle use for creating games using python [in the tinker you can create application using tkinter]
# write inside the opening and closing tags as always 

# for check turtle install or not use given below command [if output is blank then it is install otherwise some error occures]
import turtle

# when run only opening and closing tags then i window will open you all the output is shows theres
# at the center of the screen you can find a one arror using arror you can create design many more 
# [like the arror is your pen]

t = turtle.Turtle()         #opening tag

# using forward your pen move forward to 100
# t.forward(100)
# using right and left you can move the arrow angle [we enter in degrees]
# t.right(90)

# now we create a square

t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)


# now we create a square using for loop
# enter the side inside the range(side) The square has 4 side so we enter 4
# for i in range(4):
#     t.forward(100)    #for move the pen
#     t.right(90)       #for rotate or change angle of pen enter in degree



# now create a star
# for i in range(5):
#      t.forward(100)
#      t.right(144)

# now create 2 star

# for i in range(5):
#      t.forward(100)
#      t.right(144)

# # we use pendown() and penup() for bcz if we dont then we use backword for space-between two stars there in create a line 
# # means when we backword pen is down on the screen that create a lines so remove that line we use penup() and pendown() 
# t.penup()
# t.backward(200)
# t.pendown()

# for i in range(5):
#      t.forward(100)
#      t.right(144)

# if you want to speed of for pen use given below
#t.speed(1)
#t.speed(3)


# created a rangolii 
# t.speed(100)


# li1 = ["red","green","yellow","blue"]
# for i in range(360):
#     t.pencolor(li1[i%len(li1)])
#     t.forward(i)
#     t.right(140)


# t.speed(30)
# t.circle(90)


# if you nwant change a pen icon use spane()
# now initiate of arror there is a turtule icon
# t.shape("turtle")

# if you want to change the pen color and whidth of pen use this

# t.pencolor("green")
# t.pensize(10) 

turtle.mainloop()           #closing tags
 