#Sentence in UPPERs 
def sentCheck(x):
  	 null=''
  	 while x is not null: 
    	  return(x.upper())
  	 else:
    	  return '"End" and quit' 
    
sentence= input('Enter a sentence:')
print(sentCheck(sentence))

#Fibonocci sequence 
n=int(input('Enter n value:'))
x=0
y=1
z=0
for i in range(n):
 z=x
 print(z)
 	 z=x+y
 x=y
 y=z
  
  
  #Investment Interest
  
start=float(input('Enter starting balance:'))
target=float(input('Enter target balance:'))
rate=float(input('Enter interest rate:'))
period=0
while start < target:
 	 start=(start * (1 + rate))
  	 period= period+1

print('The invesetment period is:', period)

#Acceptable answer checker
response=input('Enter yes or no:')
while response not in ['Y', 'y', 'yes', 'YES', 'N', 'n', 'no', 'NO']:
 	 print('That is not an acceptable answer, try again :)')
 	 response=input('Enter yes or no:')
  
  #Enter number greater than 100 
  number=int(input('Enter a number greater than 100:'))
while number <101:
    another_number=int(input('Enter another number to get above 100:'))
    number=another_number+number




