a=0.05 #original concentration
t=0 #the number of the day
while a<=0.9: #density is lower than the objective '0.9'
    a=a*2
    t+=1  #next day
print('After day'+str(t)+' I can take a break')