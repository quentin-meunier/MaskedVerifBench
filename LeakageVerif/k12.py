# File k12.py
#
# Copyright (C) 2021, Sorbonne Universite, LIP6
# This file is part of the MaskedVerifBench project, under the GPL v3.0 license
# See https://www.gnu.org/licenses/gpl-3.0.en.html for license information
# SPDX-License-Identifier: GPL-3.0-only
# Author(s): Etienne Pons


from leakage_verif import *
from maskedbench_utils import *

x = symbol('x', 'S', 8)
x_0 = symbol('x_0', 'M', 8)
r_1_0_1 = symbol('r_1_0_1', 'M', 8)

x_1 = x ^ x_0
x_1 = verif(x_1, 1, 13)
z_0 = x_0 * x_0
z_0 = verif(z_0, 2, 13)
z_1 = x_1 * x_1
z_1 = verif(z_1, 3, 13)
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 4, 13)
tmp_secMult_j_i = z_1 * x_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 5, 13)
r_1_1_0 = r_1_0_1 ^ tmp_secMult_i_j
r_1_1_0 = verif(r_1_1_0, 6, 13)
r_1_1_0 = r_1_1_0 ^ tmp_secMult_j_i
r_1_1_0 = verif(r_1_1_0, 7, 13)
y_0 = z_0 * x_0
y_0 = verif(y_0, 8, 13)
y_0 = y_0 ^ r_1_0_1
y_0 = verif(y_0, 9, 13)
y_1 = z_1 * x_1
y_1 = verif(y_1, 10, 13)
y_1 = y_1 ^ r_1_1_0
y_1 = verif(y_1, 11, 13)
w_0 = y_0 * y_0 * y_0 * y_0
w_0 = verif(w_0, 12, 13)
w_1 = y_1 * y_1 * y_1 * y_1
w_1 = verif(w_1, 13, 13)
print_results()



"""

x_1 = x ^ x_0
z_0 = x_0 * x_0
z_1 = x_1 * x_1
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_j_i = z_1 * x_0
r_1_1_0 = r_1_0_1 ^ tmp_secMult_i_j
r_1_1_0 = r_1_1_0 ^ tmp_secMult_j_i
y_0 = z_0 * x_0
y_0 = y_0 ^ r_1_0_1
y_1 = z_1 * x_1
y_1 = y_1 ^ r_1_1_0
w_0 = y_0 * y_0 * y_0 * y_0
w_1 = y_1 * y_1 * y_1 * y_1

"""
