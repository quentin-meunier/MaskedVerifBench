# File TI-Add-Opt.py
#
# Copyright (C) 2021, Sorbonne Universite, LIP6
# This file is part of the MaskedVerifBench project, under the GPL v3.0 license
# See https://www.gnu.org/licenses/gpl-3.0.en.html for license information
# SPDX-License-Identifier: GPL-3.0-only
# Author(s): Quentin L. Meunier, Etienne Pons


from leakage_verif import *
from maskedbench_utils import *

# Computes r0 + r2

r0 = symbol("r0", "S", 32)
r1 = symbol("r1", "M", 32)
#r0 = constant(0x1234ABCD, 32)
#r1 = constant(0x6F3C94D1, 32)
r0 = r0 ^ r1
r2 = symbol("r2", "S", 32)
r3 = symbol("r3", "M", 32)
#r2 = constant(0x05A26F0C, 32)
#r3 = constant(0xA5F634CD, 32)
r2 = r2 ^ r3

r = symbol("r", "M", 32)
#r = constant(0xF00DBEEF, 32)

# lsr  r12, r12, #7 @ keep only one bit
r12 = constant(1, 32) & r


# Generate mask
# orr r11, r12, r0, lsr #1
r11 = r12 | LShR(r0, 1)
verif(r11, 1, 78)
# lsl r12, r0 , #31
r12 = r0 << 31
verif(r12, 2, 78)
# orn r4 , r0 , r3
r4 = r0 | ~r3
verif(r4, 3, 78)
# and r6 , r2 , r0
r6 = r2 & r0
verif(r6, 4, 78)
# orn r5 , r1 , r3
r5 = r1 | ~r3
verif(r5, 5, 78)
# and r7 , r2 , r1
r7 = r2 & r1
verif(r7, 6, 78)
# eor r5 , r7 , r5
r5 = r7 ^ r5
verif(r5, 7, 78)
# eor r4 , r6 , r4
r4 = r6 ^ r4
verif(r4, 8, 78)
# eor r2 , r2 , r0
r2 = r2 ^ r0
verif(r2, 9, 78)
# eor r3 , r1 , r3
r3 = r1 ^ r3
verif(r3, 10, 78)
# eor r5 , r5 , r11
r5 = r5 ^ r11
verif(r5, 11, 78)
# eor r4 , r11, r4
r4 = r11 ^ r4
verif(r4, 12, 78)

#  Iteration 1
# and r8 , r3 , r4, lsl #1
r8 = r3 & (r4 << 1)
verif(r8, 13, 78)
# and r9 , r2 , r4, lsl #1
r9 = r2 & (r4 << 1)
verif(r9, 14, 78)
# eor r4 , r9 , r4
r4 = r9 ^ r4
verif(r4, 15, 78)
# eor r4 , r8 , r4
r4 = r8 ^ r4
verif(r4, 16, 78)
# and r10, r3 , r5, lsl #1
r10 = r3 & (r5 << 1)
verif(r10, 17, 78)
# and r11, r2 , r5, lsl #1
r11 = r2 & (r5 << 1)
verif(r11, 18, 78)
# eor r5 , r10, r5
r5 = r10 ^ r5
verif(r5, 19, 78)
# eor r5 , r11, r5
r5 = r11 ^ r5
verif(r5, 20, 78)
# orn r8 , r3 , r3, lsl #1
r8 = r3 | ~(r3 << 1)
verif(r8, 21, 78)
# and r10, r3 , r2, lsl #1
r10 = r3 & (r2 << 1)
verif(r10, 22, 78)
# orn r9 , r2 , r3, lsl #1
r9 = r2 | ~(r3 << 1)
verif(r9, 23, 78)
# and r11, r2 , r2, lsl #1
r11 = r2 & (r2 << 1)
verif(r11, 24, 78)
# eor r7 , r10, r8
r7 = r10 ^ r8
verif(r7, 25, 78)
# eor r6 , r9 , r11
r6 = r9 ^ r11
verif(r6, 26, 78)

# Iteration 2
# and r8 , r7 , r4, lsl #2
r8 = r7 & (r4 << 2)
verif(r8, 27, 78)
# and r9 , r6 , r4, lsl #2
r9 = r6 & (r4 << 2)
verif(r9, 28, 78)
# eor r4 , r9 , r4
r4 = r9 ^ r4
verif(r4, 29, 78)
# eor r4 , r8 , r4
r4 = r8 ^ r4
verif(r4, 30, 78)
# and r10, r7 , r5, lsl #2
r10 = r7 & (r5 << 2)
verif(r10, 31, 78)
# and r11, r6 , r5, lsl #2
r11 = r6 & (r5 << 2)
verif(r11, 32, 78)
# eor r5 , r10, r5
r5 = r10 ^ r5
verif(r5, 33, 78)
# eor r5 , r11, r5
r5 = r11 ^ r5
verif(r5, 34, 78)
# orn r8 , r7 , r7, lsl #2
r8 = r7 | ~(r7 << 2)
verif(r8, 35, 78)
# and r10, r7 , r6, lsl #2
r10 = r7 & (r6 << 2)
verif(r10, 36, 78)
# orn r9 , r6 , r7, lsl #2
r9 = r6 | ~(r7 << 2)
verif(r9, 37, 78)
# and r11, r6 , r6, lsl #2
r11 = r6 & (r6 << 2)
verif(r11, 38, 78)
# eor r7 , r10, r8
r7 = r10 ^ r8
verif(r7, 39, 78)
# eor r6 , r9 , r11
r6 = r9 ^ r11
verif(r6, 40, 78)

# Iteration 3
# and r8 , r7 , r4, lsl #4
r8 = r7 & (r4 << 4)
verif(r8, 41, 78)
# and r9 , r6 , r4, lsl #4
r9 = r6 & (r4 << 4)
verif(r9, 42, 78)
# eor r4 , r9 , r4
r4 = r9 ^ r4
verif(r4, 43, 78)
# eor r4 , r8 , r4
r4 = r8 ^ r4
verif(r4, 44, 78)
# and r10, r7 , r5, lsl #4
r10 = r7 & (r5 << 4)
verif(r10, 45, 78)
# and r11, r6 , r5, lsl #4
r11 = r6 & (r5 << 4)
verif(r11, 46, 78)
# eor r5 , r10, r5
r5 = r10 ^ r5
verif(r5, 47, 78)
# eor r5 , r11, r5
r5 = r11 ^ r5
verif(r5, 48, 78)
# orn r8 , r7 , r7, lsl #4
r8 = r7 | ~(r7 << 4)
verif(r8, 49, 78)
# and r10, r7 , r6, lsl #4
r10 = r7 & (r6 << 4)
verif(r10, 50, 78)
# orn r9 , r6 , r7, lsl #4
r9 = r6 | ~(r7 << 4)
verif(r9, 51, 78)
# and r11, r6 , r6, lsl #4
r11 = r6 & (r6 << 4)
verif(r11, 52, 78)
# eor r7 , r10, r8
r7 = r10 ^ r8
verif(r7, 53, 78)
# eor r6 , r9 , r11
r6 = r9 ^ r11
verif(r6, 54, 78)

#  Iteration 4
#  and r8 , r7 , r4, lsl #8
r8 = r7 & (r4 << 8)
verif(r8, 55, 78)
#  and r9 , r6 , r4, lsl #8
r9 = r6 & (r4 << 8)
verif(r9, 56, 78)
#  eor r4 , r9 , r4
r4 = r9 ^ r4
verif(r4, 57, 78)
#  eor r4 , r8 , r4
r4 = r8 ^ r4
verif(r4, 58, 78)
#  and r10, r7 , r5, lsl #8
r10 = r7 & (r5 << 8)
verif(r10, 59, 78)
#  and r11, r6 , r5, lsl #8
r11 = r6 & (r5 << 8)
verif(r11, 60, 78)
#  eor r5 , r10, r5
r5 = r10 ^ r5
verif(r5, 61, 78)
#  eor r5 , r11, r5
r5 = r11 ^ r5
verif(r5, 62, 78)
#  orn r8 , r7 , r7, lsl #8
r8 = r7 | ~(r7 << 8)
verif(r8, 63, 78)
#  and r10, r7 , r6, lsl #8
r10 = r7 & (r6 << 8)
verif(r10, 64, 78)
#  orn r9 , r6 , r7, lsl #8
r9 = r6 | ~(r7 << 8)
verif(r9, 65, 78)
#  and r11, r6 , r6, lsl #8
r11 = r6 & (r6 << 8)
verif(r11, 66, 78)
#  eor r7 , r10, r8
r7 = r10 ^ r8
verif(r7, 67, 78)
#  eor r6 , r9 , r11
r6 = r9 ^ r11
verif(r6, 68, 78)

# Post loop
# and r9 , r7 , r4, lsl #16
r9 = r7 & (r4 << 16)
verif(r9, 69, 78)
# and r8 , r6 , r4, lsl #16
r8 = r6 & (r4 << 16)
verif(r8, 70, 78)
# eor r4 , r9 , r4
r4 = r9 ^ r4
verif(r4, 71, 78)
# eor r4 , r8 , r4
r4 = r8 ^ r4
verif(r4, 72, 78)
# and r11, r7 , r5, lsl #16
r11 = r7 & (r5 << 16)
verif(r11, 73, 78)
# and r10, r6 , r5, lsl #16
r10 = r6 & (r5 << 16)
verif(r10, 74, 78)
# eor r5 , r11, r5
r5 = r11 ^ r5
verif(r5, 75, 78)
# eor r5 , r10, r5
r5 = r10 ^ r5
verif(r5, 76, 78)
# eor r0 , r2 , r4, lsl #1
r0 = r2 ^ (r4 << 1)
verif(r0, 77, 78)
# eor r1 , r3 , r5, lsl #1
r1 = r3 ^ (r5 << 1)
verif(r1, 78, 78)

res = r0 ^ r1
#print('res : %s' % res)
# res is 0x17D71AD9

print_results()

