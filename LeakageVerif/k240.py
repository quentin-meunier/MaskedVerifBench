# File k240.py
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
r_4_0_1 = symbol('r_4_0_1', 'M', 8)
refresh_1_1 = symbol('refresh_1_1', 'M', 8)
r_5_0_1 = symbol('r_5_0_1', 'M', 8)

x_1 = x ^ x_0
x_1 = verif(x_1, 1, 25)
z_0 = x_0 * x_0
z_0 = verif(z_0, 2, 25)
z_1 = x_1 * x_1
z_1 = verif(z_1, 3, 25)
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 4, 25)
tmp_secMult_j_i = z_1 * x_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 5, 25)
r_4_1_0 = r_4_0_1 ^ tmp_secMult_i_j
r_4_1_0 = verif(r_4_1_0, 6, 25)
r_4_1_0 = r_4_1_0 ^ tmp_secMult_j_i
r_4_1_0 = verif(r_4_1_0, 7, 25)
y_0 = z_0 * x_0
y_0 = verif(y_0, 8, 25)
y_0 = y_0 ^ r_4_0_1
y_0 = verif(y_0, 9, 25)
y_1 = z_1 * x_1
y_1 = verif(y_1, 10, 25)
y_1 = y_1 ^ r_4_1_0
y_1 = verif(y_1, 11, 25)
w_0 = y_0 * y_0 * y_0 * y_0
w_0 = verif(w_0, 12, 25)
w_1 = y_1 * y_1 * y_1 * y_1
w_1 = verif(w_1, 13, 25)
w_0 = w_0 ^ refresh_1_1
w_0 = verif(w_0, 14, 25)
w_1 = w_1 ^ refresh_1_1
w_1 = verif(w_1, 15, 25)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 16, 25)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 17, 25)
r_5_1_0 = r_5_0_1 ^ tmp_secMult_i_j
r_5_1_0 = verif(r_5_1_0, 18, 25)
r_5_1_0 = r_5_1_0 ^ tmp_secMult_j_i
r_5_1_0 = verif(r_5_1_0, 19, 25)
y_0 = y_0 * w_0
y_0 = verif(y_0, 20, 25)
y_0 = y_0 ^ r_5_0_1
y_0 = verif(y_0, 21, 25)
y_1 = y_1 * w_1
y_1 = verif(y_1, 22, 25)
y_1 = y_1 ^ r_5_1_0
y_1 = verif(y_1, 23, 25)
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_0 = verif(y_0, 24, 25)
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
y_1 = verif(y_1, 25, 25)
print_results()



"""

x_1 = x ^ x_0
z_0 = x_0 * x_0
z_1 = x_1 * x_1
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_j_i = z_1 * x_0
r_4_1_0 = r_4_0_1 ^ tmp_secMult_i_j
r_4_1_0 = r_4_1_0 ^ tmp_secMult_j_i
y_0 = z_0 * x_0
y_0 = y_0 ^ r_4_0_1
y_1 = z_1 * x_1
y_1 = y_1 ^ r_4_1_0
w_0 = y_0 * y_0 * y_0 * y_0
w_1 = y_1 * y_1 * y_1 * y_1
w_0 = w_0 ^ refresh_1_1
w_1 = w_1 ^ refresh_1_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
r_5_1_0 = r_5_0_1 ^ tmp_secMult_i_j
r_5_1_0 = r_5_1_0 ^ tmp_secMult_j_i
y_0 = y_0 * w_0
y_0 = y_0 ^ r_5_0_1
y_1 = y_1 * w_1
y_1 = y_1 ^ r_5_1_0
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1

"""
