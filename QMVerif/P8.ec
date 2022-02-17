(* File P8.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)

op Ox00 byte

module M = {
  proc main(k1 k2 k3) = {

    r1 = $distr;
    r2 = $distr;
    r3 = $distr;
    r4 = $distr;

    n01 = bnot r2;
    t1 = n01 & r3;
    n04 = k3 ^ r3;
    t2 = r2 & n04;
    t3 = r1 ^ Ox00;
    t4 = k1 ^ r1;
    n07 = k2 ^ r2;
    n08 = bnot n07;
    n09 = k3 ^ r3;
    t5 = n08 & n09;
    n12 = k2 ^ r2;
    t6 = n12 & r3;
    n14 = t2 ^ t6;
    n15 = t1 ^ t5;
    n11 = n14 ^ n15;
    n03 = n11 ^ r4;
    n16 = n03 ^ t4;
    n17 = n16 ^ t3;
    output = n17;
  }
}

