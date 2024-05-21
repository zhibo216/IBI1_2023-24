import numpy as np
import matplotlib.pyplot as plt
N = 10000 # The whole population size
S=N-1 #initial susceptible number
beta=0.3 #infection probability upon contact
gamma=0.05 #recovery probability
I=1 #initial infected number
R=0 #initial recover number
S_arr=[S]
I_arr=[I]
R_arr=[R]

for i in range (999): #1000 points include the intitial one
    infect_rate=beta*(I/N) #update the infected rate
    Infect_list=np.random.choice([0,1],S,p=[1-infect_rate,infect_rate]) #update the infected population
    Sum0=Infect_list.sum() #calculate the number of n recent infected people
    S=S-Sum0 #update the number of susceptible people
    I=I+Sum0 #update the number of infected peoplr
    recover_list=np.random.choice([0,1],I,p=[1-gamma,gamma]) #updare the recovered population
    Sum1=recover_list.sum() #calculate the m=number of recovered people
    I=I-Sum1 #update the number of infected people
    R=R+Sum1 #update the number of recovered people
    S_arr.append(S) #update S,I,R
    I_arr.append(I)
    R_arr.append(R)

time=[i for i in range (1000)]
plt.figure(figsize=(6,4),dpi=150)
plt.plot(time, S_arr, label='Susceptible')
plt.plot(time, I_arr, label='Infected')        #draw the plot of Susceptible,infected,recovered population
plt.plot(time, R_arr, label='Recovered')
plt.xlabel('time')
plt.ylabel('the population')
plt.title('SIR Model')
plt.legend()
plt.show()

plt.savefig("SIR.png")#save






