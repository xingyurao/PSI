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
