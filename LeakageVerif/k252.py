# File k252.py
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
r_6_0_1 = symbol('r_6_0_1', 'M', 8)
refresh_2_1 = symbol('refresh_2_1', 'M', 8)
r_7_0_1 = symbol('r_7_0_1', 'M', 8)
r_8_0_1 = symbol('r_8_0_1', 'M', 8)

x_1 = x ^ x_0
x_1 = verif(x_1, 1, 33)
z_0 = x_0 * x_0
z_0 = verif(z_0, 2, 33)
z_1 = x_1 * x_1
z_1 = verif(z_1, 3, 33)
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 4, 33)
tmp_secMult_j_i = z_1 * x_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 5, 33)
r_6_1_0 = r_6_0_1 ^ tmp_secMult_i_j
r_6_1_0 = verif(r_6_1_0, 6, 33)
r_6_1_0 = r_6_1_0 ^ tmp_secMult_j_i
r_6_1_0 = verif(r_6_1_0, 7, 33)
y_0 = z_0 * x_0
y_0 = verif(y_0, 8, 33)
y_0 = y_0 ^ r_6_0_1
y_0 = verif(y_0, 9, 33)
y_1 = z_1 * x_1
y_1 = verif(y_1, 10, 33)
y_1 = y_1 ^ r_6_1_0
y_1 = verif(y_1, 11, 33)
w_0 = y_0 * y_0 * y_0 * y_0
w_0 = verif(w_0, 12, 33)
w_1 = y_1 * y_1 * y_1 * y_1
w_1 = verif(w_1, 13, 33)
w_0 = w_0 ^ refresh_2_1
w_0 = verif(w_0, 14, 33)
w_1 = w_1 ^ refresh_2_1
w_1 = verif(w_1, 15, 33)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 16, 33)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 17, 33)
r_7_1_0 = r_7_0_1 ^ tmp_secMult_i_j
r_7_1_0 = verif(r_7_1_0, 18, 33)
r_7_1_0 = r_7_1_0 ^ tmp_secMult_j_i
r_7_1_0 = verif(r_7_1_0, 19, 33)
y_0 = y_0 * w_0
y_0 = verif(y_0, 20, 33)
y_0 = y_0 ^ r_7_0_1
y_0 = verif(y_0, 21, 33)
y_1 = y_1 * w_1
y_1 = verif(y_1, 22, 33)
y_1 = y_1 ^ r_7_1_0
y_1 = verif(y_1, 23, 33)
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_0 = verif(y_0, 24, 33)
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
y_1 = verif(y_1, 25, 33)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 26, 33)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 27, 33)
r_8_1_0 = r_8_0_1 ^ tmp_secMult_i_j
r_8_1_0 = verif(r_8_1_0, 28, 33)
r_8_1_0 = r_8_1_0 ^ tmp_secMult_j_i
r_8_1_0 = verif(r_8_1_0, 29, 33)
y_0 = y_0 * w_0
y_0 = verif(y_0, 30, 33)
y_0 = y_0 ^ r_8_0_1
y_0 = verif(y_0, 31, 33)
y_1 = y_1 * w_1
y_1 = verif(y_1, 32, 33)
y_1 = y_1 ^ r_8_1_0
y_1 = verif(y_1, 33, 33)
print_results()



"""

x_1 = x ^ x_0
z_0 = x_0 * x_0
z_1 = x_1 * x_1
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_j_i = z_1 * x_0
r_6_1_0 = r_6_0_1 ^ tmp_secMult_i_j
r_6_1_0 = r_6_1_0 ^ tmp_secMult_j_i
y_0 = z_0 * x_0
y_0 = y_0 ^ r_6_0_1
y_1 = z_1 * x_1
y_1 = y_1 ^ r_6_1_0
w_0 = y_0 * y_0 * y_0 * y_0
w_1 = y_1 * y_1 * y_1 * y_1
w_0 = w_0 ^ refresh_2_1
w_1 = w_1 ^ refresh_2_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
r_7_1_0 = r_7_0_1 ^ tmp_secMult_i_j
r_7_1_0 = r_7_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * w_0
y_0 = y_0 ^ r_7_0_1
y_1 = y_1 * w_1
y_1 = y_1 ^ r_7_1_0
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
r_8_1_0 = r_8_0_1 ^ tmp_secMult_i_j
r_8_1_0 = r_8_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * w_0
y_0 = y_0 ^ r_8_0_1
y_1 = y_1 * w_1
y_1 = y_1 ^ r_8_1_0

"""
