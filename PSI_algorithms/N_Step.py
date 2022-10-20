# @Time    : 2022/10/4 14:46
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N_Step.py
# @Software: PyCharm

# %%
import numpy as np
from PSI_algorithms.Data_Process import unwraping
from datetime import datetime


# %%
# create random number
def gauss_random(mu):
    return np.random.normal(0, mu)


# %%
# get the std of positioning noise
def n_step_single_line(step=3, phase=(0, 2 * np.pi), point_number=720, loop=100000, mu_phase=5,
                       wx1: float = .0, a=0, b=1, lamda=530, shot_noise=False, position_noise=True):
    print('the current step:', step)
    print('Time:', datetime.now())
    if shot_noise is True:
        mu_intensity = 0.001
    else:
        mu_intensity = 0

    if position_noise is False:
        mu_phase = 0
    else:
        mu_phase = mu_phase * np.pi / 180

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
            upper += (a + b * np.cos(wXn + phase_interval + noise) + gauss_random(mu_intensity)) * np.sin(wXn)
            lower += (a + b * np.cos(wXn + phase_interval + noise) + gauss_random(mu_intensity)) * np.cos(wXn)

        get_value[loo_p] = np.arctan(-(upper / lower))

    print('start unwraping:', datetime.now())
    for i in np.arange(0, np.shape(get_value)[0], 1):
        get_value[i, :] = unwraping(get_value[i, :])

    std = np.std(get_value, axis=0)
    # return the monte-carlo results and their standard deviation
    return get_value * factor, std * factor


# %% get the theoretical standard deviation
def n_Step_theoretical_std(step=3, phase=(0, 2 * np.pi), point_number=720, lamda=530, mu_phase=5,
                           wx1=0, b=1, shot_noise=False, position_noise=True):
    mu_phase = mu_phase * np.pi / 180
    if position_noise is True:
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
    if shot_noise is True:
        mu_intensity = 0.001
        factor = lamda / (4 * np.pi)
        N = step
        A = np.ones([point_number]) * (1 / b * np.sqrt(2 / N))
        std = A * mu_intensity * factor
        # return theoretical standard deviation
        return std
