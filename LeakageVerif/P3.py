# File P3.py
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


st2_orig = symbol('st2_orig', 'S', 1)
st10_orig = symbol('st10_orig', 'S', 1)

r1 = symbol('r1', 'M', 1)
r2 = symbol('r2', 'M', 1)


st10 = st10_orig ^ r1
st10 = verif(st10, 1, 7)
st2 = st2_orig ^ r1
st2 = verif(st2, 2, 7)
r24  = st2 ^ zero
r24 = verif(r24, 3, 7)
r25  = st10 ^ zero
r25 = verif(r25, 4, 7)
sTT2 = r25 ^ zero
sTT2 = verif(sTT2, 5, 7)
sTT10 = r24 ^ zero
sTT10 = verif(sTT10, 6, 7)
output = sTT2 ^ sTT10
output = verif(output, 7, 7)
print_results()

