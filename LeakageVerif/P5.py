# File P5.py
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


x = symbol('x', 'S', 1)

R = symbol('R', 'M', 1)
rx = symbol('rx', 'M', 1)


X = x ^ rx
X = verif(X, 1, 9)
T1 = X ^ R
T1 = verif(T1, 2, 9)
T2 = T1 ^ R
T2 = verif(T2, 3, 9)
T3 = T2 ^ X
T3 = verif(T3, 4, 9)
R2 = R ^ rx
R2 = verif(R2, 5, 9)
A1 = X ^ R2
A1 = verif(A1, 6, 9)
A2 = A1 ^ R2
A2 = verif(A2, 7, 9)
A3 = A2 ^ T3
A3 = verif(A3, 8, 9)
output = A3
output = verif(output, 9, 9)
print_results()

