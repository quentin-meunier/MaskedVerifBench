# File maskedbench_utils.py
#
# Copyright (C) 2021, Sorbonne Universite, LIP6
# This file is part of the MaskedVerifBench project, under the GPL v3.0 license
# See https://www.gnu.org/licenses/gpl-3.0.en.html for license information
# SPDX-License-Identifier: GPL-3.0-only
# Author(s): Etienne Pons

from __future__ import print_function
import sys, os

from leakage_verif.check_leakage import checkTpsVal
from leakage_verif.simplify import simplify

nbExps = 0
nbLeak = 0


def verif(e, i, n):
    global nbExps
    global nbLeak

    print("# Instruction {}/{}".format(i, n))
    e = simplify(e)

    nbExps += 1

    res, wordRes, niTime = checkTpsVal(e)
    if not res:
        nbLeak += 1
        print('# Leakage in value for exp num %d (Total leaks : %d)' % (nbExps, nbLeak))
        #sys.exit(0)

    return e


def print_results():
    global nbExps
    global nbLeak
    print('# Total Nb. of expression analysed: %d' % nbExps)
    print('# Total Nb. of potential leakages found: %d' % nbLeak)




