# @Time    : 2022/10/22 9:51
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : run_add.py
# @Software: PyCharm
import matplotlib.pyplot as plt
from PSI_algorithms.N_plus_M_Step import *
from PSI_algorithms.Data_Process import *
from PSI_algorithms.N_Step import *

# %% comparison between 2N sampling points and N+N sampling points

N = np.append(np.array([3]), np.arange(5, 11, 1))
std_NN = np.array([])
std_2N = np.array([])
for i in N:
    _, std_nn = N_M_step(step=i, over_sample_points=i,loop=10)
    std_NN = np.append(std_NN, np.nanmean(outlier_delete(std_nn)))
    _, std_2n = n_step(step=i * 2)
    std_2N = np.append(std_2N, np.nanmean(outlier_delete(std_2n)))

plt.style.use('scientific')
plt.figure()
factor = 530 / (4 * np.pi)
plt.loglog(N * 2, std_2N, 'k-', label='2N sampling interferograms', zuorder=1)
plt.scatter(N * 2, std_NN, color='blue', label='N+N sampling interferograms', edgecolors='blue', zorder=2)
plt.scatter(np.array([8]), np.array([np.sqrt(3 / 2 / 8) * factor * 5 * np.pi / 180]), color='white', marker='o',
            edgecolors='k', zorder=2)

plt.xlabel('Number of sampling interferograms (2N)')
plt.ylabel('Standard deviation, nm')

plt.xticks([6, 10, 12, 14, 16, 18, 20], [r'$6$', r'$10$', r'$12$', r'$14$', r'$16$', r'$18$', r'$20$'])
plt.xlim(5, 30)
plt.legend(loc='upper right')
plt.title('Comparison between 2N and N+N sampling interferograms')
plt.tight_layout()
#plt.savefig('Images/Positioning Noise/STD/comparison between 2N sampling points and N+N sampling points',
#            bbox_inches='tight')
plt.show(block=1)
