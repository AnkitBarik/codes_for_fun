#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

plt.style.use('dark_background')

x = np.linspace(-1,1,100)
y = np.linspace(-1,1,100)

xx,yy = np.meshgrid(x,y)

source1 = np.array([-0.5,0.0])
source2 = np.array([0.5,0.0])

rr1 = np.sqrt((xx-source1[0])**2 + (yy-source1[1])**2)
rr2 = np.sqrt((xx-source2[0])**2 + (yy-source2[1])**2)

B1x = -(xx-source1[0])/rr1**3 + (xx-source2[0])/rr2**3
B1y = -(yy-source1[1])/rr1**3 + (yy-source2[1])/rr2**3

fig, ax = plt.subplots(figsize=(6,6))

ax.streamplot(xx,yy,B1x,B1y,density=2,linewidth=1,arrowsize=1,arrowstyle='-|>')
ax.add_patch(Rectangle((-0.5,-0.1),1,0.2,fill=None,edgecolor='white',linewidth=2))

ax.set_aspect('equal')
ax.set_xlim(-1,1)
ax.set_ylim(-1,1)
ax.axis('off')
plt.tight_layout()
plt.show()
#plt.savefig('magnetic_field_lines.png',dpi=300)
