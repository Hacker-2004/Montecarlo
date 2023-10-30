import random

def roll():
    return random.randint(1,6)

def turns():
    d=roll()
    b=roll()
    if d==b:
        d=roll()
        b=roll()
        if d==b:
            d=roll()
            b=roll()
            if(d==b):
                return 3
            else:
                return 2
        else:
            return 0
    else:
        return 0
runs=100000
nones=0
singl=0
doubl=0
triples=0
outcomes={0:0,1:0,2:0,3:0}
for i in range(runs):
    if(turns()==0):
        nones+=1
    elif(turns()==1):
        singl+=1
    elif(turns()==2):
        doubl+=1
    else:
        triples+=1
for i in range(runs):
    outcomes[turns()]+=1
for numboubles in outcomes:
    print(numboubles,outcomes[numboubles]/runs)
print(nones,singl,doubl,triples)
def flip():
    side=["H","T"]
    return random.choice(side)
def game(sec1,sec2):
    outcomes=""
    winner=0
    while True:
        outcomes=outcomes+flip()
        if outcomes[:-3]== sec1:
            winner= 1
        if outcomes[:-3]== sec2:
            winner= 2
    return winner
tails=100000
wins=0
for i in range(tails):
    winner=game("HHT","THH")
    if winner==1:
        wins+=1
print(wins/tails,(tails-wins)
)
