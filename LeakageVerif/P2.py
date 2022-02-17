# File P2.py
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
k4 = symbol('k4', 'S', 1)
k5 = symbol('k5', 'S', 1)
k6 = symbol('k6', 'S', 1)
k7 = symbol('k7', 'S', 1)
k8 = symbol('k8', 'S', 1)

r11 = symbol('r11', 'M', 1)
r12 = symbol('r12', 'M', 1)
r13 = symbol('r13', 'M', 1)
r14 = symbol('r14', 'M', 1)
r15 = symbol('r15', 'M', 1)
r16 = symbol('r16', 'M', 1)
r17 = symbol('r17', 'M', 1)
r18 = symbol('r18', 'M', 1)
r21 = symbol('r21', 'M', 1)
r22 = symbol('r22', 'M', 1)
r23 = symbol('r23', 'M', 1)
r24 = symbol('r24', 'M', 1)
r25 = symbol('r25', 'M', 1)
r26 = symbol('r26', 'M', 1)
r27 = symbol('r27', 'M', 1)
r28 = symbol('r28', 'M', 1)


n11 = k1 ^ r11
n11 = verif(n11, 1, 25)
n12 = k2 ^ r12
n12 = verif(n12, 2, 25)
n13 = k3 ^ r13
n13 = verif(n13, 3, 25)
n14 = k4 ^ r14
n14 = verif(n14, 4, 25)
n15 = k5 ^ r15
n15 = verif(n15, 5, 25)
n16 = k6 ^ r16
n16 = verif(n16, 6, 25)
n17 = k7 ^ r17
n17 = verif(n17, 7, 25)
n18 = k8 ^ r18
n18 = verif(n18, 8, 25)
n21 = n11 ^ r11
n21 = verif(n21, 9, 25)
n22 = n12 ^ r12
n22 = verif(n22, 10, 25)
n23 = n13 ^ r13
n23 = verif(n23, 11, 25)
n24 = n14 ^ r14
n24 = verif(n24, 12, 25)
n25 = n15 ^ r15
n25 = verif(n25, 13, 25)
n26 = n16 ^ r16
n26 = verif(n26, 14, 25)
n27 = n17 ^ r17
n27 = verif(n27, 15, 25)
n28 = n18 ^ r18
n28 = verif(n28, 16, 25)
n31 = n21 ^ r21
n31 = verif(n31, 17, 25)
n32 = n22 ^ r22
n32 = verif(n32, 18, 25)
n33 = n23 ^ r23
n33 = verif(n33, 19, 25)
n34 = n24 ^ r24
n34 = verif(n34, 20, 25)
n35 = n25 ^ r25
n35 = verif(n35, 21, 25)
n36 = n26 ^ r26
n36 = verif(n36, 22, 25)
n37 = n27 ^ r27
n37 = verif(n37, 23, 25)
n38 = n28 ^ r28
n38 = verif(n38, 24, 25)
output = n31 ^ n32 ^ n33 ^ n34 ^ n35 ^ n36 ^ n37 ^ n38
output = verif(output, 25, 25)
print_results()

