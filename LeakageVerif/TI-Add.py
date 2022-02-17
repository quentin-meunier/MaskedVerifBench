# File TI-Add.py
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

# orr r4 , r12, r0, lsr #1
r4 = r12 | LShR(r0, 1)
r4 = verif(r4, 1, 94)
# lsl r12, r0 , #31
r12 = r0 << 31
r12 = verif(r12, 2, 94)
# and r5 , r0 , r2
r5 = r0 & r2
r5 = verif(r5, 3, 94)
# and r6 , r0 , r3
r6 = r0 & r3
r6 = verif(r6, 4, 94)
# eor r0 , r0 , r2
r0 = r0 ^ r2
r0 = verif(r0, 5, 94)
# eor r5 , r5 , r4
r5 = r5 ^ r4
r5 = verif(r5, 6, 94)
# eor r6 , r6 , r4
r6 = r6 ^ r4
r6 = verif(r6, 7, 94)
# and r9 , r1 , r2
r9 = r1 & r2
r9 = verif(r9, 8, 94)
# and r8 , r1 , r3
r8 = r1 & r3
r8 = verif(r8, 9, 94)
# eor r1 , r1 , r3
r1 = r1 ^ r3 
r1 = verif(r1, 10, 94)
# eor r5 , r5 , r8
r5 = r5 ^ r8
r5 = verif(r5, 11, 94)
# eor r6 , r6 , r9
r6 = r6 ^ r9
r6 = verif(r6, 12, 94)

# Iteration 1
# Generate mask
# orr r4 , r12, r0 , lsr #1
r4 = r12 | LShR(r0, 1)
verif(r4, 13, 94)
# lsl r12, r0 , #31
r12 = r0 << 31
verif(r12, 14, 94)
# and r7 , r0 , r5 , lsl #1
r7 = r0 & (r5 << 1)
verif(r7, 15, 94)
# and r8 , r1 , r5 , lsl #1
r8 = r1 & (r5 << 1)
verif(r8, 16, 94)
# and r10, r0 , r6 , lsl #1
r10 = r0 & (r6 << 1)
verif(r10, 17, 94)
# and r11, r1 , r6 , lsl #1
r11 = r1 & (r6 << 1)
verif(r11, 18, 94)
# eor r6 , r6 , r11
r6 = r6 ^ r11
verif(r6, 19, 94)
# eor r6 , r6 , r10
r6 = r6 ^ r10
verif(r6, 20, 94)
# eor r5 , r7 , r5
r5 = r7 ^ r5
verif(r5, 21, 94)
# eor r5 , r8 , r5
r5 = r8 ^ r5
verif(r5, 22, 94)
# and r2 , r0 , r0 , lsl #1
r2 = r0 & (r0 << 1)
verif(r2, 23, 94)
# and r3 , r1 , r0 , lsl #1
r3 = r1 & (r0 << 1)
verif(r3, 24, 94)
# and r10, r0 , r1 , lsl #1
r10 = r0 & (r1 << 1)
verif(r10, 25, 94)
# and r11, r1 , r1 , lsl #1
r11 = r1 & (r1 << 1)
verif(r11, 26, 94)
# eor r8 , r11, r4
r8 = r11 ^ r4
verif(r8, 27, 94)
# eor r8 , r10, r8
r8 = r10 ^ r8
verif(r8, 28, 94)
# eor r7 , r3 , r4
r7 = r3 ^ r4
verif(r7, 29, 94)
# eor r7 , r7 , r2
r7 = r7 ^ r2
verif(r7, 30, 94)
 

# Iteration 2
# Generate mask
# orr r4 , r12, r7 , lsr #1
r4 = r12 | LShR(r7, 1)
verif(r4, 31, 94)
# lsl r12, r7 , #31
r12 = r7 << 31
verif(r12, 32, 94)
# and r2 , r7 , r5 , lsl #2
r2 = r7 & (r5 << 2)
verif(r2, 33, 94)
# and r3 , r8 , r5 , lsl #2
r3 = r8 & (r5 << 2)
verif(r3, 34, 94)
# and r10, r7 , r6 , lsl #2
r10 = r7 & (r6 << 2)
verif(r10, 35, 94)
# and r11, r8 , r6 , lsl #2
r11 = r8 & (r6 << 2)
verif(r11, 36, 94)
# eor r6 , r6 , r11
r6 = r6 ^ r11
verif(r6, 37, 94)
# eor r6 , r6 , r10
r6 = r6 ^ r10
verif(r6, 38, 94)
# eor r5 , r2 , r5
r5 = r2 ^ r5
verif(r5, 39, 94)
# eor r5 , r3 , r5
r5 = r3 ^ r5
verif(r5, 40, 94)
# and r2 , r7 , r7 , lsl #2
r2 = r7 & (r7 << 2)
verif(r2, 41, 94)
# and r3 , r8 , r7 , lsl #2
r3 = r8 & (r7 << 2)
verif(r3, 42, 94)
# and r10, r7 , r8 , lsl #2
r10 = r7 & (r8 << 2)
verif(r10, 43, 94)
# and r11, r8 , r8 , lsl #2
r11 = r8 & (r8 << 2)
verif(r11, 44, 94)
# eor r8 , r11, r4
r8 = r11 ^ r4
verif(r8, 45, 94)
# eor r8 , r10, r8
r8 = r10 ^ r8
verif(r8, 46, 94)
# eor r7 , r3 , r4
r7 = r3 ^ r4
verif(r7, 47, 94)
# eor r7 , r7 , r2
r7 = r7 ^ r2
verif(r7, 48, 94)


