# @Time    : 2022/10/17 0:22
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Shot_Noise_NM-Diagram.py
# @Software: PyCharm

import matplotlib.pyplot as plt
from PSI_algorithms.N_plus_M_Step import *
from PSI_algorithms.N_Step import *
from PSI_algorithms.Data_Process import *

# %% comparison with N+M sampling points
for N in np.array([3]):
    M = np.arange(0, N + 1, 1)
    plt.style.use('scientific')
    fig1 = plt.figure()
    for i in M:
        _, std = N_M_step(step=N, over_sample_points=i, position_noise=False, shot_noise=True,loop=100)
        std=outlier_delete(std)
        plt.plot(std, label='M={}'.format(i))

    # get the theoretical value of N-sampling points
    get_value_N = n_Step_theoretical_std(N, position_noise=False, shot_noise=True)
    get_value_2N = n_Step_theoretical_std(2 * N, position_noise=False, shot_noise=True)
    plt.plot(get_value_N, 'k--')
    plt.plot(get_value_2N, 'k--')

    plt.xlabel('Start phase')
    plt.ylabel('Standard deviation, nm')
    plt.xlim(0, 720)
    plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
    plt.legend(loc='upper right')
    plt.title('Comparison among {}+M sampling interferograms'.format(N))
    plt.tight_layout()
    plt.savefig('Images/Shot Noise/comparison with {}+M sampling points'.format(N), bbox_inches='tight')
    plt.show(block=1)
    plt.close(fig1)
#%%