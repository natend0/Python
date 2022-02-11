#Function area 
import math
def areaOfCircle(r):
  	area=math.pi*r**2
 	return area

   def main():
  	x=int(input("Enter the distance for the radius:"))
  	radius=areaOfCircle(x)
 	 print(radius)

   main()
    
    
 #function square root
def mySqrt(n,guessNum):
 	 newguess=n/2
 	 for i in range(n):
    		newguess=(1/2)*((newguess)+(n/newguess))

 return newguess

   def main():
 	 value=mySqrt(3,10)
 	 print(value)
main()

#turtle and functions
import turtle
wn=turtle.Screen()
wn.bgcolor("LightGreen")
def drawSquare(t,side):
  t=turtle.Turtle()
  for length in [50,70,90,110,130] :
    for i in range(side):
     t.forward(length)
     t.left(90)
    for i in range(side):
      t.penup
      t.forward(10)
      t.right(90)
      t.forward(10)
      t.pendown


def main():
 wn=turtle.Screen()
 drawSquare('Tim',4)

main()
