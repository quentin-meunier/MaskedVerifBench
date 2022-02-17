# File P9.py
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


k1 = symbol('k1', 'S', 1)
k2 = symbol('k2', 'S', 1)
k3 = symbol('k3', 'S', 1)

r1 = symbol('r1', 'M', 1)
r2 = symbol('r2', 'M', 1)
r3 = symbol('r3', 'M', 1)
r4 = symbol('r4', 'M', 1)


n01 = ~r2
n01 = verif(n01, 1, 19)
t1 = n01 & r3
t1 = verif(t1, 2, 19)
n04 = k3 ^ r3
n04 = verif(n04, 3, 19)
t2 = r2 & n04
t2 = verif(t2, 4, 19)
t3 = r1 ^ zero
t3 = verif(t3, 5, 19)
t4 = k1 ^ r1
t4 = verif(t4, 6, 19)
n07 = k2 ^ r2
n07 = verif(n07, 7, 19)
n08 = ~n07
n08 = verif(n08, 8, 19)
n09 = k3 ^ r3
n09 = verif(n09, 9, 19)
t5 = n08 & n09
t5 = verif(t5, 10, 19)
n12 = k2 ^ r2
n12 = verif(n12, 11, 19)
t6 = n12 & r3
t6 = verif(t6, 12, 19)
n14 = t2 ^ t6
n14 = verif(n14, 13, 19)
n03 = n14 ^ r4
n03 = verif(n03, 14, 19)
n15 = t1 ^ t5
n15 = verif(n15, 15, 19)
n11 = n03 ^ n15
n11 = verif(n11, 16, 19)
n16 = n11 ^ t4
n16 = verif(n16, 17, 19)
n17 = n16 ^ t3
n17 = verif(n17, 18, 19)
output = n17
output = verif(output, 19, 19)
print_results()

