#Boolean expression
x=int(input('Enter Value:'))
if x > 1 or x < 10:
  print(True)

x=int(input('Enter Value:'))
if x > 1 or x < 10:
  print(False)

#math Hypotenuse func
import math
def findHypot (a,b):
  	 c2=math.pow(a,2)+math.pow(b,2)
  	 c= math.sqrt(c2)
  	 return c

side1= 3 
side2= 4

result=findHypot(side1,side2)
print('The length of the Hypotenuse is:',result)


#Function to determine if Odd
def isOdd(n):
 	  if n % 2:
   	   return True
 	  else:
   	   return False

x=int(input('Enter value:'))
result=isOdd(x)
print('The Value is',result)


#Leap Year Function
def isLeapYear(year):
 	 if year % 4 == 0 and year % 400 != 0:
  	  return True
  	 else:
   	  return False

x=int(input('Enter year:'))
result=isLeapYear(x)
print('The Value is',result)


#Is password valid function
def isPwdValid(p):
  	 if len(p) > 5 and len(p) < 13 and ('@' in p or '#' in p or '$' in p):
    	  return True
 	 else:
    	  return False

x=input('Enter Password:')
result=isPwdValid(x)
print('The Value is',result)



#Turtle function 
import turtle

def drawTriangle(t,side):
  for i in  ['Red','Green','Red','Green','Red','Green','Red','Green','Red','Green']:
    t.color(i)
    for i in range (2):
     t.forward(side)
     t.left(120)
    for i in range (1):
      side=side+20
      t.forward(side)
      t.left(120)

wn=turtle.Screen()
t=turtle.Turtle()
side=50
drawTriangle(t,side)


