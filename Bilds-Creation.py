# @Time    : 2022/10/4 16:05
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Bilds-Creation.py
# @Software: PyCharm

# create bild of comparison with different steps
import matplotlib.pyplot as plt
from n_step_algorithms.n_step_Algorithms import *
import numpy as np

# 3 step PSI
phase_interval = (0, np.pi * 2)
_, m_std_3 = n_step_single_line(step=3, phase=phase_interval)
_, m_std_4 = n_step_single_line(step=4, phase=phase_interval)
#_, m_std_5 = n_step_single_line(step=5, phase=phase_interval)
#_, m_std_8 = n_step_single_line(step=8, phase=phase_interval)

m_std_3 = outlier_delete(m_std_3)
m_std_4 = outlier_delete(m_std_4)
#m_std_5 = outlier_delete(m_std_5)
#m_std_8 = outlier_delete(m_std_8)

#%%
fig = plt.figure()
plt.style.use('scientific')
plt.plot(m_std_3, label='3-step')
plt.plot(m_std_4, label='4-step')
#plt.plot(m_std_5, label='5-step')
#plt.plot(m_std_8, label='8-step')

plt.title('comparison with different sampling periods')
plt.xlabel('startphase')
plt.ylabel('standard deviation')
plt.legend(loc='upper right')
plt.tight_layout()
plt.show(block=True)
