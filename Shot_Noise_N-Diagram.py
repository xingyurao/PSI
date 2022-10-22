# @Time    : 2022/10/16 18:55
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Shot_Noise_N-Diagram.py
# @Software: PyCharm

# create bild of comparison with different steps
import matplotlib.pyplot as plt
from PSI_algorithms.N_Step import *
from PSI_algorithms.Data_Process import *

# %% comparison with different sampling frequency
phase_interval = (0, np.pi * 2)
_, m_std_3 = n_step(step=3, phase=phase_interval, position_noise=False, shot_noise=True)
_, m_std_4 = n_step(step=4, phase=phase_interval, position_noise=False, shot_noise=True)
_, m_std_8 = n_step(step=8, phase=phase_interval, position_noise=False, shot_noise=True)
_, m_std_20 = n_step(step=20, phase=phase_interval, position_noise=False, shot_noise=True)

m_std_3 = outlier_delete(m_std_3)
m_std_4 = outlier_delete(m_std_4)
m_std_8 = outlier_delete(m_std_8)
m_std_20 = outlier_delete(m_std_20)

# create the graph
plt.style.use('scientific')
fig = plt.figure()
plt.plot(m_std_3*.1, label='3-sampling interferograms', color='green')
plt.plot(n_Step_theoretical_std(step=3, position_noise=False, shot_noise=True)*.1, 'k--')

plt.plot(m_std_4*.1, label='4-sampling interferograms', color='blue')
plt.plot(n_Step_theoretical_std(step=4, position_noise=False, shot_noise=True)*.1, 'k--')

plt.plot(m_std_8*.1, label='8-sampling interferograms', color='red')
plt.plot(n_Step_theoretical_std(step=8, position_noise=False, shot_noise=True)*.1, 'k--')

plt.plot(m_std_20*.1, label='20-sampling interferograms', color='yellow')
plt.plot(n_Step_theoretical_std(step=20, position_noise=False, shot_noise=True)*.1, 'k--')

plt.title('Comparison among different sampling frequencies')
plt.xlabel('Start phase')
plt.ylabel('Standard deviation, nm')
plt.xlim(0, 720)
plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('Images/Shot Noise/comparison with different sampling frequency.png', bbox_inches='tight')
plt.show(block=1)

# %% standard deviation vs number of sampling points
x = np.append(np.array([[3, 4, 8]]), np.arange(10, 100, 20))  # different steps
y = np.array([])  # std respectively
phase_interval = (0, np.pi * 2)
for N in x:
    _, m_std = n_step(step=N, phase=phase_interval, position_noise=False, shot_noise=True)
    m_std = outlier_delete(m_std)
    m_std_average = np.nanmean(m_std)
    y = np.append(y, [m_std_average])
mu_Intensity = 0.01
factor = 530 / (4 * np.pi)
x_combined = np.append(np.array(3), np.arange(5, 100, 1))
plt.style.use('scientific')
plt.figure()
plt.scatter(x, y, color='blue', marker='o', label='monte-carlo method', edgecolors='blue', zorder=2)
plt.loglog(x_combined, np.sqrt(2 / (x_combined)) * mu_Intensity * factor, 'k-', label='combined uncertainty', zorder=1)
plt.xlabel('Number of sampling Interferograms (N)')
plt.xticks([3, 10, 100], ['3', r'$10$', r'$10^2$'])
plt.ylabel('Standard deviation, nm')
plt.title('Standard deviation vs number of sampling interferograms')
plt.legend(loc='upper right')
plt.xlim(2, 200)
plt.tight_layout()
plt.savefig('Images/Shot Noise/standard deviation vs number of sampling points', bbox_inches='tight')
plt.show(block=1)
