# File Sbox4.py
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
rh_0_0_1 = symbol('rh_0_0_1', 'M', 8)
rhp_0_0_1 = symbol('rhp_0_0_1', 'M', 8)
rh_1_0_1 = symbol('rh_1_0_1', 'M', 8)
rhp_1_0_1 = symbol('rhp_1_0_1', 'M', 8)
s0 = symbol('s0', 'M', 8)
s1 = symbol('s1', 'M', 8)

x_1 = x ^ x_0
x_1 = verif(x_1, 1, 69)
z_0 = x_0 * x_0
z_0 = verif(z_0, 2, 69)
z_1 = x_1 * x_1
z_1 = verif(z_1, 3, 69)
tmp_h_0 = rhp_0_0_1 * rhp_0_0_1
tmp_h_0 = verif(tmp_h_0, 4, 69)
tmp_h_0 = x_0 * tmp_h_0
tmp_h_0 = verif(tmp_h_0, 5, 69)
tmp_h_0 = rh_0_0_1 ^ tmp_h_0
tmp_h_0 = verif(tmp_h_0, 6, 69)
tmp_h_1 = x_0 * x_0
tmp_h_1 = verif(tmp_h_1, 7, 69)
tmp_h_1 = rhp_0_0_1 * tmp_h_1
tmp_h_1 = verif(tmp_h_1, 8, 69)
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_0 = verif(tmp_h_0, 9, 69)
tmp_h_1 = x_1 ^ rhp_0_0_1
tmp_h_1 = verif(tmp_h_1, 10, 69)
tmp_h_1 = tmp_h_1 * tmp_h_1
tmp_h_1 = verif(tmp_h_1, 11, 69)
tmp_h_1 = x_0 * tmp_h_1
tmp_h_1 = verif(tmp_h_1, 12, 69)
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_0 = verif(tmp_h_0, 13, 69)
tmp_h_2 = x_0 * x_0
tmp_h_2 = verif(tmp_h_2, 14, 69)
tmp_h_1 = x_1 ^ rhp_0_0_1
tmp_h_1 = verif(tmp_h_1, 15, 69)
tmp_h_1 = tmp_h_1 * tmp_h_2
tmp_h_1 = verif(tmp_h_1, 16, 69)
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_0 = verif(tmp_h_0, 17, 69)
rh_0_1_0 = tmp_h_0
rh_0_1_0 = verif(rh_0_1_0, 18, 69)
tmp_h_0 = x_0 * x_0
tmp_h_0 = verif(tmp_h_0, 19, 69)
y_0 = x_0 * tmp_h_0
y_0 = verif(y_0, 20, 69)
y_0 = y_0 ^ rh_0_0_1
y_0 = verif(y_0, 21, 69)
tmp_h_0 = x_1 * x_1
tmp_h_0 = verif(tmp_h_0, 22, 69)
y_1 = x_1 * tmp_h_0
y_1 = verif(y_1, 23, 69)
y_1 = y_1 ^ rh_0_1_0
y_1 = verif(y_1, 24, 69)
w_0 = y_0 * y_0 * y_0 * y_0
w_0 = verif(w_0, 25, 69)
w_1 = y_1 * y_1 * y_1 * y_1
w_1 = verif(w_1, 26, 69)
tmp_h_0 = rhp_1_0_1 * rhp_1_0_1 * rhp_1_0_1 * rhp_1_0_1
tmp_h_0 = verif(tmp_h_0, 27, 69)
tmp_h_0 = y_0 * tmp_h_0
tmp_h_0 = verif(tmp_h_0, 28, 69)
tmp_h_0 = rh_1_0_1 ^ tmp_h_0
tmp_h_0 = verif(tmp_h_0, 29, 69)
tmp_h_1 = y_0 * y_0 * y_0 * y_0
tmp_h_1 = verif(tmp_h_1, 30, 69)
tmp_h_1 = rhp_1_0_1 * tmp_h_1
tmp_h_1 = verif(tmp_h_1, 31, 69)
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_0 = verif(tmp_h_0, 32, 69)
tmp_h_1 = y_1 ^ rhp_1_0_1
tmp_h_1 = verif(tmp_h_1, 33, 69)
tmp_h_1 = tmp_h_1 * tmp_h_1 * tmp_h_1 * tmp_h_1
tmp_h_1 = verif(tmp_h_1, 34, 69)
tmp_h_1 = y_0 * tmp_h_1
tmp_h_1 = verif(tmp_h_1, 35, 69)
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_0 = verif(tmp_h_0, 36, 69)
tmp_h_2 = y_0 * y_0 * y_0 * y_0
tmp_h_2 = verif(tmp_h_2, 37, 69)
tmp_h_1 = y_1 ^ rhp_1_0_1
tmp_h_1 = verif(tmp_h_1, 38, 69)
tmp_h_1 = tmp_h_1 * tmp_h_2
tmp_h_1 = verif(tmp_h_1, 39, 69)
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_0 = verif(tmp_h_0, 40, 69)
rh_1_1_0 = tmp_h_0
rh_1_1_0 = verif(rh_1_1_0, 41, 69)
tmp_h_0 = y_0 * y_0 * y_0 * y_0
tmp_h_0 = verif(tmp_h_0, 42, 69)
y_0 = y_0 * tmp_h_0
y_0 = verif(y_0, 43, 69)
y_0 = y_0 ^ rh_1_0_1
y_0 = verif(y_0, 44, 69)
tmp_h_0 = y_1 * y_1 * y_1 * y_1
tmp_h_0 = verif(tmp_h_0, 45, 69)
y_1 = y_1 * tmp_h_0
y_1 = verif(y_1, 46, 69)
y_1 = y_1 ^ rh_1_1_0
y_1 = verif(y_1, 47, 69)
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_0 = verif(y_0, 48, 69)
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
y_1 = verif(y_1, 49, 69)
out_0 = y_0 * w_0
out_0 = verif(out_0, 50, 69)
out_1 = y_1 * w_1
out_1 = verif(out_1, 51, 69)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 52, 69)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 53, 69)
sp = s0 ^ tmp_secMult_i_j
sp = verif(sp, 54, 69)
sp = sp ^ tmp_secMult_j_i
sp = verif(sp, 55, 69)
out_0 = out_0 ^ s0
out_0 = verif(out_0, 56, 69)
out_1 = out_1 ^ sp
out_1 = verif(out_1, 57, 69)
y_0 = out_0
y_0 = verif(y_0, 58, 69)
y_1 = out_1
y_1 = verif(y_1, 59, 69)
out_0 = y_0 * z_0
out_0 = verif(out_0, 60, 69)
out_1 = y_1 * z_1
out_1 = verif(out_1, 61, 69)
tmp_secMult_i_j = y_0 * z_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 62, 69)
tmp_secMult_j_i = y_1 * z_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 63, 69)
sp = s1 ^ tmp_secMult_i_j
sp = verif(sp, 64, 69)
sp = sp ^ tmp_secMult_j_i
sp = verif(sp, 65, 69)
out_0 = out_0 ^ s1
out_0 = verif(out_0, 66, 69)
out_1 = out_1 ^ sp
out_1 = verif(out_1, 67, 69)
y_0 = out_0
y_0 = verif(y_0, 68, 69)
y_1 = out_1
y_1 = verif(y_1, 69, 69)
print_results()