# Iteration 3
# Generate mask
# orr r4 , r12, r7 , lsr #1
r4 = r12 | LShR(r7, 1)
verif(r4, 49, 94)
# lsl r12, r7 , #31
r12 = r7 << 31
verif(r12, 50, 94)
# and r2 , r7 , r5 , lsl #4
r2 = r7 & (r5 << 4)
verif(r2, 51, 94)
# and r3 , r7 , r6 , lsl #4
r3 = r7 & (r6 << 4)
verif(r3, 52, 94)
# and r9 , r8 , r5 , lsl #4
r9 = r8 & (r5 << 4)
verif(r9, 53, 94)
# and r10, r8 , r6 , lsl #4
r10 = r8 & (r6 << 4)
verif(r10, 54, 94)
# eor r5 , r5 , r2
r5 = r5 ^ r2
verif(r5, 55, 94)
# eor r6 , r6 , r3
r6 = r6 ^ r3
verif(r6, 56, 94)
# eor r5 , r5 , r9
r5 = r5 ^ r9
verif(r5, 57, 94)
# eor r6 , r6 , r10
r6 = r6 ^ r10
verif(r6, 58, 94)
# and r2 , r7 , r7 , lsl #4
r2 = r7 & (r7 << 4)
verif(r2, 59, 94)
# and r3 , r7 , r8 , lsl #4
r3 = r7 & (r8 << 4)
verif(r3, 60, 94)
# and r9 , r8 , r7 , lsl #4
r9 = r8 & (r7 << 4)
verif(r9, 61, 94)
# and r10, r8 , r8 , lsl #4
r10 = r8 & (r8 << 4)
verif(r10, 62, 94)
# eor r7 , r2 , r4
r7 = r2 ^ r4
verif(r7, 63, 94)
# eor r8 , r3 , r4
r8 = r3 ^ r4
verif(r8, 64, 94)
# eor r7 , r7 , r10
r7 = r7 ^ r10
verif(r7, 65, 94)
# eor r8 , r8 , r9
r8 = r8 ^ r9
verif(r8, 66, 94)
 

# Iteration 4
# Generate mask
# orr r4 , r12, r7 , lsr #1
r4 = r12 ^ LShR(r7, 1)
verif(r4, 67, 94)
# lsl r12, r7 , #31
r12 = r7 << 31
verif(r12, 68, 94)
# and r2 , r7 , r5 , lsl #8
r2 = r7 & (r5 << 8)
verif(r2, 69, 94)
# and r3 , r7 , r6 , lsl #8
r3 = r7 & (r6 << 8)
verif(r3, 70, 94)
# and r9 , r8 , r5 , lsl #8
r9 = r8 & (r5 << 8)
verif(r9, 71, 94)
# and r10, r8 , r6 , lsl #8
r10 = r8 & (r6 << 8)
verif(r10, 72, 94)
# eor r5 , r5 , r2
r5 = r5 ^ r2
verif(r5, 73, 94)
# eor r6 , r6 , r3
r6 = r6 ^ r3
verif(r6, 74, 94)
# eor r5 , r5 , r9
r5 = r5 ^ r9
verif(r5, 75, 94)
# eor r6 , r6 , r10
r6 = r6 ^ r10
verif(r6, 76, 94)
# and r2 , r7 , r7 , lsl #8
r2 = r7 & (r7 << 8)
verif(r2, 77, 94)
# and r3 , r7 , r8 , lsl #8
r3 = r7 & (r8 << 8)
verif(r3, 78, 94)
# and r9 , r8 , r7 , lsl #8
r9 = r8 & (r7 << 8)
verif(r9, 79, 94)
# and r10, r8 , r8 , lsl #8
r10 = r8 & (r8 << 8)
verif(r10, 80, 94)
# eor r7 , r2 , r4
r7 = r2 ^ r4
verif(r7, 81, 94)
# eor r8 , r3 , r4
r8 = r3 ^ r4
verif(r8, 82, 94)
# eor r7 , r7 , r10
r7 = r7 ^ r10
verif(r7, 83, 94)
# eor r8 , r8 , r9
r8 = r8 ^ r9
verif(r8, 84, 94)
 
    
# Post  loop
# and r2 , r7 , r5 , lsl #16
r2 = r7 & (r5 << 16)
verif(r2, 85, 94)
# and r3 , r7 , r6 , lsl #16
r3 = r7 & (r6 << 16)
verif(r3, 86, 94)
# and r9 , r8 , r5 , lsl #16
r9 = r8 & (r5 << 16)
verif(r9, 87, 94)
# and r10, r8 , r6 , lsl #16
r10 = r8 & (r6 << 16)
verif(r10, 88, 94)
# eor r5 , r5 , r2
r5 = r5 ^ r2
verif(r5, 89, 94)
# eor r6 , r6 , r3
r6 = r6 ^ r3
verif(r6, 90, 94)
# eor r5 , r5 , r9
r5 = r5 ^ r9
verif(r5, 91, 94)
# eor r6 , r6 , r10
r6 = r6 ^ r10
verif(r6, 92, 94)
# eor r0 , r0 , r5 , lsl #1
r0 = r0 ^ (r5 << 1)
verif(r0, 93, 94)
# eor r1 , r1 , r6 , lsl #1
r1 = r1 ^ (r6 << 1)
verif(r1, 94, 94)

#res = r0 ^ r1
#print('res : %s' % res)
# res is 0x17D71AD9

print_results()

