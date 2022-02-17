(* File P4.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)


module M = {
  proc main(x) = {

    C = $distr;
    rx = $distr;

    X = x ^ rx;
    B = C ^ rx;
    A1 = B ^ X;
    A2 = A1 ^ B;
    A3 = A2 ^ C;
    A4 = A3 ^ C;
    output = A4;
  }
}

