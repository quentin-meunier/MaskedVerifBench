# File B2A17.py
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

s = symbol('s', 'M', 8)
s = verif(s, 1, 12)
a_0 = s ^ x_0
a_0 = verif(a_0, 2, 12)
a_1 = s ^ x_1
a_1 = verif(a_1, 3, 12)
r = symbol('r', 'M', 8)
r = verif(r, 4, 12)
tmp = a_1 ^ r
tmp = verif(tmp, 5, 12)
u = a_0 ^ tmp
u = verif(u, 6, 12)
u = u - tmp
u = verif(u, 7, 12)
u = u ^ a_0
u = verif(u, 8, 12)
A_0 = a_0 ^ r
A_0 = verif(A_0, 9, 12)
A_0 = A_0 - r
A_0 = verif(A_0, 10, 12)
A_0 = A_0 ^ u
A_0 = verif(A_0, 11, 12)
A_1 = a_1
A_1 = verif(A_1, 12, 12)
print_results()


