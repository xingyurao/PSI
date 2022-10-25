# @Time    : 2022/10/22 9:51
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : run_add.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np

from PSI_algorithms.N_plus_M_Step import *
from PSI_algorithms.Data_Process import *
from PSI_algorithms.N_Step import *

form_12, _ = n_step(step=12)
form_84, _ = N_M_step(step=8, over_sample_points=4)
form_66, _ = N_M_step(step=6, over_sample_points=6)
# %%
form_12ave = np.nanmean(form_12, 1)
form_84ave = np.nanmean(form_84, 1)
form_66ave = np.nanmean(form_66, 1)
a=np.array([])
b=np.array([])
c=np.array([])
for i in np.arange(0,100000-1,1):
    a=np.append(a,form_12ave[i+1]-form_12ave[i])
    b = np.append(b, form_84ave[i + 1] - form_84ave[i])
    c = np.append(c, form_66ave[i + 1] - form_66ave[i])
std_12=np.std(a)
std_84=np.std(b)
std_66=np.std(c)

#%%
plt.figure()
plt.hist(a,bins=10000)
plt.hist(c,bins=10000)
plt.show(block=1)
