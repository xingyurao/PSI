# @Time    : 2022/10/4 14:46
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N_Step.py
# @Software: PyCharm

# %%
import numpy as np


# %%
# create random number
def gauss_random(mu):
    return np.random.normal(0, mu)


# %%
# get the std of positioning noise
def n_step_single_line(step=3, phase=(0, 2 * np.pi), point_number=720, loop=100000, mu_phase=0.1 * np.pi / 180,
                       wx1: float = .0, a=0, b=1, lamda=530):
    print('the current step:', step)
    N = step
    factor = lamda / (4 * np.pi)
    get_value = np.zeros([loop, point_number])
    phase_interval = np.linspace(phase[0], phase[1], point_number)
    for loo_p in np.arange(0, loop, 1):

        upper = np.zeros([point_number])
        lower = np.zeros([point_number])

        for n in np.arange(1, N + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            noise = gauss_random(mu_phase)
            upper += (a + b * np.cos(wXn + phase_interval + noise)) * np.sin(wXn)
            lower += (a + b * np.cos(wXn + phase_interval + noise)) * np.cos(wXn)

        get_value[loo_p] = np.arctan(-(upper / lower))

    std = np.std(get_value, axis=0)
    # return the monte-carlo results and their standard deviation
    return get_value, std * factor


# %% get the theoretical standard deviation
def n_Step_theoretical_std(step=3, phase=(0, 2 * np.pi), point_number=720, lamda=530, mu_phase=0.1 * np.pi / 180,
                           wx1=0):
    factor = lamda / (4 * np.pi)
    N = step
    phase = np.linspace(phase[0], phase[1], point_number)
    A = np.zeros([point_number])
    for n in np.arange(1, N + 1, 1):
        wXn = 2 * np.pi * (n - 1) / N + wx1
        A += ((np.sin(wXn + phase)) ** 2 * (2 / N)) ** 2
    std = np.sqrt(A) * mu_phase * factor
    # return theoretical standard deviation
    return std

