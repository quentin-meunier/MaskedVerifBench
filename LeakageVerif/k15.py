# File k15.py
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
r_2_0_1 = symbol('r_2_0_1', 'M', 8)
refresh_0_1 = symbol('refresh_0_1', 'M', 8)
r_3_0_1 = symbol('r_3_0_1', 'M', 8)

x_1 = x ^ x_0
x_1 = verif(x_1, 1, 23)
z_0 = x_0 * x_0
z_0 = verif(z_0, 2, 23)
z_1 = x_1 * x_1
z_1 = verif(z_1, 3, 23)
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 4, 23)
tmp_secMult_j_i = z_1 * x_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 5, 23)
r_2_1_0 = r_2_0_1 ^ tmp_secMult_i_j
r_2_1_0 = verif(r_2_1_0, 6, 23)
r_2_1_0 = r_2_1_0 ^ tmp_secMult_j_i
r_2_1_0 = verif(r_2_1_0, 7, 23)
y_0 = z_0 * x_0
y_0 = verif(y_0, 8, 23)
y_0 = y_0 ^ r_2_0_1
y_0 = verif(y_0, 9, 23)
y_1 = z_1 * x_1
y_1 = verif(y_1, 10, 23)
y_1 = y_1 ^ r_2_1_0
y_1 = verif(y_1, 11, 23)
w_0 = y_0 * y_0 * y_0 * y_0
w_0 = verif(w_0, 12, 23)
w_1 = y_1 * y_1 * y_1 * y_1
w_1 = verif(w_1, 13, 23)
w_0 = w_0 ^ refresh_0_1
w_0 = verif(w_0, 14, 23)
w_1 = w_1 ^ refresh_0_1
w_1 = verif(w_1, 15, 23)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 16, 23)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 17, 23)
r_3_1_0 = r_3_0_1 ^ tmp_secMult_i_j
r_3_1_0 = verif(r_3_1_0, 18, 23)
r_3_1_0 = r_3_1_0 ^ tmp_secMult_j_i
r_3_1_0 = verif(r_3_1_0, 19, 23)
y_0 = y_0 * w_0
y_0 = verif(y_0, 20, 23)
y_0 = y_0 ^ r_3_0_1
y_0 = verif(y_0, 21, 23)
y_1 = y_1 * w_1
y_1 = verif(y_1, 22, 23)
y_1 = y_1 ^ r_3_1_0
y_1 = verif(y_1, 23, 23)
print_results()



"""

x_1 = x ^ x_0
z_0 = x_0 * x_0
z_1 = x_1 * x_1
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_j_i = z_1 * x_0
r_2_1_0 = r_2_0_1 ^ tmp_secMult_i_j
r_2_1_0 = r_2_1_0 ^ tmp_secMult_j_i
y_0 = z_0 * x_0
y_0 = y_0 ^ r_2_0_1
y_1 = z_1 * x_1
y_1 = y_1 ^ r_2_1_0
w_0 = y_0 * y_0 * y_0 * y_0
w_1 = y_1 * y_1 * y_1 * y_1
w_0 = w_0 ^ refresh_0_1
w_1 = w_1 ^ refresh_0_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
r_3_1_0 = r_3_0_1 ^ tmp_secMult_i_j
r_3_1_0 = r_3_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * w_0
y_0 = y_0 ^ r_3_0_1
y_1 = y_1 * w_1
y_1 = y_1 ^ r_3_1_0

"""
