(* File ISW-AND.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)


module M = {
  proc main(a b) = {
    var a0, a1;
    var b0, b1;
    var c0, c1;
    var r0_01, r0_10, p0_01, p0_10;

    (* Presharing a *)
    a0 = $distr;
    a1 = a ^ a0;

    (* Presharing b *)
    b0 = $distr;
    b1 = b ^ b0;
    
    (* c = a * b *)
    r0_01 = $distr;
    p0_01 = a0 & b1;
    r0_10 = r0_01 ^ p0_01;
    p0_10 = a1 & b0;
    r0_10 = r0_10 ^ p0_10;
    c0 = a0 & b0;
    c0 = c0 ^ r0_01;
    c1 = a1 & b1;
    c1 = c1 ^ r0_10;
    return c0 ^ c1;
  }
}

