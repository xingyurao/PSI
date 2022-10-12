# @Time    : 2022/10/12 22:10
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N+M_step.py
# @Software: PyCharm
# %%
import numpy as np


# %%
# create random number
def gauss_random(mu):
    return np.random.normal(0, mu)


# %%
# get the std of positioning noise
def N_M_step(step=3, over_sample_points=1, phase=(0, 2 * np.pi), point_number=720, loop=100000,
             mu_phase=0.1 * np.pi / 180,
             wx1: float = .0, a=0, b=1, lamda=530):
    N = step
    M = over_sample_points
    factor = lamda / (4 * np.pi)
    get_value = np.zeros([loop, point_number])
    phase_interval = np.linspace(phase[0], phase[1], point_number)

    for loo_p in np.arange(0, loop, 1):

        upper = np.zeros([point_number])
        lower = np.zeros([point_number])
        noise = np.zeros([N + M])
        for i in np.arange(0, N + M, 1):
            noise[i] = gauss_random(mu_phase)

        upper_1 = np.zeros([N])
        upper_2 = np.zeros([M])
        upper_3 = np.zeros([M])

        lower_1 = np.zeros([N])
        lower_2 = np.zeros([M])
        lower_3 = np.zeros([M])

        for n in np.arange(1, N + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            upper_1 += 2 * (a + b * np.cos(wXn + phase_interval + noise[n - 1])) * np.sin(wXn)
            lower_1 += 2 * (a + b * np.cos(wXn + phase_interval + noise[n - 1])) * np.cos(wXn)

        for n in np.arange(N + 1, M + N + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            upper_2 += (a + b * np.cos(wXn + phase_interval + noise[n - 1])) * np.sin(wXn)
            lower_2 += (a + b * np.cos(wXn + phase_interval + noise[n - 1])) * np.cos(wXn)

        for n in np.arange(1, M + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            upper_3 += (a + b * np.cos(wXn + phase_interval + noise[n - 1])) * np.sin(wXn)
            lower_3 += (a + b * np.cos(wXn + phase_interval + noise[n - 1])) * np.cos(wXn)

        upper = upper_1 + upper_2 - upper_3
        lower = lower_1 + lower_2 - lower_3

        get_value[loo_p] = np.arctan(-(upper / lower))

    std = np.std(get_value, axis=0)
    # return the monte-carlo results and their standard deviation
    return get_value, std * factor
