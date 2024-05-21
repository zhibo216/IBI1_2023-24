import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
N = 10000 # The whole population
beta=0.3 #infection probability upon contact
gamma=0.05 #recovery probability
plt.figure(figsize=(6,4),dpi=150)

for q in range(0,101,10):
    S=N-int(q/100*N) #q/100 represents the vaccination rate, while q/100*N represents the population of vaccination people
    I=1 #initial infected number
    R=0 #initial recover number 
    I_arr=[I]
    for i in range (1,1000):
        infect_rate=beta*(I/N) #update the infected rate
        Infect_list=np.random.choice([0,1],S,p=[1-infect_rate,infect_rate]) #update the infected population
        Sum0=Infect_list.sum() #calculate the number of n recent infected people
        S=S-Sum0 #update the number of susceptible people
        I=I+Sum0 #update the number of infected peoplr
        recover_list=np.random.choice([0,1],I,p=[1-gamma,gamma]) #update the recovered population
        Sum1=recover_list.sum() #calculate the m=number of recovered people
        I=I-Sum1 #update the number of infected people
        R=R+Sum1 #update the number of recovered people
        I_arr.append(I)
    time=[i for i in range (1,1001)]
    plt.plot(time, I_arr,label='{}%'.format(q),color=cm.viridis(q*3))
plt.xlabel('time')
plt.ylabel('number of infected people')
plt.title('SIR Model with different vaccination rates')
plt.legend()
plt.show()


plt.savefig("SIR Model with Different Vaccination Rates.png",type="png")#save the fig