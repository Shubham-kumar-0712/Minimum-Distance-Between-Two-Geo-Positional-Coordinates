# Agenda is to map the content of  df1 with df2 such that geo position distance of df1 is least with the index of df2

import pandas as pd
import haversine as hs
import mysql.connector

df1= pd.read_csv('gis_direct_access.csv')
df1= pd.DataFrame(df1)

df2= pd.read_csv('sample_plant1.csv')
df2= pd.DataFrame(df2)
a=(0,0)
b=(0,0)
c=0
d=[0,0,0,0,0,0]
data=[]
for i in range(len(df2)):
    a=(df2.loc[i,"latitude"],df2.loc[i,"longitude"])
    for j in range(len(df1)):
        b=(df1.loc[j,"latitude"],df1.loc[j,"longitude"]) #calculating distance for every element of df1
        c=hs.haversine(a,b)
        d=[df2.loc[i,"Project_id"],df2.loc[i,"Project_name"],c,df1.loc[j,"cluster"],df1.loc[j,"plant_id"],df1.loc[j,"name"]]
        data.append(d)


df = pd.DataFrame(data, columns=['Project_id','Project_name','distance','cluster','Direct_access_plant','direct_access_plant_name']) #creating new data frame
df1 = df.loc[df.groupby('Project_id').distance.idxmin()] # Finding the row which has minimum distance grouping by project id
df1.to_csv('mapped.csv')
print(df1)
print("shubham")
     
