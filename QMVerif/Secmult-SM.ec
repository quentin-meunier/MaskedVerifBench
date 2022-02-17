(* File Secmult-SM.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)


module M = {
  proc main(a b) = {

    a0 = $distr;
    b0 = $distr;
    a1 = a ^ a0;
    b1 = b ^ b0;
    r0 = $distr;

    x0 = a1 * b0;
    x1 = a0 * b1;
    x2 = x1 ^ r0;
    x3 = x2 ^ x0;
    x4 = a0 * b0; 
    x5 = x4 ^ r0;
    x6 = a1 * b1;
    x7 = x6 ^ x3;

    return x5 ^ x7;
  }
}

