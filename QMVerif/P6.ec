(* File P6.ec *)
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

    n01 = k1 ^ r1;
    n02 = k2 ^ r2;
    n03 = n01 & n02;
    n04 = k2 ^ r2;
    n05 = r1 & n04;
    n06 = k1 ^ r1;
    n07 = r2 & n06;
    n08 = n05 ^ n07;
    n09 = n03 ^ n08;
    output = n09;
  }
}

