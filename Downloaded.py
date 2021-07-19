import numpy as np
import pandas as pd
path=r'C:\Users\luthr\Documents\Downloads\Downloaded.csv'
df=pd.read_csv(path)
print("Output of replace:")
df["Magnitude"]=df["Magnitude"].replace(0,6)
print(df["Magnitude"].head(50))
print("************************************************************************************")
print("Output of Data Normalization:")
avg=df["Data_value"].mean()
df["Data_value"]=df["Data_value"].replace(np.nan,avg)
df["Data_value"]=df["Data_value"]/(df["Data_value"].max())
print(df["Data_value"])
print("*************************************************************************************")
print("Output of grouping data:")
gkk = df.groupby(['Magnitude', 'Period'])

# Print the first value in each group
print(gkk.first())
print("*************************************************************************************")
print("Output of pivot table:")
print("*************************************************************************************")

