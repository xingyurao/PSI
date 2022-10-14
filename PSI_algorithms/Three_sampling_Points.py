# @Time    : 2022/10/14 11:53
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Three_sampling_Points.py
# @Software: PyCharm
# %%
import numpy as np
from scipy.optimize import root
from Data_Process import value_suit


# %%
# create random number
def gauss_random(mu):
    return np.random.normal(0, mu)


# %%
def three_Sampling_Points(step=3, number_sampling=3, phase=(0, 2 * np.pi), point_number=720, loop=100000,
                          mu_phase=0.1 * np.pi / 180,
                          wx1: float = .0, a=120, b=140, lamda=530):
    N = step
    factor = lamda / (4 * np.pi)
    get_value = np.zeros([loop, point_number])
    phase_interval = (np.linspace(phase[0], phase[1], point_number)).T  # 1 x 720

    noise = np.zeros([number_sampling])
    for i in np.arange(0, number_sampling, 1):
        noise[i] = gauss_random(mu_phase)

    # create the irradiance(here number_sampling)，e.g: 3 x 720
    S = np.zeros([number_sampling, point_number])
    for n in np.arange(0, number_sampling, 1):
        wXn = 2 * np.pi * (n - 1) / N + wx1
        S[n] = a + b * np.cos(wXn + phase_interval + noise[n])

    def func(x, *args):  # here i comes from points number
        y = []
        for n in np.arange(1, number_sampling + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            y.append(x[0] + x[1] * np.cos(wXn + x[2]) - S[n - 1, args[0]])
        return y

    def jacob(x, *args):

        mat = np.zeros([3, 3])
        for n in np.arange(0, number_sampling, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            mat[n, 0] = 1
            mat[n, 1] = np.cos(wXn + x[2])
            mat[n, 2] = -x[1] * np.sin(wXn + x[2])
            # mat[n,:] = np.array([[1, np.cos(wXn + x[2]), -x[1] * np.sin(wXn + x[2])]])
        return np.mat(mat)

    get_phase = np.zeros([point_number])
    get_a = np.zeros([point_number])
    get_b = np.zeros([point_number])
    for j in np.arange(0, point_number, 1):
        x = root(func, args=(j), x0=np.array([0, 0, np.pi / 2]), jac=jacob).x
        get_a[j] = x[0]
        get_b[j] = x[1]
        get_phase[j] = x[2]
    return get_a, get_b, get_phase


a, b, theta = three_Sampling_Points(step=3)

a_new = value_suit(a)
b_new = value_suit(b)
print(a_new)
print(b_new)
