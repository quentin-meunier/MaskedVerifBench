# File P11.py
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


n31 = r3 ^ k3 
n31 = verif(n31, 1, 29)
n29 = r1 
n29 = verif(n29, 2, 29)
n28 = r2 ^ k2 
n28 = verif(n28, 3, 29)
n27 = r3 ^ k3 
n27 = verif(n27, 4, 29)
n25 = r1 
n25 = verif(n25, 5, 29)
n24 = r2 
n24 = verif(n24, 6, 29)
n21 = r2 ^ k2 
n21 = verif(n21, 7, 29)
n20 = r3 
n20 = verif(n20, 8, 29)
n19 = r1 ^ k1 
n19 = verif(n19, 9, 29)
n18 = r3 ^ k3 
n18 = verif(n18, 10, 29)
n17 = r3 
n17 = verif(n17, 11, 29)
n16 = r2 
n16 = verif(n16, 12, 29)
n15 = un ^ n31 
n15 = verif(n15, 13, 29)
n14 = n28 ^ r1 
n14 = verif(n14, 14, 29)
n13 = zero ^ n27 
n13 = verif(n13, 15, 29)
n12 = r2 ^ r1 
n12 = verif(n12, 16, 29)
n11 = ~ zero 
n11 = verif(n11, 17, 29)
n10 = r3 & n21 
n10 = verif(n10, 18, 29)
n09 = n18 ^ n19 
n09 = verif(n09, 19, 29)
n08 = r2 | r3 
n08 = verif(n08, 20, 29)
n07 = n14 | n15 
n07 = verif(n07, 21, 29)
n06 = n12 | n13 
n06 = verif(n06, 22, 29)
n05 = n10 & n11 
n05 = verif(n05, 23, 29)
n04 = n06 &  n07 
n04 = verif(n04, 24, 29)
n03 = n09 ^  n04 
n03 = verif(n03, 25, 29)
n02 = n03 ^  n05 
n02 = verif(n02, 26, 29)
n01 = n02 ^  r4 
n01 = verif(n01, 27, 29)
n00 = n01 ^ n08 
n00 = verif(n00, 28, 29)
output =  n00
output = verif(output, 29, 29)
print_results()

