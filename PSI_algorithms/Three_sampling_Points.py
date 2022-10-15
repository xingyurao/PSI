# @Time    : 2022/10/14 11:53
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Three_sampling_Points.py
# @Software: PyCharm
# %%
import numpy as np
from scipy.optimize import root
from Data_Process import value_suit, outlier_delete


# %%
# create random number
def gauss_random(mu):
    return np.random.normal(0, mu)


# %%
def three_Sampling_Points(step=3, number_sampling=3, phase=(0, 2 * np.pi), point_number=720, loop=10,
                          mu_phase=0.1 * np.pi / 180,
                          wx1: float = .0, a=120, b=140, lamda=530):
    N = step
    factor = lamda / (4 * np.pi)
    get_value = np.zeros([loop, point_number])
    for loo in np.arange(0, loop, 1):
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

        a_value = value_suit(get_a)
        b_value = value_suit(get_b)
        get_phase = np.zeros([number_sampling, point_number])
        for n in np.arange(0, number_sampling, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1

            inner = (S[n] - a_value) / b_value
            for i in np.arange(0, np.size(inner), 1):

                if inner[i] >= 1:
                    inner[i] = 1
                elif inner[i] <= -1:
                    inner[i] = -1

            get_phase[n] = np.arccos(inner) - wXn
        get_value[loo] = np.average(get_phase, 0)

    std = np.std(get_value, axis=0)
    # return the monte-carlo results and their standard deviation
    return get_value, std * factor


_, std = three_Sampling_Points(step=3)

std_new = outlier_delete(std)
# %%
import matplotlib.pyplot as plt

plt.figure()
plt.plot(std_new)
plt.show(block=1)