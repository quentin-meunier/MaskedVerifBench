(* File B2A17.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)


module M = {
  proc main(x) = {

    (* # Sharing x in 2 shares # *)
    x_0 = $distr;
    x_1 = x ^ x_0;
    s = $distr;
    a_0 = s ^ x_0;
    a_1 = s ^ x_1;
    r = $distr;
    tmp = a_1 ^ r;
    u = a_0 ^ tmp;
    u = u - tmp;
    u = u ^ a_0;
    A_0 = a_0 ^ r;
    A_0 = A_0 - r;
    A_0 = A_0 ^ u;
    A_1 = a_1;
  }
}

