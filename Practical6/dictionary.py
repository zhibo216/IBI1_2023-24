a=8 #sleepingtime
b=6  #classestime
c=3.5  #studying time
d=2    #tv time 
e=1    #music time
f=24-a-b-c-d-e #f=other time
dict={'sleeping':a,'C':b,'studying':c,'tv':d,'music':e,'other':f}
s='sleeping' #changeable
activity=['sleeping','classes','studying','tv','music','other']
if s in activity:
    print(dict[s])
else:
    print(dict['other'])

