# @Time    : 2022/10/22 14:12
# @Author  : Xingyu Rao
# @Email   : x.rao@tu-braunschweig.de
# @File    : Test.py
# @Software: PyCharm

'''
#%% test sinPSI (8)
x = np.linspace(0, np.pi, 80)
y = np.array([])
for theta in np.linspace(0, np.pi, 80):
    I = np.zeros([8])
    for n in np.arange(0, 8, 1):
        I[n] = 1 + 5 * np.cos(theta + 2.93 * np.cos(np.pi / 8 * 1 + n * np.pi / 4))

    y = np.append(y, np.arctan(
        (-1.6647 * (I[1] - I[2] - I[5] + I[6])) / (-(I[0] + I[3] + I[4] + I[7]) + (I[1] + I[2] + I[5] + I[6]))))
'''

'''
#%% test halb number equal 0
for theta in np.linspace(0,np.pi*2,1000):

    for N in np.arange(4,100,2):
        all = 0
        for n in np.arange(0,N/2,1):
            all+=np.cos((theta+2*np.pi*(n-1)/N)*4)
        if not np.isclose(all,0,atol=1.e-5):
            print('error:',N)
            
'''

'''
# %% cos curve sampling 3sampling
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import mpl_toolkits.axisartist as axisartist

sampling = 3
kwx = np.pi / 3

x = np.linspace(0, 2 * np.pi, 1000)
y = np.cos(x)
plt.style.use('scientific')
fig = plt.figure()
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
# ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0, 0)
# 给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("->", size=1.0)
# 添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["y"].set_axisline_style("->", size=1.0)
# 设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")

plt.plot(x, y, 'k')
plt.xticks([0, np.pi / 2, np.pi, np.pi / 2 * 3, np.pi * 2], ['', '', '', '', ''])
plt.text(x=np.pi / 48, y=-.1, s=r'$0$', fontsize=13, verticalalignment="center", horizontalalignment="center")
plt.text(x=np.pi / 2.1, y=-.15, s=r'$\frac{\pi}{2}$', fontsize=16, verticalalignment="center",
         horizontalalignment="center")
plt.text(x=np.pi, y=.1, s=r'$\pi$', fontsize=13, verticalalignment="center", horizontalalignment="center")
plt.text(x=3 * np.pi / 2.05, y=.15, s=r'$\frac{3\pi}{2}$', fontsize=16, verticalalignment="center",
         horizontalalignment="center")
plt.text(x=2 * np.pi, y=-.1, s=r'$2\pi$', fontsize=13, verticalalignment="center", horizontalalignment="center")

plt.yticks([-1, 1], ['', ''])

style = "-|>,head_length=4, head_width=1, widthA=.5, widthB=.5, lengthA=0.2, lengthB=0.2"
kw = dict(arrowstyle=style, color='k')

for n in np.arange(kwx, np.pi * 2, 2 * np.pi / 3):
    a1 = patches.FancyArrowPatch((n, 0.), (n, np.cos(n)), **kw)
    # plt.text(arrow_theta_2[i], arrow_r_2[i] + .1, r'${}$'.format(i + 6), fontsize=18)
    plt.gca().add_patch(a1)
    plt.scatter(x=n, y=np.cos(n), marker='o', color='red', edgecolors='r', zorder=2)

style_2 = "<->,head_length=4, head_width=1, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2, angleA=0, angleB=0"
kw_2 = dict(arrowstyle=style_2, color='k')
a2 = patches.FancyArrowPatch((0, 0.2), (kwx, 0.2), **kw_2)
plt.gca().add_patch(a2)
plt.text(kwx / 2, .3, r'$kW_1(x,y)$', fontsize=13, verticalalignment="center", horizontalalignment="center")

plt.tight_layout()
plt.savefig('Images/ppt-picture/3-sampling', bbox_inches='tight')
plt.show(block=1)

# %% cos curve sampling 3sampling
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import mpl_toolkits.axisartist as axisartist

sampling = 3
kwx = np.pi / 3

x = np.linspace(0, 3.5 * np.pi, 1000)
y = np.cos(x)

plt.style.use('scientific')
fig = plt.figure()
ax = axisartist.Subplot(fig, 111)
fig.add_axes(ax)
# 通过set_visible方法设置绘图区所有坐标轴隐藏
ax.axis[:].set_visible(False)
# ax.new_floating_axis代表添加新的坐标轴
ax.axis["x"] = ax.new_floating_axis(0, 0)
# 给x坐标轴加上箭头
ax.axis["x"].set_axisline_style("->", size=1.0)
# 添加y坐标轴，且加上箭头
ax.axis["y"] = ax.new_floating_axis(1, 0)
ax.axis["y"].set_axisline_style("->", size=1.0)
# 设置x、y轴上刻度显示方向
ax.axis["x"].set_axis_direction("bottom")
ax.axis["y"].set_axis_direction("right")

plt.plot(x, y, 'k')
plt.xticks([0, np.pi / 2, np.pi, np.pi / 2 * 3, np.pi * 2], ['', '', '', '', ''])
plt.text(x=np.pi / 48, y=-.1, s=r'$0$', fontsize=13, verticalalignment="center", horizontalalignment="center")
plt.text(x=np.pi / 2.1, y=-.15, s=r'$\frac{\pi}{2}$', fontsize=16, verticalalignment="center",
         horizontalalignment="center")
plt.text(x=np.pi, y=.1, s=r'$\pi$', fontsize=13, verticalalignment="center", horizontalalignment="center")
plt.text(x=3 * np.pi / 2.05, y=.15, s=r'$\frac{3\pi}{2}$', fontsize=16, verticalalignment="center",
         horizontalalignment="center")
plt.text(x=2 * np.pi, y=-.1, s=r'$2\pi$', fontsize=13, verticalalignment="center", horizontalalignment="center")
plt.text(x=5 * np.pi / 2.03, y=-.15, s=r'$\frac{5\pi}{2}$', fontsize=16, verticalalignment="center",
         horizontalalignment="center")
plt.text(x=3 * np.pi, y=.1, s=r'$3\pi$', fontsize=13, verticalalignment="center", horizontalalignment="center")

plt.yticks([-1, 1], ['', ''])

style = "-|>,head_length=4, head_width=1, widthA=.5, widthB=.5, lengthA=0.2, lengthB=0.2"
kw = dict(arrowstyle=style, color='k')

for n in np.arange(kwx, np.pi * 3.5, 2 * np.pi / 3):
    a1 = patches.FancyArrowPatch((n, 0.), (n, np.cos(n)), **kw)
    # plt.text(arrow_theta_2[i], arrow_r_2[i] + .1, r'${}$'.format(i + 6), fontsize=18)
    plt.gca().add_patch(a1)
    plt.scatter(x=n, y=np.cos(n), marker='o', color='red', edgecolors='r', zorder=2)

style_2 = "<->,head_length=4, head_width=1, widthA=1.0, widthB=1.0, lengthA=0.2, lengthB=0.2, angleA=0, angleB=0"
kw_2 = dict(arrowstyle=style_2, color='k')
a2 = patches.FancyArrowPatch((0, 0.2), (kwx, 0.2), **kw_2)
plt.gca().add_patch(a2)
plt.text(kwx / 2, .3, r'$kW_1(x,y)$', fontsize=10, verticalalignment="center", horizontalalignment="center")

plt.tight_layout()
# plt.savefig('Images/ppt-picture/3+2-sampling', bbox_inches='tight')
plt.show(block=1)

'''
# %% write a data for test of .c of c language
import numpy as np
import matplotlib.pyplot as plt

from PSI_algorithms.unwrap import unwrap

# slope-along x-axis
data = np.zeros([1000, 3])
slope = -5
lamda = 530
factor = lamda / (2 * np.pi)
a = 0
b = 1
for n in np.arange(0, 1000, 1):
    data[n, :] = data[n, :] + n * slope


bild_1 = a + b * np.cos(data / factor + np.pi * 0 / 2)
bild_2 = a + b * np.cos(data / factor + np.pi * 1 / 2)
bild_3 = a + b * np.cos(data / factor + np.pi * 2 / 2)
bild_4 = a + b * np.cos(data / factor + np.pi * 3 / 2)

# np.savetxt('C:/Users/Administrator/Desktop/C_Test/data.txt', np.float32(bild_all.T), fmt='%f', delimiter=',')

# test for unwrapping
sin = bild_4
cos = bild_1

new_data = unwrap(sin=sin.T, cos=cos.T)

plt.figure()
plt.subplot(411)
plt.plot(sin[:,0])
plt.subplot(412)
plt.plot(cos[:,0])
plt.subplot(413)
plt.plot((sin/cos)[:,0])
plt.subplot(414)
plt.plot((new_data * factor)[0])
plt.show(block=1)
