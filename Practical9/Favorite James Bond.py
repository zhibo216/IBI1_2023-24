def FJB(a): # a function about Favourite James Bond 
    b=a+18 #the year when he is 18                            for example,for a man born in 1966, when he is 18, it is 1984
    if 1973<=b<=1986:    #different actors for different years
        c='Roger Moore'
    elif 1987<=b<=1994:                                        #in 1984,it was Roger Moore who played the character, so the actor is Roger Moore
        c='Timothy Dalton'
    elif 1995<=b<=2005:
        c='Pierce Brosnan'
    elif 2006<=b<=2021:
        c='Daniel Craig'
    else:
        c='None'
    return c
a=int(input('your birth year:')) #represent the birth year
print('the individual actor is:'+FJB(a))                                                        
