# File Sbox1.py
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
s0 = symbol('s0', 'M', 8)
refresh_1_1 = symbol('refresh_1_1', 'M', 8)
s1 = symbol('s1', 'M', 8)
s2 = symbol('s2', 'M', 8)
s3 = symbol('s3', 'M', 8)

x_1 = x ^ x_0
x_1 = verif(x_1, 1, 51)
z_0 = x_0 * x_0
z_0 = verif(z_0, 2, 51)
z_1 = x_1 * x_1
z_1 = verif(z_1, 3, 51)
z_0 = z_0 ^ refresh_0_1
z_0 = verif(z_0, 4, 51)
z_1 = z_1 ^ refresh_0_1
z_1 = verif(z_1, 5, 51)
out_0 = z_0 * x_0
out_0 = verif(out_0, 6, 51)
out_1 = z_1 * x_1
out_1 = verif(out_1, 7, 51)
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 8, 51)
tmp_secMult_j_i = z_1 * x_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 9, 51)
sp = s0 ^ tmp_secMult_i_j
sp = verif(sp, 10, 51)
sp = sp ^ tmp_secMult_j_i
sp = verif(sp, 11, 51)
out_0 = out_0 ^ s0
out_0 = verif(out_0, 12, 51)
out_1 = out_1 ^ sp
out_1 = verif(out_1, 13, 51)
y_0 = out_0
y_0 = verif(y_0, 14, 51)
y_1 = out_1
y_1 = verif(y_1, 15, 51)
w_0 = y_0 * y_0 * y_0 * y_0
w_0 = verif(w_0, 16, 51)
w_1 = y_1 * y_1 * y_1 * y_1
w_1 = verif(w_1, 17, 51)
w_0 = w_0 ^ refresh_1_1
w_0 = verif(w_0, 18, 51)
w_1 = w_1 ^ refresh_1_1
w_1 = verif(w_1, 19, 51)
out_0 = y_0 * w_0
out_0 = verif(out_0, 20, 51)
out_1 = y_1 * w_1
out_1 = verif(out_1, 21, 51)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 22, 51)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 23, 51)
sp = s1 ^ tmp_secMult_i_j
sp = verif(sp, 24, 51)
sp = sp ^ tmp_secMult_j_i
sp = verif(sp, 25, 51)
out_0 = out_0 ^ s1
out_0 = verif(out_0, 26, 51)
out_1 = out_1 ^ sp
out_1 = verif(out_1, 27, 51)
y_0 = out_0
y_0 = verif(y_0, 28, 51)
y_1 = out_1
y_1 = verif(y_1, 29, 51)
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_0 = verif(y_0, 30, 51)
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
y_1 = verif(y_1, 31, 51)
out_0 = y_0 * w_0
out_0 = verif(out_0, 32, 51)
out_1 = y_1 * w_1
out_1 = verif(out_1, 33, 51)
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 34, 51)
tmp_secMult_j_i = y_1 * w_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 35, 51)
sp = s2 ^ tmp_secMult_i_j
sp = verif(sp, 36, 51)
sp = sp ^ tmp_secMult_j_i
sp = verif(sp, 37, 51)
out_0 = out_0 ^ s2
out_0 = verif(out_0, 38, 51)
out_1 = out_1 ^ sp
out_1 = verif(out_1, 39, 51)
y_0 = out_0
y_0 = verif(y_0, 40, 51)
y_1 = out_1
y_1 = verif(y_1, 41, 51)
out_0 = y_0 * z_0
out_0 = verif(out_0, 42, 51)
out_1 = y_1 * z_1
out_1 = verif(out_1, 43, 51)
tmp_secMult_i_j = y_0 * z_1
tmp_secMult_i_j = verif(tmp_secMult_i_j, 44, 51)
tmp_secMult_j_i = y_1 * z_0
tmp_secMult_j_i = verif(tmp_secMult_j_i, 45, 51)
sp = s3 ^ tmp_secMult_i_j
sp = verif(sp, 46, 51)
sp = sp ^ tmp_secMult_j_i
sp = verif(sp, 47, 51)
out_0 = out_0 ^ s3
out_0 = verif(out_0, 48, 51)
out_1 = out_1 ^ sp
out_1 = verif(out_1, 49, 51)
y_0 = out_0
y_0 = verif(y_0, 50, 51)
y_1 = out_1
y_1 = verif(y_1, 51, 51)
print_results()



"""

x_1 = x ^ x_0
z_0 = x_0 * x_0
z_1 = x_1 * x_1
z_0 = z_0 ^ refresh_0_1
z_1 = z_1 ^ refresh_0_1
out_0 = z_0 * x_0
out_1 = z_1 * x_1
tmp_secMult_i_j = z_0 * x_1
tmp_secMult_j_i = z_1 * x_0
sp = s0 ^ tmp_secMult_i_j
sp = sp ^ tmp_secMult_j_i
out_0 = out_0 ^ s0
out_1 = out_1 ^ sp
y_0 = out_0
y_1 = out_1
w_0 = y_0 * y_0 * y_0 * y_0
w_1 = y_1 * y_1 * y_1 * y_1
w_0 = w_0 ^ refresh_1_1
w_1 = w_1 ^ refresh_1_1
out_0 = y_0 * w_0
out_1 = y_1 * w_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
sp = s1 ^ tmp_secMult_i_j
sp = sp ^ tmp_secMult_j_i
out_0 = out_0 ^ s1
out_1 = out_1 ^ sp
y_0 = out_0
y_1 = out_1
y_0 = y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0 * y_0
y_1 = y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1 * y_1
out_0 = y_0 * w_0
out_1 = y_1 * w_1
tmp_secMult_i_j = y_0 * w_1
tmp_secMult_j_i = y_1 * w_0
sp = s2 ^ tmp_secMult_i_j
sp = sp ^ tmp_secMult_j_i
out_0 = out_0 ^ s2
out_1 = out_1 ^ sp
y_0 = out_0
y_1 = out_1
out_0 = y_0 * z_0
out_1 = y_1 * z_1
tmp_secMult_i_j = y_0 * z_1
tmp_secMult_j_i = y_1 * z_0
sp = s3 ^ tmp_secMult_i_j
sp = sp ^ tmp_secMult_j_i
out_0 = out_0 ^ s3
out_1 = out_1 ^ sp
y_0 = out_0
y_1 = out_1

"""
