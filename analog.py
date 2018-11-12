import turtle
import time

#Create screen 
wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.title("Simple Analog clock by Maryam")
wn.tracer(0)
##########################################

#Create pen of drawing
pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)
##########################################

#Draw border of clock
def draw_clock(h,m,s,pen):
	pen.up()
	pen.goto(0,210)
	pen.setheading(180)
	pen.color("green")
	pen.pendown()
	pen.circle(210)
	
	#Draw lines of hours
	pen.penup()
	pen.goto(0,0)
	pen.setheading(90)
	for i in range(12):
		pen.fd(190)
		pen.pendown()
		pen.fd(20)
		pen.penup()
		pen.goto(0,0)
		pen.rt(30)
		
		
	#Draw hour hand
	pen.penup()
	pen.goto(0,0)
	pen.color("white")
	pen.setheading(90)
	angle=(h/12)*360
	pen.rt(angle)
	pen.pendown()
	pen.fd(100)
	
	#Draw minutes hand
	pen.penup()
	pen.goto(0,0)
	pen.color("blue")
	pen.setheading(90)
	angle=(m/60)*360
	pen.rt(angle)
	pen.pendown()
	pen.fd(160)
	
	#Draw seconds hand
	pen.penup()
	pen.goto(0,0)
	pen.color("yellow")
	pen.setheading(90)
	angle=(s/60)*360
	pen.rt(angle)
	pen.pendown()
	pen.fd(50)

while True:
	h=int(time.strftime("%I"))
	m=int(time.strftime("%M"))	
	s=int(time.strftime("%S"))	
	draw_clock(h,m,s,pen)
	wn.update()
	time.sleep(1)
	pen.clear()
#This line to allow screen to be exit 
wn.mainloop()


