import pandas as pd
import numpy as np
df=pd.read_csv('climb_data.csv')
df['ROC_mps']=df.ROC_ftps*0.3048
df['V_ms']=df.V_knots*0.5144
df['gamma_deg']=np.degrees(np.arcsin(df.ROC_mps/df.V_ms))
print(df)
