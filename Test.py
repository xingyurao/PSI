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


