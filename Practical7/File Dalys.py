import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir(r'C:\Users\giggity\Desktop\2023-24 IBI1 notes\IBI1_2023-24\Practical7')
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
print(dalys_data.iloc[0:101:10,3]) #fourth column every 10th row from first row to first 100 rows

my_rows=[]
a=dalys_data.loc[:,'Entity']
for i in a:
    if i=='Afghanistan':
        my_rows.append(True)
    else:
        my_rows.append(False)
print(dalys_data.loc[my_rows, 'Entity'])

china_data=dalys_data["Entity"]=="China" 
print(dalys_data.loc[china_data,:]) #we can found that DALYs in 2019 was 22270.51
b=np.array([dalys_data[china_data].iloc[:,3]])
print('the mean DALYS in China is '+str(np.mean(b)))   # The mean is 30677.69 DALYs in China in 2019 was less than the mean DALYS in China
print('DALYs in China in 2019 was less than the mean')
x=dalys_data[china_data].Year
y=dalys_data[china_data].DALYs
plt.plot(x,y, 'b+')
plt.xticks(x,rotation=-45)
plt.xlabel('Year',color='red',fontsize='18')
plt.ylabel('DALYs',color='red',fontsize='18')
plt.show()


dalys_2019=dalys_data[dalys_data['Year']==2019]
print(dalys_2019)
dalys_2019_=[]
for i in dalys_2019.DALYs:
    if i<18000:
        dalys_2019_.append(True)
    else:
        dalys_2019_.append(False)
if True in dalys_2019_:
    print(dalys_2019.loc[dalys_2019_,'Entity'])
    print('countries above had DALYS lower than 18000 in 2019')
else:
    print('There are no place where DALYs was below 18000 in 2019')
