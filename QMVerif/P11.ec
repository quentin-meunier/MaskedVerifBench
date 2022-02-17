(* File P11.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)

op Ox00 byte;
op Oxff byte;

module M = {
  proc main(k1 k2 k3) = {

    r1 = $distr;
    r2 = $distr;
    r3 = $distr;
    r4 = $distr;

    n31 = r3 ^ k3;
    n29 = r1;
    n28 = r2 ^ k2;
    n27 = r3 ^ k3;
    n25 = r1;
    n24 = r2;
    n21 = r2 ^ k2;
    n20 = r3;
    n19 = r1 ^ k1;
    n18 = r3 ^ k3;
    n17 = r3;
    n16 = r2;
    n15 = Oxff ^ n31;
    n14 = n28 ^ r1;
    n13 = Ox00 ^ n27;
    n12 = r2 ^ r1;
    n11 = bnot  Ox00;
    n10 = r3 & n21;
    n09 = n18 ^ n19;
    n08 = r2 & r3;
    n08 = bnot n08;
    n07 = n14 & n15;
    n07 = bnot n07;
    n06 = n12 & n13;
    n06 = bnot n06;
    n05 = n10 & n11;
    n04 = n06 & n07;
    n03 = n09 ^ n04;
    n02 = n03 ^ n05;
    n01 = n02 ^ r4;
    n00 = n01 ^ n08;
    output =  n00;
  }
}

