# @Time    : 2022/10/17 13:46
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : unwraping.py
# @Software: PyCharm


from PSI_algorithms.N_Step import *
import matplotlib.pyplot as plt


def unwraping(line=np.zeros([720]), lamda=530):
    factor = lamda / (4 * np.pi)
    for i in np.arange(0, np.size(line) - 1, 1):
        if np.isclose(np.abs(line[i + 1] - line[i]), np.pi * factor, 1.e-1):
            line[i + 1:] = line[i + 1:] + (line[i] - line[i + 1]) / np.abs(line[i + 1] - line[i]) * np.pi * factor


    return line


# %%
data1, _ = n_step_single_line(step=3, loop=1)
data_0 = data1[0]
plt.figure()
plt.plot(data_0, 'b-')
plt.show(block=1)

new = unwraping(data1[0])

plt.figure()
plt.plot(data_0, 'b-')
plt.plot(unwraping(data1[0]), 'k--')
plt.show(block=1)
