#Count even numbers in range 
def countEven (x,y):
  	 count=0
  	 for i in range(x,y):
      	  if i % 2 == 0:
         count=count+1
  	 return count  

firstNumber=int(input("Enter first number:"))
secondNumber=int(input("Enter second number:"))

answer=countEven(firstNumber,secondNumber)

print(answer, 'Even Numbers between', firstNumber, 'and', secondNumber)


#convert dog age to human age
def age(a):
 	 if a <= 2:
    	  dog_age= a*10.5
 	 else:
    	  dog_age=21+ (4*(a-2))
 	 return dog_age

input_age=float(input("Enter dog age to convert to human age:"))
answer=age(input_age)
print(input_age, 'dog years is equal to', answer, 'human years')


#calculate letters and digits in a string
c=input("Enter an English Sentece with Letters and Digits:")
alpha=0
digit=0
for i in c:
  	 if i.isdigit():
  	  digit=digit+1
  	 elif i.isalpha():
    	  alpha=alpha+1

print('Letters',alpha)
print('digits:',digit)


#How many days in a month? 
def calcDays(month,year):
  	 if month in (1,3,5,7,8,10,12):
    	  days=31
 	 elif month in(4,6,9,11):
   	  days=30
 	 elif month == 2:
   	  if year % 4 == 0 and year % 400 != 0: 
     	   days=29
   	  else:
     	   days=28  
  	 return days 

input_month=int(input('Enter the month format MM:'))
input_year=int(input('Enter the year format YYYY:'))

total_days= calcDays(input_month, input_year)
print(total_days, 'days in month', input_month, 'of year', input_year)



#Random turtles:
import turtle
import random
wn=turtle.Screen()
circle=turtle.Turtle()
def random_circles(x,y):
 	 for i in range(20):
   	 circle.penup()
   	 circle.setx(random.randrange(-100,100))
   	 circle.sety(random.randrange(-100,100))
   	 circle.pendown()
   	 radius =(random.randrange(x,y))
   	 if radius < 21:
     	  circle.color('Red')
     	  circle.circle(radius)
   	 elif radius >20 and radius <30:
     	  circle.color('Blue')
     	  circle.circle(radius) 
   	 elif radius < 40:
     	  circle.color('Green')
     	  circle.circle(radius)    

random_circles(10,40)





