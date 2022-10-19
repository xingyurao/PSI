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
N = 6
M = np.arange(0, N + 1, 1)
plt.style.use('scientific')
plt.figure()
for i in M:
    _, std = N_M_step(step=N, over_sample_points=i, loop=1000,mu_phase=.1)
    std_new = outlier_delete(std)
    plt.plot(std_new, label='M={}'.format(i))

# get the theoretical value of N-sampling points
get_value_N = n_Step_theoretical_std(N,mu_phase=.1)
get_value_2N = n_Step_theoretical_std(2 * N,mu_phase=.1)
plt.plot(get_value_N, 'k--')
plt.plot(get_value_2N, 'k--')

plt.xlabel('start phase')
plt.ylabel('standard deviation, nm')
plt.xlim(0, 720)
plt.xticks([0, 720 / 4, 720 / 2, 720 / 4 * 3, 720], [r'0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.legend(loc='upper right')
plt.title('comparison with {}+M sampling interferograms'.format(N))
plt.tight_layout()
plt.savefig('Images/Positioning Noise/STD/comparison with {}+M sampling interferograms'.format(N), bbox_inches='tight')
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

plt.loglog(N * 2, std_2N, 'k-', label='2N sampling interferograms')
plt.scatter(N * 2, std_NN, color='blue', label='N+N sampling interferograms', edgecolors='blue')
plt.xlabel('number of sampling interferograms (2N)')
plt.ylabel('standard deviation, nm')

plt.xticks([6, 10, 12, 14, 16, 18, 20], [r'$6$', r'$10$', r'$12$', r'$14$', r'$16$', r'$18$', r'$20$'])
plt.xlim(5, 30)
plt.legend(loc='upper right')
plt.title('comparison between 2N and N+N sampling interferograms')
plt.tight_layout()
plt.savefig('Images/Positioning Noise/STD/comparison between 2N sampling points and N+N sampling points', bbox_inches='tight')
plt.show(block=1)


# %% comparison between different sampling frequencies # create 6+6 7+5 8+4...12+0 step
All_step = 16
x = np.arange(0, All_step / 2 + 1, 1)
y = np.array([])
yerr = np.array([])
for i in np.arange(All_step / 2, All_step + 1, 1):
    i = int(i)
    std = N_M_theoretical_std(step=i, over_sample_points=All_step - i)
    y = np.append(y, np.average(std))
    yerr = np.append(yerr, np.max(std)-np.average(std))

yerr[0]=np.nan
yerr[-1]=np.nan
plt.style.use('scientific')
plt.figure()
plt.errorbar(x, y, yerr, ecolor='k', elinewidth=1, marker='s', mfc='k', mec='k', mew=1, ms=5, alpha=1,
             capsize=5, capthick=3, linestyle="none", label="Observation")

p=np.polyfit(x,y,deg=4)
plt.plot(np.linspace(0,All_step/2,100),np.polyval(p,np.linspace(0,All_step/2,100)),'grey')

plt.xlabel('sampling methods')
plt.xticks([0,1,2,3,4,5,6,7,8],['8+8','9+7','10+6','11+5','12+4','13+3','14+2','15+1','16+0'],rotation=45)
plt.ylabel('standard deviation, nm')
plt.title('comparison between different sampling frequencies')
plt.tight_layout()
plt.savefig('Images/Positioning Noise/STD/comparison between different sampling frequencies', bbox_inches='tight')
plt.show(block=1)
