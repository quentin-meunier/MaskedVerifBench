(* File k3.ec *)
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

    (*  SecExp254 of x  *)
    z_0 = pow2 x_0;
    z_1 = pow2 x_1;
    
    (* # SecMult of z and x # *)
    r_0_0_1 = $distr;
    tmp_secMult_i_j = z_0 * x_1;
    tmp_secMult_j_i = z_1 * x_0;
    r_0_1_0 = r_0_0_1 ^ tmp_secMult_i_j;
    r_0_1_0 = r_0_1_0 ^ tmp_secMult_j_i;
    y_0 = z_0 * x_0;
    y_0 = y_0 ^ r_0_0_1;
    y_1 = z_1 * x_1;
    y_1 = y_1 ^ r_0_1_0;
  }
}
    
