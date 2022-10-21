# @Time    : 2022/10/19 10:36
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Problem_Proof.py
# @Software: PyCharm
import numpy as np

from PSI_algorithms.N_plus_M_Step import *
from PSI_algorithms.N_Step import n_Step_theoretical_std
import matplotlib.pyplot as plt

#%% halb number (M) proof
N=6
M = np.arange(0, N + 1, 1)
plt.style.use('scientific')
plt.figure()
for i in M:
    _, std = N_M_step(step=N, over_sample_points=i,wx1=np.pi/12)
    plt.plot(std, label='M={}'.format(i))

# get the theoretical value of N-sampling points
get_value_N = n_Step_theoretical_std(N)
get_value_2N = n_Step_theoretical_std(2 * N)
plt.plot(get_value_N, 'k--')
plt.plot(get_value_2N, 'k--')
plt.xlabel('Start phase')
plt.ylabel('Standard deviation, nm')
plt.xlim(0, 720)
plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.legend(loc='upper right')
plt.title('Comparison among {}+M sampling interferograms'.format(N))
plt.tight_layout()
plt.savefig('Images/Positioning Noise/STD/comparison with {}+M sampling interferograms(6+3)'.format(N),
            bbox_inches='tight')
plt.close()