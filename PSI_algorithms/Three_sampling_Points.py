# @Time    : 2022/10/14 11:53
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Three_sampling_Points.py
# @Software: PyCharm
# %%
import numpy as np
from scipy.optimize import root
from Data_Process import value_suit, outlier_delete, phase_choose


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

        get_a = np.zeros([point_number])
        get_b = np.zeros([point_number])
        for j in np.arange(0, point_number, 1):
            x = root(func, args=(j), x0=np.array([0, 0, np.pi / 2]), jac=jacob).x
            get_a[j] = x[0]
            get_b[j] = x[1]

        a_value = value_suit(get_a)
        b_value = value_suit(get_b)

        get_phase = np.zeros([point_number])  # 720 x 3
        phase_try = np.zeros([2, number_sampling, point_number])  # 2 x 3 x 720
        for n in np.arange(0, number_sampling, 1):  # 0 1 2
            wXn = 2 * np.pi * (n - 1) / N + wx1

            inner = (S[n] - a_value) / b_value
            for i in np.arange(0, np.size(inner), 1):

                if inner[i] >= 1:
                    inner[i] = 1
                elif inner[i] <= -1:
                    inner[i] = -1

            # test
            phase_try[:, n, :] = (np.array([[(np.arccos(inner) - wXn), (-np.arccos(inner) - wXn)]]))

        for i in np.arange(0, point_number, 1):
            p = np.sort((phase_try[:, :, i]).reshape((1, phase_try.shape[0] * phase_try.shape[1])))


            get_phase[i] = phase_choose(p,number_sampling)

        get_value[loo] = get_phase

    std = np.std(get_value, axis=0)
    # return the monte-carlo results and their standard deviation
    return get_value * factor, std * factor


data, std = three_Sampling_Points(step=3, phase=(0,2*np.pi),point_number=720)

std_new = outlier_delete(std)
# %%
import matplotlib.pyplot as plt

plt.figure()
plt.subplot(211)
plt.plot(data[1])
#plt.plot(np.arange(0, 720, 1), np.linspace(0, np.pi * 2, 720) * 530 / (4 * np.pi))
plt.subplot(212)
plt.plot(std_new)
plt.show(block=1)
