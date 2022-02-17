# File P6.py
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

r1 = symbol('r1', 'M', 1)
r2 = symbol('r2', 'M', 1)


n01 = k1 ^ r1
n01 = verif(n01, 1, 10)
n02 = k2 ^ r2
n02 = verif(n02, 2, 10)
n03 = n01 & n02
n03 = verif(n03, 3, 10)
n04 = k2 ^ r2
n04 = verif(n04, 4, 10)
n05 = r1 & n04
n05 = verif(n05, 5, 10)
n06 = k1 ^ r1
n06 = verif(n06, 6, 10)
n07 = r2 & n06
n07 = verif(n07, 7, 10)
n08 = n05 ^ n07
n08 = verif(n08, 8, 10)
n09 = n03 ^ n08
n09 = verif(n09, 9, 10)
output = n09
output = verif(output, 10, 10)
print_results()

