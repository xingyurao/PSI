# @Time    : 2022/10/19 10:36
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Problem_Proof.py
# @Software: PyCharm
import numpy as np

wx1 = np.pi / 10
for N in np.arange(3, 1000, 1):
    data = np.array([])
    for n in np.arange(1, N + 1, 1):
        data = np.append(data, 32 * (2 * np.pi*(n - 1) / N + wx1))
    value = np.sum(np.cos(data))
    if not np.isclose(value,.0,1.e-10):
        print('error step:', N)
        print(value)
