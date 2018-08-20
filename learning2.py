# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 14:26:51 2018

@author: fxia
"""

import numpy as np
import matplotlib.pyplot as plt

#set the x,y label number
x=np.linspace(0,10,1000)
y=np.sin(x)

plt.xkcd()
#create plot object
plt.figure(figsize=(8,4),dpi=300)

#plot in the current object
plt.plot(x,y,label='$sin(x)$', color='red',linewidth=2)

plt.xlabel('Time(s)')
plt.ylabel('speed')
plt.title('learning2')

plt.ylim(-1.2,1.2)
plt.legend()
plt.show
plt.savefig('sinx.jpg')