# @Time    : 2022/10/4 16:05
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Bilds-Creation.py
# @Software: PyCharm

# create bild of comparison with different steps
import matplotlib.pyplot as plt
from n_step_algorithms.n_step_Algorithms import *
import numpy as np

# %% comparison with different sampling frequency
phase_interval = (0, np.pi * 2)
_, m_std_3 = n_step_single_line(step=3, phase=phase_interval)
_, m_std_4 = n_step_single_line(step=4, phase=phase_interval)
_, m_std_8 = n_step_single_line(step=8, phase=phase_interval)
_, m_std_20 = n_step_single_line(step=20, phase=phase_interval)

m_std_3 = outlier_delete(m_std_3)
m_std_4 = outlier_delete(m_std_4)
m_std_8 = outlier_delete(m_std_8)
m_std_20 = outlier_delete(m_std_20)
# create the graph
fig = plt.figure()
plt.style.use('scientific')
plt.plot(m_std_3, label='3-sampling points', color='green')
plt.plot(outlier_delete(n_Step_theoretical_std(step=3)), 'k--')

plt.plot(m_std_4, label='4-sampling points', color='blue')
plt.plot(outlier_delete(n_Step_theoretical_std(step=4)), 'k--')

plt.plot(m_std_8, label='8-sampling points', color='red')
plt.plot(outlier_delete(n_Step_theoretical_std(step=8)), 'k--')

plt.plot(m_std_20, label='20-sampling points', color='yellow')
plt.plot(outlier_delete(n_Step_theoretical_std(step=20)), 'k--')

plt.title('comparison with different sampling frequency')
plt.xlabel('start phase')
plt.ylabel('standard deviation, nm')
plt.xlim(0, 720)
plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('Images/comparison with different sampling frequency', bbox_inches='tight')
plt.show(block=True)

# %%
x = np.append(np.array(3), np.arange(4, 100, 2))  # different steps
y = np.array([])  # std respectively
phase_interval = (0, np.pi * 2)
for N in x:
    _, m_std = n_step_single_line(step=N, phase=phase_interval)
    m_std_outlier = outlier_delete(m_std)
    m_std_average = np.nanmean(m_std_outlier)
    y = np.append(y, [m_std_average])
#%%
plt.figure()
plt.style.use('scientific')
plt.semilogx(x, y, color='red')
plt.show(block=1)
