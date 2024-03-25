a=8 #sleepingtime
b=6  #classestime
c=3.5  #studying time
d=2    #tv time 
e=1    #music time
f=24-a-b-c-d-e #f=other time
dict={'sleeping':a,'C':b,'studying':c,'tv':d,'music':e,'other':f}
print(dict)
s='sleeping' #changeable
activity=['sleeping','classes','studying','tv','music','other']
if s in activity:
    print(dict[s])
else:
    print(dict['other'])
import matplotlib.pyplot as plt
time_day = [a,b,c,d,e,f]
else1 = [0, 0, 0, 0, 0, 0]
activity=['sleeping','classes','studying','tv','music','other']
plt.pie(time_day, labels =activity, startangle = 90, explode=else1)
plt.show()
plt.clf()
