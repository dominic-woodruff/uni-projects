#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Dominic Woodruff

import numpy as np
import matplotlib.pyplot as plt

#Code for Exercise 1

fig1, ax1 = plt.subplots()
ax1.plot([1, 2, 4, 5, 6, 10], [3, 8, 1, 1, 6, 9])

#Code for Exercise 2

fig2, ax2 = plt.subplots()
ax2.plot([0, 50], [0, 100])
ax2.plot([0, 50], [20, 60])
ax2.set_title("Cost-Revenue Projection")
ax2.set_xlabel('Items Sold')
ax2.set_ylabel("Dollars ($)")
ax2.legend(['Cost', 'Revenue'])
