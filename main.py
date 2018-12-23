#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np;
import matplotlib.pyplot as plt;

def sigmoid (x):
    return 1 / (1 + np.exp(-x));

def softmax (x):
    c = np.max(x);
    expA = np.exp(x - c);
    sumExpA = np.sum(expA);
    y = expA / sumExpA;
    return y;

x = np.arange(0, 100, 1);
y = softmax(x);

plt.plot(x, y, label = "sin");
plt.xlabel("x");
plt.ylabel("y");
plt.legend();
plt.show();