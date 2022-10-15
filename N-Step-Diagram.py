# @Time    : 2022/10/4 16:05
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N-Step-Diagram.py
# @Software: PyCharm

# create bild of comparison with different steps
import matplotlib.pyplot as plt
from PSI_algorithms.N_Step import *
from PSI_algorithms.Data_Process import *
from PSI_algorithms.Three_sampling_Points import *


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
# plt.savefig('Images/comparison with different sampling frequency', bbox_inches='tight')
plt.show(block=True)

# %% standard deviation vs number of sampling points
x = np.append(np.array(3), np.arange(5, 100, 10))  # different steps
y = np.array([])  # std respectively
phase_interval = (0, np.pi * 2)
for N in x:
    _, m_std = n_step_single_line(step=N, phase=phase_interval)
    m_std_outlier = outlier_delete(m_std)
    m_std_average = np.nanmean(m_std_outlier)
    y = np.append(y, [m_std_average])
mu_phase = 0.1 * np.pi / 180
factor = 530 / (4 * np.pi)
x_combined = np.append(np.array(3), np.arange(5, 100, 1))
plt.style.use('scientific')
plt.figure()
plt.scatter(x, y, color='blue', marker='o', label='monte-carlo method', edgecolors='blue')
plt.loglog(x_combined, np.sqrt(3 / (2 * x_combined)) * mu_phase * factor, 'k-', label='combined uncertainty')
plt.xlabel('number of sampling points N')
plt.xticks([3, 10, 100], ['3', r'$10$', r'$10^2$'])
plt.ylabel('standard deviation, nm')
plt.title('standard deviation vs number of sampling points')
plt.legend(loc='upper right')
plt.xlim(2, 200)
plt.tight_layout()
# plt.savefig('Images/standard deviation vs number of sampling points', bbox_inches='tight')
plt.show(block=1)

# %%  form error for [3,4,8,20]-step algorithms
n = [3, 4, 8, 20]
for i in n:
    Form, _ = n_step_single_line(step=i)

    plt.style.use('scientific')
    plt.figure()
    plt.plot(outlier_delete(Form[0] - np.average(Form, 0)), label='measurement 1')
    plt.plot(outlier_delete(Form[1] - np.average(Form, 0)), label='measurement 2')
    plt.plot(outlier_delete(Form[2] - np.average(Form, 0)), label='measurement 3')

    plt.title('form error for {}-step algorithms'.format(i))
    plt.xlabel('start phase')
    plt.ylabel('measurement error, nm')
    plt.xlim(0, 720)
    plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig('Images/Positioning Noise/Form Error/form error for {}-step algorithms.png'.format(i),
                bbox_inches='tight')
    plt.show(block=1)
# %%  non-linear algorithms for 3 sampling points
n = [3, 4, 8]
for i in n:
    Form, std = three_Sampling_Points(step=i)
    std_new = outlier_delete(std)
    plt.style.use('scientific')
    plt.figure()
    plt.plot(outlier_delete(Form[0] - np.average(Form, 0)), label='measurement 1')
    plt.plot(outlier_delete(Form[1] - np.average(Form, 0)), label='measurement 2')
    plt.plot(outlier_delete(Form[2] - np.average(Form, 0)), label='measurement 3')

    plt.title('form error for non-linear algorithms(sampling frequency={})'.format(i))
    plt.xlabel('start phase')
    plt.ylabel('measurement error, nm')
    plt.xlim(0, 720)
    plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    plt.legend(loc='upper right')
    plt.tight_layout()
    plt.savefig(
        'Images/Positioning Noise/Form Error/form error for non-linear algorithms(sampling frequency={}).png'.format(i),
        bbox_inches='tight')
    plt.show(block=1)

