# @Time    : 2022/10/18 13:23
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : ppt_diagram.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

r=np.linspace(2,6,1000)
theta=1*np.pi*r


arrow_r=np.linspace(2,4,4)
arrow_theta=1*np.pi*arrow_r


plt.figure()
ax=plt.subplot(projection='polar')
plt.plot(theta,r,'r')

style = "-|>,head_length=4, head_width=2, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2"
kw = dict(arrowstyle=style, color="k")

for i in np.arange(0,4,1):
    a1=patches.FancyArrowPatch((0,0),(arrow_theta[i],arrow_r[i]),**kw)
    plt.gca().add_patch(a1)





ax.set_rgrids([])
ax.set_thetagrids([])
ax.spines['polar'].set_visible(False)
plt.show(block=1)