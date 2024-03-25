uk_cities=[0.56,0.62,0.04,9.7] # UK CITY POPULATION
cn_cities=[0.58,8.4,22.2,29.9] #CN CITY POPULATION
uk_cities.sort() #sort the population of uk cities and china cities
cn_cities.sort()
print(uk_cities)
print(cn_cities)
cn=('haining','hangzhou','shanghai','beijing')
uk=('Edinburgh','Glasgow','Stirling','London')
import matplotlib.pyplot as plt
plt.bar(uk,uk_cities) # draw a bar
plt.show()
plt.clf() 
plt.bar(cn,cn_cities)
plt.show()
plt.clf() 