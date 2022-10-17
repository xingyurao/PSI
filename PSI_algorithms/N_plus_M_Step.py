# @Time    : 2022/10/12 22:10
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : N_plus_M_Step.py
# @Software: PyCharm
# %%
import numpy as np


# %%
# create random number
def gauss_random(mu):
    return np.random.normal(0, mu)


# %%  get the std of positioning noise

def N_M_step(step=3, over_sample_points=1, phase=(0, 2 * np.pi), point_number=720, loop=100000,
             mu_phase=0.1 * np.pi / 180,
             wx1: float = .0, a=0, b=1, lamda=530, shot_noise=False, position_noise=True):
    print('the current step:', step, '\n', 'the current over sampling points:', over_sample_points)
    if shot_noise is True:
        mu_intensity = 0.001
    else:
        mu_intensity = 0

    if position_noise is False:
        mu_phase = 0
    else:
        mu_phase = mu_phase

    N = step
    M = over_sample_points
    factor = lamda / (4 * np.pi)
    get_value = np.zeros([loop, point_number])
    phase_interval = np.linspace(phase[0], phase[1], point_number)

    for loo_p in np.arange(0, loop, 1):

        upper = np.zeros([point_number])
        lower = np.zeros([point_number])
        noise_position = np.zeros([N + M])
        noise_shot = np.zeros([N + M, point_number])
        for i in np.arange(0, N + M, 1):
            for j in np.arange(0, point_number, 1):
                noise_shot[i, j] = gauss_random(mu_intensity)

        for i in np.arange(0, N + M, 1):
            noise_position[i] = gauss_random(mu_phase)

        upper_1 = np.zeros([point_number])
        upper_2 = np.zeros([point_number])
        upper_3 = np.zeros([point_number])

        lower_1 = np.zeros([point_number])
        lower_2 = np.zeros([point_number])
        lower_3 = np.zeros([point_number])

        for n in np.arange(1, N + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            upper_1 += 2 * (a + b * np.cos(wXn + phase_interval + noise_position[n - 1]) + noise_shot[n - 1]) * np.sin(
                wXn)
            lower_1 += 2 * (a + b * np.cos(wXn + phase_interval + noise_position[n - 1]) + noise_shot[n - 1]) * np.cos(
                wXn)

        for n in np.arange(N + 1, M + N + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            upper_2 += (a + b * np.cos(wXn + phase_interval + noise_position[n - 1]) + noise_shot[n - 1]) * np.sin(wXn)
            lower_2 += (a + b * np.cos(wXn + phase_interval + noise_position[n - 1]) + noise_shot[n - 1]) * np.cos(wXn)

        for n in np.arange(1, M + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            upper_3 += (a + b * np.cos(wXn + phase_interval + noise_position[n - 1]) + noise_shot[n - 1]) * np.sin(wXn)
            lower_3 += (a + b * np.cos(wXn + phase_interval + noise_position[n - 1]) + noise_shot[n - 1]) * np.cos(wXn)

        upper = upper_1 + upper_2 - upper_3
        lower = lower_1 + lower_2 - lower_3

        get_value[loo_p] = np.arctan(-(upper / lower))

    std = np.std(get_value, axis=0)
    # return the monte-carlo results and their standard deviation
    return get_value, std * factor


# %% get the theoretical standard deviation
def N_M_theoretical_std(step=3, over_sample_points=1, phase=(0, 2 * np.pi), point_number=720,
                        mu_phase=0.1 * np.pi / 180, wx1: float = .0, a=0, b=1, lamda=530, shot_noise=False,
                        position_noise=True):
    N = step
    M=over_sample_points
    if position_noise is True:
        factor = lamda / (4 * np.pi)

        phase = np.linspace(phase[0], phase[1], point_number)
        A = np.zeros([point_number])
        for n in np.arange(1, M + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            A += (1/(4*N**2))*(4*np.cos(2*wXn+2*phase)-np.cos(4*wXn+4*phase))
        std = np.sqrt(A+(3/(4*N**2))*(2*N-M)) * mu_phase * factor
        # return theoretical standard deviation
        return std
    if shot_noise is True:
        mu_intensity = 0.001
        factor = lamda / (4 * np.pi)
        phase = np.linspace(phase[0], phase[1], point_number)
        A = np.zeros([point_number])
        for n in np.arange(1, M + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            A+=np.cos(2*wXn+2*phase)

        std = (1/(N*b))*np.sqrt(2*N-M+A)* mu_intensity * factor
        # return theoretical standard deviation
        return std
