##Miles per gallon calculator
miles= int(input("Enter the number of miles driven:"))
gallons=int(input("Enter the number of gallons used:"))
miles_per_gallon=miles/gallons

print("MPG is", miles_per_gallon)

#Variable switch 
a = int(input("Enter variable a:")) 
b = int(input("Enter variable b:")) 
print(a,b)
a = a + b  
b=a-b
a=a-b
print(a,b)

#Vacation days of the week problem
start = int(input("Enter the starting day number:")) 
length = int(input("Enter the nights of stay:")) 
return_day = (start + length) % 7
print("return on day", return_day)
