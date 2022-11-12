# @Time    : 2022/11/12 11:31
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : unwrap.py
# @Software: PyCharm
import numpy as np

# input array of sin and cos
def unwrap(sin=np.array([]), cos=np.array([])):

    if np.shape(sin)!=np.shape(cos):
        print('error')
        return 0
    else:
        tan = np.zeros([np.shape(sin)[0],np.shape(sin)[1]])

        for i in np.arange(0, np.shape(sin)[0], 1):
            for j in np.arange(0, np.shape(sin)[1], 1):
                if sin[i][j] > 0 and np.isclose(cos[i][j], 0):
                    tan[i][j] = np.pi / 2
                elif sin[i][j] < 0 and np.isclose(cos[i][j], 0):
                    tan[i][j] = -np.pi / 2
                else:
                    tan[i][j] = np.arctan(sin[i][j] / cos[i][j])
    for i in np.arange(0, np.shape(sin)[0], 1):
        for j in np.arange(0, np.shape(sin)[1]-1, 1):
            delta = tan[i][j + 1] - tan[i][j]
            tan[i][j + 1] = tan[i][j] + (delta - np.pi * round(delta / np.pi))
    return tan