"""

x_1 = x ^ x_0
z_0 = x_0 * x_0
z_1 = x_1 * x_1
tmp_h_0 = rhp_0_0_1 * rhp_0_0_1
tmp_h_0 = x_0 * tmp_h_0
tmp_h_0 = rh_0_0_1 ^ tmp_h_0
tmp_h_1 = x_0 * x_0
tmp_h_1 = rhp_0_0_1 * tmp_h_1
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_1 = x_1 ^ rhp_0_0_1
tmp_h_1 = tmp_h_1 * tmp_h_1
tmp_h_1 = x_0 * tmp_h_1
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_2 = x_0 * x_0
tmp_h_1 = x_1 ^ rhp_0_0_1
tmp_h_1 = tmp_h_1 * tmp_h_2
tmp_h_0 = tmp_h_0 ^ tmp_h_1
rh_0_1_0 = tmp_h_0
tmp_h_0 = x_0 * x_0
y_0 = x_0 * tmp_h_0
y_0 = y_0 ^ rh_0_0_1
tmp_h_0 = x_1 * x_1
y_1 = x_1 * tmp_h_0
y_1 = y_1 ^ rh_0_1_0
w_0 = y_0 * y_0 * y_0 * y_0
w_1 = y_1 * y_1 * y_1 * y_1
tmp_h_0 = rhp_1_0_1 * rhp_1_0_1 * rhp_1_0_1 * rhp_1_0_1
tmp_h_0 = y_0 * tmp_h_0
tmp_h_0 = rh_1_0_1 ^ tmp_h_0
tmp_h_1 = y_0 * y_0 * y_0 * y_0
tmp_h_1 = rhp_1_0_1 * tmp_h_1
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_1 = y_1 ^ rhp_1_0_1
tmp_h_1 = tmp_h_1 * tmp_h_1 * tmp_h_1 * tmp_h_1
tmp_h_1 = y_0 * tmp_h_1
tmp_h_0 = tmp_h_0 ^ tmp_h_1
tmp_h_2 = y_0 * y_0 * y_0 * y_0
tmp_h_1 = y_1 ^ rhp_1_0_1
tmp_h_1 = tmp_h_1 * tmp_h_2
tmp_h_0 = tmp_h_0 ^ tmp_h_1
rh_1_1_0 = tmp_h_0
tmp_h_0 = y_0 * y_0 * y_0 * y_0
y_0 = y_0 * tmp_h_0
y_0 = y_0 ^ rh_1_0_1
tmp_h_0 = y_1 * y_1 * y_1 * y_1
y_1 = y_1 * tmp_h_0
y_1 = y_1 ^ rh_1_1_0
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
out_0 = y_0 * w_0
out_1 = y_1 * w_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
sp = s0 ^ tmp_secMult_i_j
sp = sp ^ tmp_secMult_j_i
out_0 = out_0 ^ s0
out_1 = out_1 ^ sp
y_0 = out_0
y_1 = out_1
out_0 = y_0 * z_0
out_1 = y_1 * z_1
tmp_secMult_i_j = y_0 * z_1
tmp_secMult_j_i = y_1 * z_0
sp = s1 ^ tmp_secMult_i_j
sp = sp ^ tmp_secMult_j_i
out_0 = out_0 ^ s1
out_1 = out_1 ^ sp
y_0 = out_0
y_1 = out_1

"""
