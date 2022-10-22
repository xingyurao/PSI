# @Time    : 2022/10/22 14:12
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Test.py
# @Software: PyCharm
import numpy as np
from datetime import datetime
from PSI_algorithms.Data_Process import unwraping
import matplotlib.pyplot as plt

def NM(step=3, over_sample_points=1, phase=(0, 2 * np.pi), point_number=720, loop=100000,
       mu_phase=5, mu_intensity=0.01,
       wx1: float = .0, a=0, b=1, lamda=530, shot_noise=False, position_noise=True):
    mu_phase = mu_phase * np.pi / 180
    print('the current step:', step, 'the current over sampling points:', over_sample_points)
    print(datetime.now())

    if shot_noise is True:
        mu_intensity = mu_intensity
        mu_phase = 0
    else:
        mu_intensity = 0
        mu_phase =mu_phase

    N = step
    M = over_sample_points

    factor = lamda / (4 * np.pi)
    get_value = np.zeros([loop, point_number])
    phase_interval = np.linspace(phase[0], phase[1], point_number)

    Time = datetime.now()
    for loo_p in np.arange(0, loop, 1):



        noise_position=np.random.normal(0,mu_phase,size=M+N)

        noise_shot =np.random.normal(0,mu_intensity,size=(N + M, point_number))



        lines = np.zeros([2, N + M, point_number])  # 0-sin, 1-cos

        for n in np.arange(1, N + M + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            lines[0, n - 1, :] = (a + b * np.cos(wXn + phase_interval + noise_position[n - 1]) + noise_shot[
                n - 1]) * np.sin(wXn)
            lines[1, n - 1, :] = (a + b * np.cos(wXn + phase_interval + noise_position[n - 1]) + noise_shot[
                n - 1]) * np.cos(wXn)

        upper = 2 * np.sum(lines[0, 0:N, :], 0) + np.sum(lines[0, N:M + N, :], 0) - np.sum(lines[0, 0:M, :], 0)
        lower = 2 * np.sum(lines[1, 0:N, :], 0) + np.sum(lines[1, N:M + N, :], 0) - np.sum(lines[1, 0:M, :], 0)
        get_value[loo_p] = np.arctan(-(upper / lower))

    print(datetime.now() - Time)
    print('start unwraping:', datetime.now())
    for i in np.arange(0, np.shape(get_value)[0], 1):
        get_value[i, :] = unwraping(get_value[i, :])

    std = np.std(get_value, axis=0)
    # return the monte-carlo results and their standard deviation
    return get_value * factor, std * factor

_, std=NM(step=4,over_sample_points=4,loop=10000)
plt.figure()
plt.plot(std)
plt.show(block=1)