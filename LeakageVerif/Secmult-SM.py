# File Secmult-SM.py
#
# Copyright (C) 2021, Sorbonne Universite, LIP6
# This file is part of the MaskedVerifBench project, under the GPL v3.0 license
# See https://www.gnu.org/licenses/gpl-3.0.en.html for license information
# SPDX-License-Identifier: GPL-3.0-only
# Author(s): Etienne Pons


from leakage_verif import *
from maskedbench_utils import *

a = symbol('a', 'S', 8)
b = symbol('b', 'S', 8)

a0 = symbol('a0', 'M', 8)
b0 = symbol('b0', 'M', 8)

r0_01 = symbol('r0_01', 'M', 8)

a1 = a ^ a0
a1 = verif(a1, 1, 10)
b1 = b ^ b0
b1 = verif(b1, 2, 10)
p0_01 = a0 * b1
p0_01 = verif(p0_01, 3, 10)
r0_10 = r0_01 ^ p0_01
r0_10 = verif(r0_10, 4, 10)
p0_10 = a1 * b0
p0_10 = verif(p0_10, 5, 10)
r0_10 = r0_10 ^ p0_10
r0_10 = verif(r0_10, 6, 10)
c0 = a0 * b0
c0 = verif(c0, 7, 10)
c0 = c0 ^ r0_01
c0 = verif(c0, 8, 10)
c1 = a1 * b1
c1 = verif(c1, 9, 10)
c1 = c1 ^ r0_10
c1 = verif(c1, 10, 10)

print_results()

