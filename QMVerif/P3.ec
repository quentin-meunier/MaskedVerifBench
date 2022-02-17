(* File P3.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)

op Ox00 byte

module M = {
  proc main(st2_orig st10_orig) = {

    r1 = $distr;
    r2 = $distr;

    st10 = st10_orig ^ r1;
    st2 = st2_orig ^ r1;
    r24  = st2 ^ Ox00;
    r25  = st10 ^ Ox00;
    sTT2 = r25 ^ Ox00;
    sTT10 = r24 ^ Ox00;
    output = sTT2 ^ sTT10;
  }
}

