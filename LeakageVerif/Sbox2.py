# File Sbox2.py
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
refresh_0_1 = symbol('refresh_0_1', 'M', 8)
r_0_1_0 = symbol('r_0_1_0', 'M', 8)
refresh_1_1 = symbol('refresh_1_1', 'M', 8)
r_0_1_1 = symbol('r_0_1_1', 'M', 8)
r_0_1_2 = symbol('r_0_1_2', 'M', 8)
r_0_1_3 = symbol('r_0_1_3', 'M', 8)

x_1 = x ^ x_0
x_1 = verif(x_1, 1, 43)
z_0 = x_0 * x_0
z_0 = verif(z_0, 2, 43)
z_1 = x_1 * x_1
z_1 = verif(z_1, 3, 43)
z_0 = z_0 ^ refresh_0_1
z_0 = verif(z_0, 4, 43)
z_1 = z_1 ^ refresh_0_1
z_1 = verif(z_1, 5, 43)
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 6, 43)
tmp_secMult_j_i = z_1 * x_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 7, 43)
r_1_0 = r_0_1_0 ^ tmp_secMult_i_j
r_1_0 = verif(r_1_0, 8, 43)
r_1_0 = r_1_0 ^ tmp_secMult_j_i
r_1_0 = verif(r_1_0, 9, 43)
y_0 = z_0 * x_0
y_0 = verif(y_0, 10, 43)
y_0 = y_0 ^ r_0_1_0
y_0 = verif(y_0, 11, 43)
y_1 = z_1 * x_1
y_1 = verif(y_1, 12, 43)
y_1 = y_1 ^ r_1_0
y_1 = verif(y_1, 13, 43)
w_0 = y_0 * y_0 * y_0 * y_0
w_0 = verif(w_0, 14, 43)
w_1 = y_1 * y_1 * y_1 * y_1
w_1 = verif(w_1, 15, 43)
w_0 = w_0 ^ refresh_1_1
w_0 = verif(w_0, 16, 43)
w_1 = w_1 ^ refresh_1_1
w_1 = verif(w_1, 17, 43)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 18, 43)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 19, 43)
r_1_0 = r_0_1_1 ^ tmp_secMult_i_j
r_1_0 = verif(r_1_0, 20, 43)
r_1_0 = r_1_0 ^ tmp_secMult_j_i
r_1_0 = verif(r_1_0, 21, 43)
y_0 = y_0 * w_0
y_0 = verif(y_0, 22, 43)
y_0 = y_0 ^ r_0_1_1
y_0 = verif(y_0, 23, 43)
y_1 = y_1 * w_1
y_1 = verif(y_1, 24, 43)
y_1 = y_1 ^ r_1_0
y_1 = verif(y_1, 25, 43)
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_0 = verif(y_0, 26, 43)
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
y_1 = verif(y_1, 27, 43)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 28, 43)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 29, 43)
r_1_0 = r_0_1_2 ^ tmp_secMult_i_j
r_1_0 = verif(r_1_0, 30, 43)
r_1_0 = r_1_0 ^ tmp_secMult_j_i
r_1_0 = verif(r_1_0, 31, 43)
y_0 = y_0 * w_0
y_0 = verif(y_0, 32, 43)
y_0 = y_0 ^ r_0_1_2
y_0 = verif(y_0, 33, 43)
y_1 = y_1 * w_1
y_1 = verif(y_1, 34, 43)
y_1 = y_1 ^ r_1_0
y_1 = verif(y_1, 35, 43)
tmp_secMult_i_j = y_0 * z_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 36, 43)
tmp_secMult_j_i = y_1 * z_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 37, 43)
r_1_0 = r_0_1_3 ^ tmp_secMult_i_j
r_1_0 = verif(r_1_0, 38, 43)
r_1_0 = r_1_0 ^ tmp_secMult_j_i
r_1_0 = verif(r_1_0, 39, 43)
y_0 = y_0 * z_0
y_0 = verif(y_0, 40, 43)
y_0 = y_0 ^ r_0_1_3
y_0 = verif(y_0, 41, 43)
y_1 = y_1 * z_1
y_1 = verif(y_1, 42, 43)
y_1 = y_1 ^ r_1_0
y_1 = verif(y_1, 43, 43)
print_results()



"""

x_1 = x ^ x_0
z_0 = x_0 * x_0
z_1 = x_1 * x_1
z_0 = z_0 ^ refresh_0_1
z_1 = z_1 ^ refresh_0_1
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_j_i = z_1 * x_0
r_1_0 = r_0_1_0 ^ tmp_secMult_i_j
r_1_0 = r_1_0 ^ tmp_secMult_j_i
y_0 = z_0 * x_0
y_0 = y_0 ^ r_0_1_0
y_1 = z_1 * x_1
y_1 = y_1 ^ r_1_0
w_0 = y_0 * y_0 * y_0 * y_0
w_1 = y_1 * y_1 * y_1 * y_1
w_0 = w_0 ^ refresh_1_1
w_1 = w_1 ^ refresh_1_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
r_1_0 = r_0_1_1 ^ tmp_secMult_i_j
r_1_0 = r_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * w_0
y_0 = y_0 ^ r_0_1_1
y_1 = y_1 * w_1
y_1 = y_1 ^ r_1_0
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
r_1_0 = r_0_1_2 ^ tmp_secMult_i_j
r_1_0 = r_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * w_0
y_0 = y_0 ^ r_0_1_2
y_1 = y_1 * w_1
y_1 = y_1 ^ r_1_0
tmp_secMult_i_j = y_0 * z_1
tmp_secMult_j_i = y_1 * z_0
r_1_0 = r_0_1_3 ^ tmp_secMult_i_j
r_1_0 = r_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * z_0
y_0 = y_0 ^ r_0_1_3
y_1 = y_1 * z_1
y_1 = y_1 ^ r_1_0

"""
