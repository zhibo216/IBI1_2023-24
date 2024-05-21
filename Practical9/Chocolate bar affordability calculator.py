def Cbac(a,b): # a function calculating the number of chocolate you can buy and your left money 
    n=a//b #the number of chocolate 
    c=a%b  #the change
    return f'you can buy {n} chocolate and have {c} money left'
a=int(input('money you have:'))  #the total money
b=int(input('the chocolate prize:')) # the prize for each chocolate
print(Cbac(a,b))