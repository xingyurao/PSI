# @Time    : 2022/10/17 13:46
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : unwraping.py
# @Software: PyCharm
import numpy as np
from PSI_algorithms.N_Step import *
import matplotlib.pyplot as plt

def unwraping(data=np.zeros([720]), lamda=530):
    factor = lamda / (4 * np.pi)

    for i in np.arange(0, np.size(data) - 1, 1):
        if np.isclose(np.abs(data[i + 1] - data[i]), np.pi * factor, 1.e-1):
            data[i + 1:]= data[i + 1:] + (data[i] - data[i + 1]) / np.abs(data[i + 1] - data[i]) * np.pi * factor

    return [data]


data, _ = n_step_single_line(step=3, loop=1)
data = data[0]
plt.figure()
plt.plot(data)
plt.show(block=1)

data_new=unwraping(data)[0]
plt.figure()
plt.plot(data)
plt.plot(data_new,'k--')
plt.show(block=1)
