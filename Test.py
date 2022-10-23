# @Time    : 2022/10/22 14:12
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Test.py
# @Software: PyCharm
import numpy as np
'''
#%% test sinPSI (8)
x = np.linspace(0, np.pi, 80)
y = np.array([])
for theta in np.linspace(0, np.pi, 80):
    I = np.zeros([8])
    for n in np.arange(0, 8, 1):
        I[n] = 1 + 5 * np.cos(theta + 2.93 * np.cos(np.pi / 8 * 1 + n * np.pi / 4))

    y = np.append(y, np.arctan(
        (-1.6647 * (I[1] - I[2] - I[5] + I[6])) / (-(I[0] + I[3] + I[4] + I[7]) + (I[1] + I[2] + I[5] + I[6]))))
'''

'''
#%% test halb number equal 0
for theta in np.linspace(0,np.pi*2,1000):

    for N in np.arange(4,100,2):
        all = 0
        for n in np.arange(0,N/2,1):
            all+=np.cos((theta+2*np.pi*(n-1)/N)*4)
        if not np.isclose(all,0,atol=1.e-5):
            print('error:',N)
            
'''


# %% comparison between (N+1/2N) sampling und N+1/2N sampling interferograms
import matplotlib.pyplot as plt
from PSI_algorithms.N_plus_M_Step import *
from PSI_algorithms.N_Step import *
from PSI_algorithms.Data_Process import *

std_NN = np.array([])
std_NM = np.array([])
x=np.arange(4,20,2)
x=(x+x/2).astype(int)
for N in np.arange(4, 20, 2):
    _, std = n_step(step=N + N / 2,position_noise=False,shot_noise=True)
    std_NN = np.append(std_NN, np.nanmean(std))
    _, std = N_M_step(step=N, over_sample_points=int(N / 2),position_noise=False,shot_noise=True)
    std_NM = np.append(std_NM, np.nanmean(std))

plt.style.use('scientific')
plt.figure()
factor = 530 / (4 * np.pi)
plt.loglog(x, std_NN, 'k', label='N sampling interferograms',marker='o',markeredgecolor='k')
plt.loglog(x, std_NM, 'r', label='N+M sampling interferograms',marker='o',markeredgecolor='r')

plt.xlabel('Number of sampling interferograms')
plt.ylabel('Standard deviation, nm')

plt.xticks([5,6, 15, 20, 30], ['',r'$6$', r'$15$','', r'$30$'])
plt.yticks([0.04,0.05,0.06,0.1,0.2,0.3],['',r'$0.05$','',r'$0.1$',r'$0.2$',''])
plt.xlim(5, 30)
plt.ylim(0.08,0.3)
plt.legend(loc='upper right')
plt.title('Comparison between N und N+M sampling interferograms')
plt.tight_layout()
plt.savefig('Images/Shot Noise/comparison sampling sampling interferograms',
            bbox_inches='tight')
plt.show(block=1)

