a=40
b=36
c=30
d=a-b;e=a-c
if d>e:
    print('d>e,training only by running is the better method')
elif d<e:
    print('d<e,training by combining strenth exercise and running is the better method')
else:
    print('d=e') 
    #d<e,training by combining strenth exercise and running is the better method

X=True
Y=False
W=not (X and Y) and (X or Y)
print(W) #True