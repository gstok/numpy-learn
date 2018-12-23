#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np;
import matplotlib.pyplot as plt;

x = np.arange(-6, 6, 0.1);
y = x * x;

plt.plot(x, y, label = "sin");
plt.xlabel("x");
plt.ylabel("y");
plt.legend();
plt.show();