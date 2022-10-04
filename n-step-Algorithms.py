# @Time    : 2022/10/4 14:46
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : n-step-Algorithms.py
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
    N = step
    factor = lamda / (4 * np.pi)
    get_value = np.zeros([loop, point_number])
    phase_interval = np.linspace(phase[0], phase[1], point_number)
    for loo_p in np.arange(0, loop, 1):
        # get the velocity of programm
        if loo_p % (loop / 10) == 0:
            print(loo_p)

        upper = np.zeros([point_number])
        lower = np.zeros([point_number])

        for n in np.arange(1, N + 1, 1):
            wXn = 2 * np.pi * (n - 1) / N + wx1
            noise = gauss_random(mu_phase)
            upper += (a + b * np.cos(wXn + phase_interval + noise)) * np.sin(wXn)
            lower += (a + b * np.cos(wXn + phase_interval + noise)) * np.cos(wXn)

        get_value[loo_p] = np.arctan(-(upper / lower))

    std = np.std(get_value, axis=0)
    return get_value, std * factor


# %%

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
    return std

    # %%


def outlier_delete(y):
    y = np.array(y)
    q1 = np.percentile(y, 25)
    q3 = np.percentile(y, 75)
    iqr = q3 - q1
    n: int = 0
    # n_list = []
    while n < np.size(y):
        if y[n] < q1 - 3 * iqr or y[n] > q3 + 3 * iqr:
            y[n] = None
            # n_list.append(n)
            n += 1
        else:
            n += 1

    # y = np.delete(y, n_list)

    return y


# %% subtract the point with equally spaced intervals
def sub_point(y, n):
    y_new = []
    for i in np.arange(0, np.max(np.shape(y)), n):
        y_new.append(y[i])
    y_new = np.array(y_new)
    x_new = np.arange(0, np.max(np.shape(y)), n)
    return x_new, y_new
