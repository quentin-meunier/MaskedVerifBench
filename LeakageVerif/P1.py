# File P1.py
#
# Copyright (C) 2021, Sorbonne Universite, LIP6
# This file is part of the MaskedVerifBench project, under the GPL v3.0 license
# See https://www.gnu.org/licenses/gpl-3.0.en.html for license information
# SPDX-License-Identifier: GPL-3.0-only
# Author(s): Etienne Pons


from leakage_verif import *
from maskedbench_utils import *

zero = constant(0, 1)
un = constant(1, 1)

x0 = symbol('x0', 'P', 1)
x1 = symbol('x1', 'P', 1)
x2 = symbol('x2', 'P', 1)
x3 = symbol('x3', 'P', 1)
x4 = symbol('x4', 'P', 1)
x5 = symbol('x5', 'P', 1)
x6 = symbol('x6', 'P', 1)
x7 = symbol('x7', 'P', 1)
x8 = symbol('x8', 'P', 1)
x9 = symbol('x9', 'P', 1)
x10 = symbol('x10', 'P', 1)
x11 = symbol('x11', 'P', 1)
x12 = symbol('x12', 'P', 1)
x13 = symbol('x13', 'P', 1)
x14 = symbol('x14', 'P', 1)
x15 = symbol('x15', 'P', 1)

k0 = symbol('k0', 'S', 1)
k1 = symbol('k1', 'S', 1)
k2 = symbol('k2', 'S', 1)
k3 = symbol('k3', 'S', 1)
k4 = symbol('k4', 'S', 1)
k5 = symbol('k5', 'S', 1)
k6 = symbol('k6', 'S', 1)
k7 = symbol('k7', 'S', 1)
k8 = symbol('k8', 'S', 1)
k9 = symbol('k9', 'S', 1)
k10 = symbol('k10', 'S', 1)
k11 = symbol('k11', 'S', 1)
k12 = symbol('k12', 'S', 1)
k13 = symbol('k13', 'S', 1)
k14 = symbol('k14', 'S', 1)
k15 = symbol('k15', 'S', 1)

r0 = symbol('r0', 'M', 1)
r1 = symbol('r1', 'M', 1)
r2 = symbol('r2', 'M', 1)
r3 = symbol('r3', 'M', 1)
r4 = symbol('r4', 'M', 1)
r5 = symbol('r5', 'M', 1)
r6 = symbol('r6', 'M', 1)
r7 = symbol('r7', 'M', 1)
r8 = symbol('r8', 'M', 1)
r9 = symbol('r9', 'M', 1)
r10 = symbol('r10', 'M', 1)
r11 = symbol('r11', 'M', 1)
r12 = symbol('r12', 'M', 1)
r13 = symbol('r13', 'M', 1)
r14 = symbol('r14', 'M', 1)
r15 = symbol('r15', 'M', 1)


n011 = k0 ^ x0
n011 = verif(n011, 1, 33)
n012 = n011 ^ r0
n012 = verif(n012, 2, 33)
n021 = k1 ^ x1
n021 = verif(n021, 3, 33)
n022 = n021 ^ r1
n022 = verif(n022, 4, 33)
n031 = k2 ^ x2
n031 = verif(n031, 5, 33)
n032 = n031 ^ r2
n032 = verif(n032, 6, 33)
n041 = k3 ^ x3
n041 = verif(n041, 7, 33)
n042 = n041 ^ r3
n042 = verif(n042, 8, 33)
n051 = k4 ^ x4
n051 = verif(n051, 9, 33)
n052 = n051 ^ r4
n052 = verif(n052, 10, 33)
n061 = k5 ^ x5
n061 = verif(n061, 11, 33)
n062 = n061 ^ r5
n062 = verif(n062, 12, 33)
n071 = k6 ^ x6
n071 = verif(n071, 13, 33)
n072 = n071 ^ r6
n072 = verif(n072, 14, 33)
n081 = k7 ^ x7
n081 = verif(n081, 15, 33)
n082 = n081 ^ r7
n082 = verif(n082, 16, 33)
n091 = k8 ^ x8
n091 = verif(n091, 17, 33)
n092 = n091 ^ r8
n092 = verif(n092, 18, 33)
n101 = k9 ^ x8
n101 = verif(n101, 19, 33)
n102 = n101 ^ r9
n102 = verif(n102, 20, 33)
n111 = k10 ^ x10
n111 = verif(n111, 21, 33)
n112 = n111 ^ r10
n112 = verif(n112, 22, 33)
n121 = k11 ^ x11
n121 = verif(n121, 23, 33)
n122 = n121 ^ r11
n122 = verif(n122, 24, 33)
n131 = k12 ^ x12
n131 = verif(n131, 25, 33)
n132 = n131 ^ r12
n132 = verif(n132, 26, 33)
n141 = k13 ^ x13
n141 = verif(n141, 27, 33)
n142 = n141 ^ r13
n142 = verif(n142, 28, 33)
n151 = k14 ^ x14
n151 = verif(n151, 29, 33)
n152 = n151 ^ r14
n152 = verif(n152, 30, 33)
n161 = k15 ^ x15
n161 = verif(n161, 31, 33)
n162 = n161 ^ r15
n162 = verif(n162, 32, 33)
output = n012 ^ n022 ^ n032 ^ n042 ^ n052 ^ n062 ^ n072 ^ n082 ^ n092 ^ n102 ^ n112 ^ n122 ^ n132 ^ n142 ^ n152 ^ n162
output = verif(output, 33, 33)
print_results()

