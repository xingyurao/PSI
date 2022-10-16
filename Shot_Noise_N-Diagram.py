# @Time    : 2022/10/16 18:55
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Shot_Noise_N-Diagram.py
# @Software: PyCharm

# create bild of comparison with different steps
import matplotlib.pyplot as plt
from PSI_algorithms.N_Step import *
from PSI_algorithms.Data_Process import *
from PSI_algorithms.Three_sampling_Points import *

# %% comparison with different sampling frequency
phase_interval = (0, np.pi * 2)
_, m_std_3 = n_step_single_line(step=3, phase=phase_interval, position_noise=False, shot_noise=True)
_, m_std_4 = n_step_single_line(step=4, phase=phase_interval, position_noise=False, shot_noise=True)
_, m_std_8 = n_step_single_line(step=8, phase=phase_interval, position_noise=False, shot_noise=True)
_, m_std_20 = n_step_single_line(step=20, phase=phase_interval, position_noise=False, shot_noise=True)

m_std_3 = outlier_delete(m_std_3)
m_std_4 = outlier_delete(m_std_4)
m_std_8 = outlier_delete(m_std_8)
m_std_20 = outlier_delete(m_std_20)
# create the graph
fig = plt.figure()
plt.style.use('scientific')
plt.plot(m_std_3, label='3-sampling points', color='green')

plt.plot(m_std_4, label='4-sampling points', color='blue')

plt.plot(m_std_8, label='8-sampling points', color='red')

plt.plot(m_std_20, label='20-sampling points', color='yellow')

plt.title('comparison with different sampling frequency')
plt.xlabel('start phase')
plt.ylabel('standard deviation, nm')
plt.xlim(0, 720)
plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('Images/Shot Noise/comparison with different sampling frequency.png', bbox_inches='tight')
plt.show(block=True)
