(* File P5.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)


module M = {
  proc main(x) = {

    R = $distr;
    rx = $distr;

    X = x ^ rx;
    T1 = X ^ R;
    T2 = T1 ^ R;
    T3 = T2 ^ X;
    R2 = R ^ rx;
    A1 = X ^ R2;
    A2 = A1 ^ R2;
    A3 = A2 ^ T3;
    output = A3;
  }
}

