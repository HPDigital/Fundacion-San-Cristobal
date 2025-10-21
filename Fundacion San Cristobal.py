"""
Fundacion San Cristobal
"""

#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd 
import numpy as np 


# In[11]:


df_3G = pd.read_excel(r'C:\Users\HP\Desktop\TESORESRA\Personal desvinculacion\3G _FIRE&HIRE.xlsx')
df_ESMI = pd.read_excel(r'C:\Users\HP\Desktop\TESORESRA\Personal desvinculacion\ESMI_FIRE&HIRE.xlsx', header=2)
df_FSC = pd.read_excel(r'C:\Users\HP\Desktop\TESORESRA\Personal desvinculacion\FSC_FIRE&HIRE.xlsx')
df_RESUMEN_DESVINCULACION = pd.read_excel(r'C:\Users\HP\Desktop\TESORESRA\Personal desvinculacion\RESUMEN_DESVINCULACION.xlsx')


# In[14]:


df_ESMI.drop('Unnamed', axis=0)


# In[ ]:




