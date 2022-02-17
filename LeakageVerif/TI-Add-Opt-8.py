# File TI-Add-Opt-8.py
#
# Copyright (C) 2021, Sorbonne Universite, LIP6
# This file is part of the MaskedVerifBench project, under the GPL v3.0 license
# See https://www.gnu.org/licenses/gpl-3.0.en.html for license information
# SPDX-License-Identifier: GPL-3.0-only
# Author(s): Quentin L. Meunier, Etienne Pons


from leakage_verif import *
from maskedbench_utils import *

# Computes r0 + r2

r0 = symbol("r0", "S", 8)
r1 = symbol("r1", "M", 8)
#r0 = constant(0x12, 8)
#r1 = constant(0x6F, 8)
r0 = r0 ^ r1
r2 = symbol("r2", "S", 8)
r3 = symbol("r3", "M", 8)
#r2 = constant(0x5C, 8)
#r3 = constant(0xA5, 8)
r2 = r2 ^ r3

r = symbol("r", "M", 8)
#r = constant(0xE6, 8)

# lsr  r12, r12, #7 @ keep only one bit
r12 = constant(1, 8) & r


# Generate mask
# orr r11, r12, r0, lsr #1
r11 = r12 | LShR(r0, 1)
verif(r11, 1, 50)
# lsl r12, r0 , #31
r12 = r0 << 7
verif(r12, 2, 50)
# orn r4 , r0 , r3
r4 = r0 | ~r3
verif(r4, 3, 50)
# and r6 , r2 , r0
r6 = r2 & r0
verif(r6, 4, 50)
# orn r5 , r1 , r3
r5 = r1 | ~r3
verif(r5, 5, 50)
# and r7 , r2 , r1
r7 = r2 & r1
verif(r7, 6, 50)
# eor r5 , r7 , r5
r5 = r7 ^ r5
verif(r5, 7, 50)
# eor r4 , r6 , r4
r4 = r6 ^ r4
verif(r4, 8, 50)
# eor r2 , r2 , r0
r2 = r2 ^ r0
verif(r2, 9, 50)
# eor r3 , r1 , r3
r3 = r1 ^ r3
verif(r3, 10, 50)
# eor r5 , r5 , r11
r5 = r5 ^ r11
verif(r5, 11, 50)
# eor r4 , r11, r4
r4 = r11 ^ r4
verif(r4, 12, 50)

#  Iteration 1
# and r8 , r3 , r4, lsl #1
r8 = r3 & (r4 << 1)
verif(r8, 13, 50)
# and r9 , r2 , r4, lsl #1
r9 = r2 & (r4 << 1)
verif(r9, 14, 50)
# eor r4 , r9 , r4
r4 = r9 ^ r4
verif(r4, 15, 50)
# eor r4 , r8 , r4
r4 = r8 ^ r4
verif(r4, 16, 50)
# and r10, r3 , r5, lsl #1
r10 = r3 & (r5 << 1)
verif(r10, 17, 50)
# and r11, r2 , r5, lsl #1
r11 = r2 & (r5 << 1)
verif(r11, 18, 50)
# eor r5 , r10, r5
r5 = r10 ^ r5
verif(r5, 19, 50)
# eor r5 , r11, r5
r5 = r11 ^ r5
verif(r5, 20, 50)
# orn r8 , r3 , r3, lsl #1
r8 = r3 | ~(r3 << 1)
verif(r8, 21, 50)
# and r10, r3 , r2, lsl #1
r10 = r3 & (r2 << 1)
verif(r10, 22, 50)
# orn r9 , r2 , r3, lsl #1
r9 = r2 | ~(r3 << 1)
verif(r9, 23, 50)
# and r11, r2 , r2, lsl #1
r11 = r2 & (r2 << 1)
verif(r11, 24, 50)
# eor r7 , r10, r8
r7 = r10 ^ r8
verif(r7, 25, 50)
# eor r6 , r9 , r11
r6 = r9 ^ r11
verif(r6, 26, 50)

# Iteration 2
# and r8 , r7 , r4, lsl #2
r8 = r7 & (r4 << 2)
verif(r8, 27, 50)
# and r9 , r6 , r4, lsl #2
r9 = r6 & (r4 << 2)
verif(r9, 28, 50)
# eor r4 , r9 , r4
r4 = r9 ^ r4
verif(r4, 29, 50)
# eor r4 , r8 , r4
r4 = r8 ^ r4
verif(r4, 30, 50)
# and r10, r7 , r5, lsl #2
r10 = r7 & (r5 << 2)
verif(r10, 31, 50)
# and r11, r6 , r5, lsl #2
r11 = r6 & (r5 << 2)
verif(r11, 32, 50)
# eor r5 , r10, r5
r5 = r10 ^ r5
verif(r5, 33, 50)
# eor r5 , r11, r5
r5 = r11 ^ r5
verif(r5, 34, 50)
# orn r8 , r7 , r7, lsl #2
r8 = r7 | ~(r7 << 2)
verif(r8, 35, 50)
# and r10, r7 , r6, lsl #2
r10 = r7 & (r6 << 2)
verif(r10, 36, 50)
# orn r9 , r6 , r7, lsl #2
r9 = r6 | ~(r7 << 2)
verif(r9, 37, 50)
# and r11, r6 , r6, lsl #2
r11 = r6 & (r6 << 2)
verif(r11, 38, 50)
# eor r7 , r10, r8
r7 = r10 ^ r8
verif(r7, 39, 50)
# eor r6 , r9 , r11
r6 = r9 ^ r11
verif(r6, 40, 50)

# Post loop
# and r9 , r7 , r4, lsl #16
r9 = r7 & (r4 << 4)
verif(r9, 41, 50)
# and r8 , r6 , r4, lsl #16
r8 = r6 & (r4 << 4)
verif(r8, 42, 50)
# eor r4 , r9 , r4
r4 = r9 ^ r4
verif(r4, 43, 50)
# eor r4 , r8 , r4
r4 = r8 ^ r4
verif(r4, 44, 50)
# and r11, r7 , r5, lsl #16
r11 = r7 & (r5 << 4)
verif(r11, 45, 50)
# and r10, r6 , r5, lsl #16
r10 = r6 & (r5 << 4)
verif(r10, 46, 50)
# eor r5 , r11, r5
r5 = r11 ^ r5
verif(r5, 47, 50)
# eor r5 , r10, r5
r5 = r10 ^ r5
verif(r5, 48, 50)
# eor r0 , r2 , r4, lsl #1
r0 = r2 ^ (r4 << 1)
verif(r0, 49, 50)
# eor r1 , r3 , r5, lsl #1
r1 = r3 ^ (r5 << 1)
verif(r1, 50, 50)

#res = r0 ^ r1
#print('res : %s' % res)
# res is 0x6E

print_results()

