#For loop
for i in range(1,10,2):
 	 print('Number', i)

#for loop adding odd numbers
t=0
for i in range(1,1000,2):
  		t=(t+i)
print(t)


#for loop creating *
n = int(input("Enter the number of rows:")) 
for i in range(0,n,1):
  for j in range(i):   
    print ('*', end="")   
    print('')     
for i in range(n, 0, -1):   
  for j in range(i):   
    print('*', end="")   
    print('')   


#Turtle shapes
import turtle
wn=turtle.Screen()
polygon=turtle.Turtle()
sides= int(input("Enter number of sides:"))
length = int(input("Enter length of sides:"))
color = input("Enter color:")
fillcolor = input("Enter fill color:")
polygon.color(color)
polygon.fillcolor(fillcolor)
polygon.begin_fill()
for i in range(sides):
  	  polygon.left(360/sides)
   	  polygon.forward(length)
polygon.end_fill()


#Turtle Clock
import turtle
wn=turtle.Screen()
wn.bgcolor("LightGreen")
clock=turtle.Turtle()
clock.color("blue")
clock.shape("turtle")
clock.stamp()
clock.penup()
for r in range(12):
  clock.forward(150)
  clock.pendown()
  clock.forward(25)
  clock.penup()
  clock.stamp()
  clock.forward(-175)
  clock.right(360/12)

