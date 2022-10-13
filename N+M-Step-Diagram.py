# @Time    : 2022/10/13 10:36
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N+M-Step-Diagram.py
# @Software: PyCharm
import matplotlib.pyplot as plt
from PSI_algorithms.N_plus_M_Step import *
from PSI_algorithms.N_Step import *
from PSI_algorithms.Data_Process import *

# %% comparison with N+M sampling points
N = 8
M = np.arange(0, N + 1, 1)
plt.style.use('scientific')
plt.figure()
for i in M:
    _, std = N_M_step(step=N, over_sample_points=i)
    std_new = outlier_delete(std)
    plt.plot(std_new, label='M={}'.format(i))

plt.xlabel('start phase')
plt.ylabel('standard deviation, nm')
plt.xlim(0, 720)
plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.legend(loc='upper right')
plt.title('comparison with {}+M sampling points'.format(N))
plt.tight_layout()
# plt.savefig('Images/comparison with {}+M sampling points'.format(N), bbox_inches='tight')
plt.show(block=1)

# %% comparison between 2N sampling points and N+N sampling points

N = np.append(np.array([3]), np.arange(5, 11, 1))
std_NN = np.array([])
std_2N = np.array([])
for i in N:
    _, std_nn = N_M_step(step=i, over_sample_points=i)
    std_NN = np.append(std_NN, np.nanmean(outlier_delete(std_nn)))
    _, std_2n = n_step_single_line(step=i * 2)
    std_2N = np.append(std_2N, np.nanmean(outlier_delete(std_2n)))

plt.style.use('scientific')
plt.figure()

plt.loglog(N * 2, std_2N, 'k-', label='2N sampling points')
plt.scatter(N * 2, std_NN, color='blue', label='N+N sampling points', edgecolors='blue')
plt.xlabel('number of sampling points (2N)')
plt.ylabel('standard deviation, nm')

plt.xticks([6, 10, 12, 14, 16, 18, 20], [r'$6$', r'$10$', r'$12$', r'$14$', r'$16$', r'$18$', r'$20$'])
plt.xlim(5, 30)
plt.legend(loc='upper right')
plt.title('comparison between 2N and N+N sampling points')
plt.tight_layout()
plt.savefig('Images/comparison between 2N sampling points and N+N sampling points', bbox_inches='tight')
plt.show(block=1)
