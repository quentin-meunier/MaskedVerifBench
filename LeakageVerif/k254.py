# File k254.py
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
r_9_0_1 = symbol('r_9_0_1', 'M', 8)
refresh_3_1 = symbol('refresh_3_1', 'M', 8)
r_10_0_1 = symbol('r_10_0_1', 'M', 8)
r_11_0_1 = symbol('r_11_0_1', 'M', 8)
r_12_0_1 = symbol('r_12_0_1', 'M', 8)

x_1 = x ^ x_0
x_1 = verif(x_1, 1, 41)
z_0 = x_0 * x_0
z_0 = verif(z_0, 2, 41)
z_1 = x_1 * x_1
z_1 = verif(z_1, 3, 41)
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 4, 41)
tmp_secMult_j_i = z_1 * x_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 5, 41)
r_9_1_0 = r_9_0_1 ^ tmp_secMult_i_j
r_9_1_0 = verif(r_9_1_0, 6, 41)
r_9_1_0 = r_9_1_0 ^ tmp_secMult_j_i
r_9_1_0 = verif(r_9_1_0, 7, 41)
y_0 = z_0 * x_0
y_0 = verif(y_0, 8, 41)
y_0 = y_0 ^ r_9_0_1
y_0 = verif(y_0, 9, 41)
y_1 = z_1 * x_1
y_1 = verif(y_1, 10, 41)
y_1 = y_1 ^ r_9_1_0
y_1 = verif(y_1, 11, 41)
w_0 = y_0 * y_0 * y_0 * y_0
w_0 = verif(w_0, 12, 41)
w_1 = y_1 * y_1 * y_1 * y_1
w_1 = verif(w_1, 13, 41)
w_0 = w_0 ^ refresh_3_1
w_0 = verif(w_0, 14, 41)
w_1 = w_1 ^ refresh_3_1
w_1 = verif(w_1, 15, 41)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 16, 41)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 17, 41)
r_10_1_0 = r_10_0_1 ^ tmp_secMult_i_j
r_10_1_0 = verif(r_10_1_0, 18, 41)
r_10_1_0 = r_10_1_0 ^ tmp_secMult_j_i
r_10_1_0 = verif(r_10_1_0, 19, 41)
y_0 = y_0 * w_0
y_0 = verif(y_0, 20, 41)
y_0 = y_0 ^ r_10_0_1
y_0 = verif(y_0, 21, 41)
y_1 = y_1 * w_1
y_1 = verif(y_1, 22, 41)
y_1 = y_1 ^ r_10_1_0
y_1 = verif(y_1, 23, 41)
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_0 = verif(y_0, 24, 41)
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
y_1 = verif(y_1, 25, 41)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 26, 41)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 27, 41)
r_11_1_0 = r_11_0_1 ^ tmp_secMult_i_j
r_11_1_0 = verif(r_11_1_0, 28, 41)
r_11_1_0 = r_11_1_0 ^ tmp_secMult_j_i
r_11_1_0 = verif(r_11_1_0, 29, 41)
y_0 = y_0 * w_0
y_0 = verif(y_0, 30, 41)
y_0 = y_0 ^ r_11_0_1
y_0 = verif(y_0, 31, 41)
y_1 = y_1 * w_1
y_1 = verif(y_1, 32, 41)
y_1 = y_1 ^ r_11_1_0
y_1 = verif(y_1, 33, 41)
tmp_secMult_i_j = y_0 * z_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 34, 41)
tmp_secMult_j_i = y_1 * z_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 35, 41)
r_12_1_0 = r_12_0_1 ^ tmp_secMult_i_j
r_12_1_0 = verif(r_12_1_0, 36, 41)
r_12_1_0 = r_12_1_0 ^ tmp_secMult_j_i
r_12_1_0 = verif(r_12_1_0, 37, 41)
y_0 = y_0 * z_0
y_0 = verif(y_0, 38, 41)
y_0 = y_0 ^ r_12_0_1
y_0 = verif(y_0, 39, 41)
y_1 = y_1 * z_1
y_1 = verif(y_1, 40, 41)
y_1 = y_1 ^ r_12_1_0
y_1 = verif(y_1, 41, 41)
print_results()



"""

x_1 = x ^ x_0
z_0 = x_0 * x_0
z_1 = x_1 * x_1
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_j_i = z_1 * x_0
r_9_1_0 = r_9_0_1 ^ tmp_secMult_i_j
r_9_1_0 = r_9_1_0 ^ tmp_secMult_j_i
y_0 = z_0 * x_0
y_0 = y_0 ^ r_9_0_1
y_1 = z_1 * x_1
y_1 = y_1 ^ r_9_1_0
w_0 = y_0 * y_0 * y_0 * y_0
w_1 = y_1 * y_1 * y_1 * y_1
w_0 = w_0 ^ refresh_3_1
w_1 = w_1 ^ refresh_3_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
r_10_1_0 = r_10_0_1 ^ tmp_secMult_i_j
r_10_1_0 = r_10_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * w_0
y_0 = y_0 ^ r_10_0_1
y_1 = y_1 * w_1
y_1 = y_1 ^ r_10_1_0
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
r_11_1_0 = r_11_0_1 ^ tmp_secMult_i_j
r_11_1_0 = r_11_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * w_0
y_0 = y_0 ^ r_11_0_1
y_1 = y_1 * w_1
y_1 = y_1 ^ r_11_1_0
tmp_secMult_i_j = y_0 * z_1
tmp_secMult_j_i = y_1 * z_0
r_12_1_0 = r_12_0_1 ^ tmp_secMult_i_j
r_12_1_0 = r_12_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * z_0
y_0 = y_0 ^ r_12_0_1
y_1 = y_1 * z_1
y_1 = y_1 ^ r_12_1_0

"""
