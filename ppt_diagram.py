# @Time    : 2022/10/18 13:23
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : ppt_diagram.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

from PSI_algorithms.Data_Process import outlier_delete

r = np.linspace(2, 6, 1000)
theta = 1 * np.pi * r

# %% 3+2
delta_r = 1 / 6
delta_theta = delta_r * np.pi

arrow_r = np.linspace(2 + delta_r, 4 + delta_r, 4)
arrow_r = np.delete(arrow_r, -1)
arrow_theta = 1 * np.pi * arrow_r

arrow_r_2 = np.linspace(4 + delta_r, 6 + delta_r, 4)
arrow_r_2 = np.delete(arrow_r_2, -1)
arrow_theta_2 = 1 * np.pi * arrow_r_2

plt.figure(figsize=(8, 8))
ax = plt.subplot(projection='polar')
plt.plot(theta, r, 'b')

style = "-|>,head_length=8, head_width=4, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2"

for i in np.arange(0, np.size(arrow_r), 1):
    kw = dict(arrowstyle=style, color='r')
    a1 = patches.FancyArrowPatch((0, 0), (arrow_theta[i], arrow_r[i]), **kw)
    if i == 0:
        plt.text(arrow_theta[i], arrow_r[i], r'${}$'.format(i + 1), fontsize=18)
    else:
        plt.text(arrow_theta[i], arrow_r[i] + .5, r'${}$'.format(i + 1), fontsize=18)
    plt.gca().add_patch(a1)

for i in np.arange(0, np.size(arrow_r_2) - 1, 1):
    kw = dict(arrowstyle=style, color='k')
    a1 = patches.FancyArrowPatch((0, 0), (arrow_theta_2[i], arrow_r_2[i]), **kw)
    if i == 0:
        plt.text(arrow_theta_2[i], arrow_r_2[i] + .2, r'${}$'.format(i + 4), fontsize=18)
    else:
        plt.text(arrow_theta_2[i], arrow_r_2[i] + .5, r'${}$'.format(i + 4), fontsize=18)

    plt.gca().add_patch(a1)

plt.plot(np.linspace(0, 0, 100), np.linspace(0, 2, 100), 'k')
plt.plot(np.linspace(0, np.pi / 6, 100), np.linspace(.7, .7, 100), 'k')
ax.text(np.pi / 30, 1, r'$kW_1(x,y)$', fontsize=15)

ax.set_rgrids([])
ax.set_thetagrids([])
ax.spines['polar'].set_visible(False)
plt.tight_layout()
plt.savefig('Images/ppt-picture/3+2', bbox_inches='tight')
plt.close()
# %% 5+1

delta_r = 1 / 6
arrow_r = np.linspace(2 + delta_r, 4 + delta_r, 6)
arrow_r = np.delete(arrow_r, -1)
arrow_theta = 1 * np.pi * arrow_r

arrow_r_2 = np.linspace(4 + delta_r, 6 + delta_r, 6)
arrow_r_2 = np.delete(arrow_r_2, -1)
arrow_theta_2 = 1 * np.pi * arrow_r_2

plt.figure(figsize=(8, 8))
ax = plt.subplot(projection='polar')
plt.plot(theta, r, 'b')

style = "-|>,head_length=8, head_width=4, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2"

for i in np.arange(0, np.size(arrow_r), 1):
    kw = dict(arrowstyle=style, color='r')
    a1 = patches.FancyArrowPatch((0, 0), (arrow_theta[i], arrow_r[i]), **kw)
    if i == 0:
        plt.text(arrow_theta[i], arrow_r[i], r'${}$'.format(i + 1), fontsize=18)
    elif i == 1:
        plt.text(arrow_theta[i], arrow_r[i] + .2, r'${}$'.format(i + 1), fontsize=18)
    else:
        plt.text(arrow_theta[i], arrow_r[i] + .5, r'${}$'.format(i + 1), fontsize=18)
    plt.gca().add_patch(a1)

for i in np.arange(0, np.size(arrow_r_2) - 4, 1):
    kw = dict(arrowstyle=style, color='k')
    a1 = patches.FancyArrowPatch((0, 0), (arrow_theta_2[i], arrow_r_2[i]), **kw)
    plt.text(arrow_theta_2[i], arrow_r_2[i] + .1, r'${}$'.format(i + 6), fontsize=18)
    plt.gca().add_patch(a1)

plt.plot(np.linspace(0, 0, 100), np.linspace(0, 2, 100), 'k')
plt.plot(np.linspace(0, np.pi / 6, 100), np.linspace(.7, .7, 100), 'k')
ax.text(np.pi / 30, 1, r'$kW_1(x,y)$', fontsize=15)
ax.set_rgrids([])
ax.set_thetagrids([])
ax.spines['polar'].set_visible(False)
plt.tight_layout()
plt.savefig('Images/ppt-picture/5+1', bbox_inches='tight')
plt.show(block=1)
# %%
form = np.random.normal(0, 0.3, size=(720, 720))
fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
x = np.linspace(0, 720, 720)
y = np.linspace(0, 720, 720)
X, Y = np.meshgrid(x, y)
z = form
ax.plot_surface(X, Y, z, cmap='rainbow')
ax.set_zlim(-10,10)
ax.set_xlabel(r'X,$\mu$m',fontsize=13)
ax.set_ylabel(r'Y,$\mu$m',fontsize=13)
ax.set_zlabel(r'Z,nm',fontsize=13)
ax.set_xticks([0,180,360,540,720],[0,464/4,464/2,464/4*3,464],fontsize=13)
ax.set_yticks([0,180,360,540,720],[0,464/4,464/2,464/4*3,464],fontsize=13)
ax.set_zticks([-10,-5,0,5,10],fontsize=13)
ax.grid(False)
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
plt.tight_layout()

plt.savefig('Images/ppt-picture/shot_noise', bbox_inches='tight')
plt.show(block=1)
