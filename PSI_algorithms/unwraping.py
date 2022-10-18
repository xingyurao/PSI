# @Time    : 2022/10/17 13:46
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : unwraping.py
# @Software: PyCharm


from PSI_algorithms.N_Step import *
import matplotlib.pyplot as plt
from PSI_algorithms.Data_Process import unwraping

# %%
data1, _ = n_step_single_line(step=3, loop=10)
data_0 = data1[0]
plt.figure()
plt.plot(data_0, 'b-')
plt.plot(unwraping(data_0), 'k--')
plt.show(block=1)
