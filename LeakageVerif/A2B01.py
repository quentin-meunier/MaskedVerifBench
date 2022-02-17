# File A2B01.py
#
# Copyright (C) 2021, Sorbonne Universite, LIP6
# This file is part of the MaskedVerifBench project, under the GPL v3.0 license
# See https://www.gnu.org/licenses/gpl-3.0.en.html for license information
# SPDX-License-Identifier: GPL-3.0-only
# Author(s): Etienne Pons


from leakage_verif import *
from maskedbench_utils import *

x = symbol('x', 'S', 8)
x_1 = symbol('x_1', 'M', 8)
x_0 = x ^ x_1

gamma = symbol('gamma', 'M', 8)
gamma = verif(gamma, 1, 47)
T = gamma + gamma
T = verif(T, 2, 47)
y_0 = gamma ^ x_1
y_0 = verif(y_0, 3, 47)
omega = gamma & y_0
omega = verif(omega, 4, 47)
y_0 = T ^ x_0
y_0 = verif(y_0, 5, 47)
gamma = gamma ^ y_0
gamma = verif(gamma, 6, 47)
gamma = gamma & x_1
gamma = verif(gamma, 7, 47)
omega = omega ^ gamma
omega = verif(omega, 8, 47)
gamma = T & x_0
gamma = verif(gamma, 9, 47)
omega = omega ^ gamma
omega = verif(omega, 10, 47)
gamma = T & x_1
gamma = verif(gamma, 11, 47)
gamma = gamma ^ omega
gamma = verif(gamma, 12, 47)
T = T & x_0
T = verif(T, 13, 47)
gamma = gamma ^ T
gamma = verif(gamma, 14, 47)
T = gamma + gamma
T = verif(T, 15, 47)
gamma = T & x_1
gamma = verif(gamma, 16, 47)
gamma = gamma ^ omega
gamma = verif(gamma, 17, 47)
T = T & x_0
T = verif(T, 18, 47)
gamma = gamma ^ T
gamma = verif(gamma, 19, 47)
T = gamma + gamma
T = verif(T, 20, 47)
gamma = T & x_1
gamma = verif(gamma, 21, 47)
gamma = gamma ^ omega
gamma = verif(gamma, 22, 47)
T = T & x_0
T = verif(T, 23, 47)
gamma = gamma ^ T
gamma = verif(gamma, 24, 47)
T = gamma + gamma
T = verif(T, 25, 47)
gamma = T & x_1
gamma = verif(gamma, 26, 47)
gamma = gamma ^ omega
gamma = verif(gamma, 27, 47)
T = T & x_0
T = verif(T, 28, 47)
gamma = gamma ^ T
gamma = verif(gamma, 29, 47)
T = gamma + gamma
T = verif(T, 30, 47)
gamma = T & x_1
gamma = verif(gamma, 31, 47)
gamma = gamma ^ omega
gamma = verif(gamma, 32, 47)
T = T & x_0
T = verif(T, 33, 47)
gamma = gamma ^ T
gamma = verif(gamma, 34, 47)
T = gamma + gamma
T = verif(T, 35, 47)
gamma = T & x_1
gamma = verif(gamma, 36, 47)
gamma = gamma ^ omega
gamma = verif(gamma, 37, 47)
T = T & x_0
T = verif(T, 38, 47)
gamma = gamma ^ T
gamma = verif(gamma, 39, 47)
T = gamma + gamma
T = verif(T, 40, 47)
gamma = T & x_1
gamma = verif(gamma, 41, 47)
gamma = gamma ^ omega
gamma = verif(gamma, 42, 47)
T = T & x_0
T = verif(T, 43, 47)
gamma = gamma ^ T
gamma = verif(gamma, 44, 47)
T = gamma + gamma
T = verif(T, 45, 47)
y_0 = y_0 ^ T
y_0 = verif(y_0, 46, 47)
y_1 = x_1
y_1 = verif(y_1, 47, 47)
print_results()


