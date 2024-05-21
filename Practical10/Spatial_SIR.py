import numpy as np
import matplotlib.pyplot as plt #import necessary libraries
population = np. zeros((100,100)) #make array of all population
outbreak = np.random.choice(range(100),2) #choose a initial point 
population [outbreak[0],outbreak[1]]=1
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', vmin=0, vmax=2, interpolation='nearest')
plt.colorbar()  # show color bar
plt.show()
beta=0.3 #infected rate
gamma=0.05 #recover rate
for day in range(1,101):
    # find infected points
    infectedIndex = np.where(population==1)
    # loop through all infected points
    for i in range(len(infectedIndex[0])):
        # get x, y coordinates for each point
        x = infectedIndex[0][i]
        y = infectedIndex[1][i]
        # infect each neighbour with probability beta
        # infect all 8 neighbours:
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                # make sure do not infect the point itself
                if (xNeighbour,yNeighbour) != (x,y):
                    # make sure the point is in the edge
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        # make sure only uninfected points can be infected
                        if population[xNeighbour,yNeighbour]==0:
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        if population[x,y]==1:
            population[x,y]=np.random.choice(range(1,3),1,p=[1-gamma,gamma])[0]
    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', vmin=0, vmax=2, interpolation='nearest')
    plt.title(f'DAY {day}')
    plt.show()

