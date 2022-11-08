import random

parents = ['Bre1', 'Bre2', 'Bre3', 'Randy1', 'Randy2', 'Randy3', 'Randy4', 'Steve1', 'Steve2', 'Steve3', 'Steve4', 'Steve5','Chris','Nate1', 'Nate2','Katie1', 'Katie2', 'Katie3']
parentlist = ['bre','randy', 'steve', 'chris', 'nate', 'kate']
kids = ['Ethan', 'Connor', 'Genevieve', 'Remy', 'Zayne', 'Michelle', 'Glory', 'Audrey', 'Emma', 'Arya', 'Andrew', 'Kinsley', 'Colton', 'Lilly', 'Elena', 'Camila', 'Julian', 'Ragnar']
bre = ['Ethan', 'Connor', 'Genevieve']
randy = ['Remy', 'Zayne', 'Michelle', 'Ragnar']
steve = ['Glory', 'Audrey', 'Emma', 'Andrew', 'Arya']
chris = ['Kinsley']
nate = ['Colton', 'Lilly' ]
katie= ['Elena','Camila', 'Julian']



for i in parents:
    if i in ['Bre1', 'Bre2', 'Bre3']:
        pick = random.choice(kids)
        while pick in bre:
            pick = random.choice(kids)
            #print(pick, "trying again for", i)
        print(i ,' has to buy pjs for', pick)
        kids.remove(pick)

    elif i in ['Randy1', 'Randy2', 'Randy3', 'Randy4']:
        pick = random.choice(kids)
        while pick in randy:
            pick = random.choice(kids)
            #print(pick, "trying again for", i)
        print(i ,' has to buy pjs for', pick)
        kids.remove(pick)

    elif i in ['Steve1', 'Steve2', 'Steve3', 'Steve4', 'Steve5']:
        pick = random.choice(kids)
        while pick in steve:
            pick = random.choice(kids)
            #print(pick, "trying again for", i)
        print(i ,' has to buy pjs for', pick)
        kids.remove(pick)

    elif i in ['Chris']:
        pick = random.choice(kids)
        while pick in chris:
            pick = random.choice(kids)
            #print(pick, "trying again for", i)
        print(i ,' has to buy pjs for', pick)
        kids.remove(pick)

    elif i in ['Nate1', 'Nate2']:
        pick = random.choice(kids)
        while pick in nate:
            pick = random.choice(kids)
            #print(pick, "trying again for", i)
        print(i ,' has to buy pjs for', pick)
        kids.remove(pick)

    elif i in ['Katie1', 'Katie2', 'Katie3']:
        pick = random.choice(kids)
        while pick in katie:
            pick = random.choice(kids)
            #print(pick, "trying again for", i)
        print(i ,' has to buy pjs for', pick)
        kids.remove(pick)


