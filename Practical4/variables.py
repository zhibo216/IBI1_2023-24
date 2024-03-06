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

X=True;Y=False;W=X or Y
print('X','Y','W')
print(X,Y,W)
print('W is '+str(W)) 
#X Y W
#True False True
#W is True