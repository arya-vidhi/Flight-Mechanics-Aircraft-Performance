import pandas as pd
import numpy as np
from scipy.stats import linregress
df=pd.read_csv('cruise_data.csv')
rho=1.225;S=16.16;W=1633*9.81
df['V_ms']=df.V_knots*0.5144
df['Power_W']=df.BHP_HP*745.7
df['PV']=df.Power_W*df.V_ms
df['V4']=df.V_ms**4
m,c,*_=linregress(df.V4,df.PV)
print(m,c)
