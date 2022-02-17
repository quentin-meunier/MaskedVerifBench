# File P4.py
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

C = symbol('C', 'M', 1)
rx = symbol('rx', 'M', 1)


X = x ^ rx
X = verif(X, 1, 7)
B = C ^ rx
B = verif(B, 2, 7)
A1 = B ^ X
A1 = verif(A1, 3, 7)
A2 = A1 ^ B
A2 = verif(A2, 4, 7)
A3 = A2 ^ C
A3 = verif(A3, 5, 7)
A4 = A3 ^ C
A4 = verif(A4, 6, 7)
output = A4
output = verif(output, 7, 7)
print_results()

