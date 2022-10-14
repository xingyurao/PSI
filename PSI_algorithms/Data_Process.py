# @Time    : 2022/10/13 11:59
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Data_Process.py
# @Software: PyCharm

import numpy as np


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
        data = data[np.size(data)//4:index//4 * 3]
    else:
        data = data[(index + 1)+(np.size(data)-index)//4:np.size(data)//4 * 3]

    return np.average(data)
