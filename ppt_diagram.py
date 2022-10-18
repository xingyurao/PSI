# @Time    : 2022/10/18 13:23
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : ppt_diagram.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt

r=np.linspace(1,5,1000)
theta=1*np.pi*r-np.pi

plt.figure()
ax=plt.subplot(projection='polar')
plt.plot(theta,r,'r')

ax.set_rgrids([])
ax.set_thetagrids([])
plt.show(block=1)