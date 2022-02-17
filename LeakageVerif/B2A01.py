# File B2A01.py
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
gamma = verif(gamma, 1, 8)
T = x_0 ^ gamma
T = verif(T, 2, 8)
T = T - gamma
T = verif(T, 3, 8)
T = T ^ x_0
T = verif(T, 4, 8)
gamma = gamma ^ x_1
gamma = verif(gamma, 5, 8)
x_0 = x_0 ^ gamma
x_0 = verif(x_0, 6, 8)
x_0 = x_0 - gamma
x_0 = verif(x_0, 7, 8)
x_0 = x_0 ^ T
x_0 = verif(x_0, 8, 8)
print_results()


