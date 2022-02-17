(* File P7.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)


module M = {
  proc main(k1 k2) = {

    r1 = $distr;
    r2 = $distr;
    r3 = $distr;

    n01 = k1 ^ r1;
    n02 = k2 ^ r2;
    n03 = n01 & n02;
    n04 = k1 ^ r1;
    n05 = r2 & n04;
    n06 = r1 & r2;
    n07 = n06 ^ r3;
    n08 = n05 & n07;
    n08 = bnot n08;
    n09 = k2 ^ r2;
    n10 = r1 & n09;
    n11 = n03 ^ n10;
    output = n11;
  }
}

