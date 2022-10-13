# @Time    : 2022/10/13 10:36
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N+M-Step-Diagram.py
# @Software: PyCharm
import matplotlib.pyplot as plt
from PSI_algorithms.N_plus_M_Step import *
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
plt.savefig('Images/comparison with {}+M sampling points'.format(N), bbox_inches='tight')
plt.show(block=1)

# %%
