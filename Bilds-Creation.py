# @Time    : 2022/10/4 16:05
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Bilds-Creation.py
# @Software: PyCharm

# create bild of comparison with different steps
import matplotlib.pyplot as plt
from n_step_algorithms.n_step_Algorithms import *
import numpy as np


# 3 step PSI
phase_interval = (0, np.pi * 2)
get_value, m_std = n_step_single_line(step=3, phase=phase_interval)

m_std = outlier_delete(m_std)
plt.figure(1)
plt.plot(m_std)
plt.show()
