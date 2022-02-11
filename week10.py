#Pay
def grossPay(h,p):
    if h > 40:
     base=40*p
     overtime_hours=h-40
     overtime_pay=overtime_hours*(1.5*p)
     total_pay=base+overtime_pay
    else:
     total_pay=h*p
    return total_pay

   hours=int(input('Enter how many hours worked:'))
   pay=int(input('Enter the pay rate:'))
   weekly_gross=grossPay(hours,pay)
   print(weekly_gross)

  #Multiple by 2 until greater than 10,000
  count = 0 
while x < 10000:
 x= x * 2
 count=count+1
print (x, 'is greater than 10,000 after', count, 'multiplication operations')


#Multiply within an Array: 
numbs=[ 2, 5, 8, 4, 3, 6, 7, 9]
sum=0
total=0
for i in numbs:
  for j in numbs:
    sum = i * j 
   	    total=sum+total
	
print('The total is:',total)


#Difference between largest and smallest values
difflist=[170,240,2,30,4]
x=0
y=1000000
for i in difflist:
  	 if i > x:
    	  x=i
    
for i in difflist:
 	 if i < y:
    	  y=i

result= x-y
print('The difference between the highest and lowest is:',result)


#Computer dice game
import random
def rolldice(is_losing):
 	 while is_losing == True:
  	  computer_roll=random.randrange(1,7)
   	  print('The computer rolled:',computer_roll)
 	  response=input('Do you want to roll the dice?:')
        if response  in ['y','Y']:
         user_roll=random.randrange(1,7)
         if user_roll == computer_roll:
          print('I rolled:',user_roll,'\n I WIN!')
          return False
         else:
         print('I rolled:', user_roll)
       return True

rolldice(True)

