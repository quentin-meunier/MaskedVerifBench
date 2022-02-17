# File TI-Add-8.py
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

# orr r4 , r12, r0, lsr #1
r4 = r12 | LShR(r0, 1)
r4 = verif(r4, 1, 58)
# lsl r12, r0 , #31
r12 = r0 << 7
r12 = verif(r12, 2, 58)
# and r5 , r0 , r2
r5 = r0 & r2
r5 = verif(r5, 3, 58)
# and r6 , r0 , r3
r6 = r0 & r3
r6 = verif(r6, 4, 58)
# eor r0 , r0 , r2
r0 = r0 ^ r2
r0 = verif(r0, 5, 58)
# eor r5 , r5 , r4
r5 = r5 ^ r4
r5 = verif(r5, 6, 58)
# eor r6 , r6 , r4
r6 = r6 ^ r4
r6 = verif(r6, 7, 58)
# and r9 , r1 , r2
r9 = r1 & r2
r9 = verif(r9, 8, 58)
# and r8 , r1 , r3
r8 = r1 & r3
r8 = verif(r8, 9, 58)
# eor r1 , r1 , r3
r1 = r1 ^ r3 
r1 = verif(r1, 10, 58)
# eor r5 , r5 , r8
r5 = r5 ^ r8
r5 = verif(r5, 11, 58)
# eor r6 , r6 , r9
r6 = r6 ^ r9
r6 = verif(r6, 12, 58)

# Iteration 1
# Generate mask
# orr r4 , r12, r0 , lsr #1
r4 = r12 | LShR(r0, 1)
verif(r4, 13, 58)
# lsl r12, r0 , #31
r12 = r0 << 7
verif(r12, 14, 58)
# and r7 , r0 , r5 , lsl #1
r7 = r0 & (r5 << 1)
verif(r7, 15, 58)
# and r8 , r1 , r5 , lsl #1
r8 = r1 & (r5 << 1)
verif(r8, 16, 58)
# and r10, r0 , r6 , lsl #1
r10 = r0 & (r6 << 1)
verif(r10, 17, 58)
# and r11, r1 , r6 , lsl #1
r11 = r1 & (r6 << 1)
verif(r11, 18, 58)
# eor r6 , r6 , r11
r6 = r6 ^ r11
verif(r6, 19, 58)
# eor r6 , r6 , r10
r6 = r6 ^ r10
verif(r6, 20, 58)
# eor r5 , r7 , r5
r5 = r7 ^ r5
verif(r5, 21, 58)
# eor r5 , r8 , r5
r5 = r8 ^ r5
verif(r5, 22, 58)
# and r2 , r0 , r0 , lsl #1
r2 = r0 & (r0 << 1)
verif(r2, 23, 58)
# and r3 , r1 , r0 , lsl #1
r3 = r1 & (r0 << 1)
verif(r3, 24, 58)
# and r10, r0 , r1 , lsl #1
r10 = r0 & (r1 << 1)
verif(r10, 25, 58)
# and r11, r1 , r1 , lsl #1
r11 = r1 & (r1 << 1)
verif(r11, 26, 58)
# eor r8 , r11, r4
r8 = r11 ^ r4
verif(r8, 27, 58)
# eor r8 , r10, r8
r8 = r10 ^ r8
verif(r8, 28, 58)
# eor r7 , r3 , r4
r7 = r3 ^ r4
verif(r7, 29, 58)
# eor r7 , r7 , r2
r7 = r7 ^ r2
verif(r7, 30, 58)
 

# Iteration 2
# Generate mask
# orr r4 , r12, r7 , lsr #1
r4 = r12 | LShR(r7, 1)
verif(r4, 31, 58)
# lsl r12, r7 , #31
r12 = r7 << 7
verif(r12, 32, 58)
# and r2 , r7 , r5 , lsl #2
r2 = r7 & (r5 << 2)
verif(r2, 33, 58)
# and r3 , r8 , r5 , lsl #2
r3 = r8 & (r5 << 2)
verif(r3, 34, 58)
# and r10, r7 , r6 , lsl #2
r10 = r7 & (r6 << 2)
verif(r10, 35, 58)
# and r11, r8 , r6 , lsl #2
r11 = r8 & (r6 << 2)
verif(r11, 36, 58)
# eor r6 , r6 , r11
r6 = r6 ^ r11
verif(r6, 37, 58)
# eor r6 , r6 , r10
r6 = r6 ^ r10
verif(r6, 38, 58)
# eor r5 , r2 , r5
r5 = r2 ^ r5
verif(r5, 39, 58)
# eor r5 , r3 , r5
r5 = r3 ^ r5
verif(r5, 40, 58)
# and r2 , r7 , r7 , lsl #2
r2 = r7 & (r7 << 2)
verif(r2, 41, 58)
# and r3 , r8 , r7 , lsl #2
r3 = r8 & (r7 << 2)
verif(r3, 42, 58)
# and r10, r7 , r8 , lsl #2
r10 = r7 & (r8 << 2)
verif(r10, 43, 58)
# and r11, r8 , r8 , lsl #2
r11 = r8 & (r8 << 2)
verif(r11, 44, 58)
# eor r8 , r11, r4
r8 = r11 ^ r4
verif(r8, 45, 58)
# eor r8 , r10, r8
r8 = r10 ^ r8
verif(r8, 46, 58)
# eor r7 , r3 , r4
r7 = r3 ^ r4
verif(r7, 47, 58)
# eor r7 , r7 , r2
r7 = r7 ^ r2
verif(r7, 48, 58)


# Post  loop
# and r2 , r7 , r5 , lsl #16
r2 = r7 & (r5 << 4)
verif(r2, 49, 58)
# and r3 , r7 , r6 , lsl #16
r3 = r7 & (r6 << 4)
verif(r3, 50, 58)
# and r9 , r8 , r5 , lsl #16
r9 = r8 & (r5 << 4)
verif(r9, 51, 58)
# and r10, r8 , r6 , lsl #16
r10 = r8 & (r6 << 4)
verif(r10, 52, 58)
# eor r5 , r5 , r2
r5 = r5 ^ r2
verif(r5, 53, 58)
# eor r6 , r6 , r3
r6 = r6 ^ r3
verif(r6, 54, 58)
# eor r5 , r5 , r9
r5 = r5 ^ r9
verif(r5, 55, 58)
# eor r6 , r6 , r10
r6 = r6 ^ r10
verif(r6, 56, 58)
# eor r0 , r0 , r5 , lsl #1
r0 = r0 ^ (r5 << 1)
verif(r0, 57, 58)
# eor r1 , r1 , r6 , lsl #1
r1 = r1 ^ (r6 << 1)
verif(r1, 58, 58)

#res = r0 ^ r1
#print('res : %s' % res)
# res is 0x6E

print_results()
