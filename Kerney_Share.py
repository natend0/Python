import random
def KerneyShare(x):
  response=input('Select Enter to run and stop to stop:')
  while response not in ['stop','Stop']:
    Kerney_Order=['Mom','Dad','Bre','Randy','Steve','Chris','Nate','Katie']
    order=0
    for i in range(x):
      sample=random.sample(Kerney_Order,8)
    print('The random sharing order is:')
    for i in sample:
      order=order+1
      print(order,':',i)
    response=input('Select Enter to run and stop to stop:')


times_to_run=int(input('Enter number of times to shuffle:'))
KerneyShare(times_to_run)
