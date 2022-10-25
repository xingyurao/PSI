# @Time    : 2022/10/4 16:05
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N-Step-Diagram.py
# @Software: PyCharm

# create bild of comparison with different steps
import matplotlib.pyplot as plt
import numpy as np

from PSI_algorithms.N_Step import *
from PSI_algorithms.Data_Process import *
from PSI_algorithms.Three_sampling_Points import *

# %% Comparison among different number of sampling Interferograms
phase_interval = (0, np.pi * 2)
_, m_std_3 = n_step(step=3, phase=phase_interval)
_, m_std_4 = n_step(step=4, phase=phase_interval)
_, m_std_8 = n_step(step=8, phase=phase_interval)
_, m_std_20 = n_step(step=20, phase=phase_interval)

# create the graph
plt.style.use('scientific')
fig = plt.figure()
plt.plot(m_std_3, label='3-sampling interferograms', color='green')
plt.plot((n_Step_theoretical_std(step=3)), 'k--')

plt.plot(m_std_4, label='4-sampling interferograms', color='blue')
plt.plot((n_Step_theoretical_std(step=4)), 'k--')

plt.plot(m_std_8, label='8-sampling interferogramss', color='red')
plt.plot((n_Step_theoretical_std(step=8)), 'k--')

plt.plot(m_std_20, label='20-sampling interferograms', color='yellow')
plt.plot((n_Step_theoretical_std(step=20)), 'k--')

plt.title('Comparison among different number of sampling interferograms')
plt.xlabel('Start phase')
plt.ylabel('Standard deviation, nm')
plt.xlim(0, 720)
plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig('Images/Positioning Noise/STD/Comparison among different number of sampling Interferograms',
            bbox_inches='tight')
plt.show(block=True)

# %% standard deviation vs number of sampling points
x = np.append(np.array([3, 5, 8]), np.arange(10, 100, 20))  # different steps
y = np.array([])  # std respectively
phase_interval = (0, np.pi * 2)
for N in x:
    _, m_std = n_step(step=N, phase=phase_interval)
    m_std_average = np.nanmean(m_std)
    y = np.append(y, [m_std_average])
mu_phase = 5 * np.pi / 180
factor = 530 / (4 * np.pi)
x_combined = np.append(np.array(3), np.arange(5, 100, 1))
plt.style.use('scientific')
plt.figure()
plt.scatter(x, y, color='blue', marker='o', label='monte-carlo method', edgecolors='blue',zorder=2)
plt.scatter(np.array([4]),np.array([np.sqrt(3/2/4)*factor*5*np.pi/180]),color='white',marker='o',edgecolors='k',zorder=2)
plt.loglog(x_combined, np.sqrt(3 / (2 * x_combined)) * mu_phase * factor, 'k-', label='combined uncertainty',zorder=1)
plt.xlabel('Number of sampling interferograms N')
plt.xticks([3, 10, 100], ['3', r'$10$', r'$10^2$'])
plt.ylabel('Standard deviation, nm')
plt.title('Standard deviation vs number of sampling interferograms')
plt.legend(loc='upper right')
plt.xlim(2, 200)
plt.tight_layout()
plt.savefig('Images/Positioning Noise/STD/standard deviation vs number of sampling interferograms', bbox_inches='tight')
plt.show(block=1)

# %%  form error for [3,4,8,20]-step algorithms
n = [12]
for i in n:
    Form, _ = n_step(step=i,loop=4)
    Form_free, _ = n_step(step=i, mu_phase=0, loop=1)
    plt.style.use('scientific')
    plt.figure()
    plt.plot(outlier_delete(Form[0] - Form_free[0]), label='measurement 1')
    plt.plot(outlier_delete(Form[1] - Form_free[0]), label='measurement 2')
    plt.plot(outlier_delete(Form[2] - Form_free[0]), label='measurement 3')
    plt.plot(outlier_delete(Form[3] - Form_free[0]), label='measurement 4')
    plt.plot(np.arange(0,720,1),np.zeros([720]),'k--')

    plt.title('Form error for {}-step algorithms'.format(i))
    plt.xlabel('Start phase')
    plt.ylabel('Form error, nm')
    plt.xlim(0, 720)
    plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    plt.legend(loc='upper right')
    plt.tight_layout()

    plt.savefig('Images/Positioning Noise/Form Error/form error for {}-step algorithms.png'.format(i),
                bbox_inches='tight')
    plt.close()
# %%  non-linear algorithms for 3 sampling points
n = [3, 4, 8]
for i in n:
    Form, std = three_Sampling_Points(step=i)
    Form_free, _ = three_Sampling_Points(step=i, mu_phase=0)

    plt.style.use('scientific')
    plt.figure()
    plt.plot((Form[0] - Form_free[0]), label='measurement 1')
    plt.plot((Form[1] - Form_free[0]), label='measurement 2')
    plt.plot((Form[2] - Form_free[0]), label='measurement 3')

    plt.title('form error for non-linear algorithms(sampling frequency={})'.format(i))
    plt.xlabel('start phase')
    plt.ylabel('measurement error, nm')
    plt.xlim(0, 720)
    plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    plt.legend(loc='upper right')
    plt.tight_layout()
    '''
    plt.savefig(
        'Images/Positioning Noise/Form Error/form error for non-linear algorithms(sampling frequency={}).png'.format(i),
        bbox_inches='tight')
    '''

    plt.show(block=1)
