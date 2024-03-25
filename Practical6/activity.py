a=8 #sleepingtime
b=6  #classestime
c=3.5  #studying time
d=2    #tv time 
e=1    #music time
f=24-a-b-c-d-e #f=other time
import matplotlib.pyplot as plt
time_day = [a,b,c,d,e,f]
else1 = [0, 0, 0, 0, 0, 0]
activity=['sleeping','classes','studying','tv','music','other']
plt.pie(time_day, labels =activity, startangle = 90, explode=else1)
plt.show()
plt.clf()
