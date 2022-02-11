#Math Power
import math
a=int(input("Enter integer a:"))
b=int(input("Enter integer b:"))
a_power_b= math.pow(a,b)
print(a_power_b)

#Random
import random
for i in range(50):
  		value=random.randrange(0,10)
  		print(value)

#Math and Random

import random
import math
total=0
t=10000
for i in range(t):
  	  y=random.uniform(10,100)
 	  total=total+y
avg=(total/t)
x=math.floor(avg)
print(x)

#random days of the week 
import random
days_of_week=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
ran_day=random.choice(days_of_week)
print(ran_day)


#math Square root loop 
import math
total=0
for i in range(1,11):
 	 sq=math.sqrt(i)
 	 total=total+sq
ceil=math.ceil(total)
print(ceil)

