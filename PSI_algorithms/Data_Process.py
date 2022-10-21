# @Time    : 2022/10/13 11:59
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Data_Process.py
# @Software: PyCharm

import numpy as np
import warnings

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

            n += 1
        else:
            n += 1

    return y


# %% subtract the point with equally spaced intervals
def sub_point(y, n):
    y_new = []
    for i in np.arange(0, np.max(np.shape(y)), n):
        y_new.append(y[i])
    y_new = np.array(y_new)
    x_new = np.arange(0, np.max(np.shape(y)), n)
    return x_new, y_new


# %% choose the suitable value of the list/array
def value_suit(data):
    data = np.array(data)
    delet = []
    for i in np.arange(0, np.size(data), 1):
        if data[i] <= 0:
            delet.append(i)
    data = np.delete(data, delet)

    data = np.sort(data)
    index = 0
    for i in np.arange(0, np.size(data) - 2, 1):
        if data[i + 2] - data[i + 1] > (data[i + 1] - data[0]):
            index = i + 1
            break
    if index >= (np.size(data) // 2):
        data = data[np.size(data) // 4:index // 4 * 3]
    else:
        data = data[(index + 1) + (np.size(data) - index) // 4:np.size(data) // 4 * 3]

    return np.average(data)


# %%
def phase_choose(data, n):
    data = np.sort(np.abs(data))
    std = []
    for j in np.arange(0, np.size(data) - n, 1):
        std.append(np.std(data[0, j:j + n]))
    index = std.index(min(std))
    return np.average(data[0, index:index + n])


# %%
def unwraping(data,jump_point=(180,540)):  # loop x 720

    loop=0
    while loop<np.min(jump_point):
        if  not np.isclose((data[jump_point[0]-loop]+data[jump_point[0]+loop])/2,data[jump_point[0]],atol=.5):
            if data[jump_point[0]+loop-1]>data[jump_point[0]+loop]:
                i=jump_point[0]+loop-1
                data[i + 1:] = data[i + 1:] + (data[i] - data[i + 1]) / np.abs(data[i + 1] - data[i]) * np.pi
                loop = jump_point[0]
            elif data[jump_point[0]-loop]>data[jump_point[0]-loop+1]:
                i=jump_point[0]-loop
                data[i + 1:] = data[i + 1:] + (data[i] - data[i + 1]) / np.abs(data[i + 1] - data[i]) * np.pi
                loop = jump_point[0]
            else:
                warnings.warn('error',category=FutureWarning)
        else:loop+=1

    loop = 0
    while loop < np.min(jump_point):
        if not np.isclose((data[jump_point[1] - loop] + data[jump_point[1] + loop]) / 2, data[jump_point[1]], atol=.5):
            if data[jump_point[1] + loop - 1] > data[jump_point[1] + loop]:
                i = jump_point[1] + loop - 1
                data[i + 1:] = data[i + 1:] + (data[i] - data[i + 1]) / np.abs(data[i + 1] - data[i]) * np.pi

                loop=jump_point[0]
            elif data[jump_point[1] - loop] > data[jump_point[1] - loop + 1]:
                i = jump_point[1] - loop
                data[i + 1:] = data[i + 1:] + (data[i] - data[i + 1]) / np.abs(data[i + 1] - data[i]) * np.pi
                loop = jump_point[0]
            else:
                warnings.warn('error', category=FutureWarning)
        else:
            loop += 1
    return data

#%%
def unwraping_shotnoise(data,jump_point=(180,540)):
    for i in jump_point:
        data[i + 1:] = data[i + 1:] + np.pi
    return data









