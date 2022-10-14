# @Time    : 2022/10/14 11:53
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N_sampling_Points.py
# @Software: PyCharm
# %%
import numpy as np
from scipy.optimize import root


# %%
# create random number
def gauss_random(mu):
    return np.random.normal(0, mu)


# %%
def N_Sampling_Points(step=3, number_sampling=3, phase=(0, 2 * np.pi), point_number=720, loop=100000,
                      mu_phase=0.1 * np.pi / 180,
                      wx1: float = .0, a=0, b=1, lamda=530):
    print('the current step:', step)
    N = step
    factor = lamda / (4 * np.pi)
    get_value = np.zeros([loop, point_number])
    phase_interval = np.linspace(phase[0], phase[1], point_number)

    noise = np.zeros([number_sampling])
    for i in np.arange(0, number_sampling, 1):
        noise[i] = gauss_random(mu_phase)

    # create the irradiance(here number_sampling)
    S = np.zeros([number_sampling, point_number])
    for n in np.arange(0, number_sampling, 1):
        wXn = 2 * np.pi * (n - 1) / N + wx1
        S[n] = a + b * np.cos(wXn + phase_interval + noise[n])
