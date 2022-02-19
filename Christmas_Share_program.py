import random
def FamilyShare(x):
  response=input('Select Enter to run and stop to stop:')
  while response not in ['stop','Stop']:
    Family_Order=['Mom','Dad','Sister','Brother','Cousin','Uncle','Aunt','Grandma', 'Grandpa']
    order=0
    for i in range(x):
      sample=random.sample(Family_Order,8)
    print('The random sharing order is:')
    for i in sample:
      order=order+1
      print(order,':',i)
    response=input('Select Enter to run and stop to stop:')


times_to_run=int(input('Enter number of times to shuffle:'))
FamilyShare(times_to_run)
