a=0.05 #original concentration
t=0 #the number of the day
while a<=0.9: #density is lower than the objective '0.9'
    a=2*a
    t+=1  #next day
    print('the cell density on the end of day'+str(t)+' is '+str(a))
print('After day'+str(t-1)+' I can take a break') #I should leave the lab before the density is over '0.9'!