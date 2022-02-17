(* File Sbox2.ec *)
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

    (* # Sbox for x # *)
    
    (* ## SecExp254 of x ## *)
    z_0 = pow2 x_0;
    z_1 = pow2 x_1;
    
    (* ### Refresh masks for z ### *)
    refresh_0_1 = $distr;
    z_0 = z_0 ^ refresh_0_1;
    z_1 = z_1 ^ refresh_0_1;
    
    (* ### SecMult of z and x ### *)
    r_0_1_0 = $distr;
    tmp_secMult_i_j = z_0 * x_1;
    tmp_secMult_j_i = z_1 * x_0;
    r_1_0 = r_0_1_0 ^ tmp_secMult_i_j;
    r_1_0 = r_1_0 ^ tmp_secMult_j_i;
    y_0 = z_0 * x_0;
    y_0 = y_0 ^ r_0_1_0;
    y_1 = z_1 * x_1;
    y_1 = y_1 ^ r_1_0;
    
    w_0 = pow4 y_0;
    w_1 = pow4 y_1;
    
    (* ### Refresh masks for w ### *)
    refresh_1_1 = $distr;
    w_0 = w_0 ^ refresh_1_1;
    w_1 = w_1 ^ refresh_1_1;
    
    (* ### SecMult of y and w ### *)
    r_0_1_1 = $distr;
    tmp_secMult_i_j = y_0 * w_1;
    tmp_secMult_j_i = y_1 * w_0;
    r_1_0 = r_0_1_1 ^ tmp_secMult_i_j;
    r_1_0 = r_1_0 ^ tmp_secMult_j_i;
    y_0 = y_0 * w_0;
    y_0 = y_0 ^ r_0_1_1;
    y_1 = y_1 * w_1;
    y_1 = y_1 ^ r_1_0;
    
    y_0 = pow16 y_0;
    y_1 = pow16 y_1;
    
    (* ### SecMult of y and w ### *)
    r_0_1_2 = $distr;
    tmp_secMult_i_j = y_0 * w_1;
    tmp_secMult_j_i = y_1 * w_0;
    r_1_0 = r_0_1_2 ^ tmp_secMult_i_j;
    r_1_0 = r_1_0 ^ tmp_secMult_j_i;
    y_0 = y_0 * w_0;
    y_0 = y_0 ^ r_0_1_2;
    y_1 = y_1 * w_1;
    y_1 = y_1 ^ r_1_0;
    
    (* ### SecMult of y and z ### *)
    r_0_1_3 = $distr;
    tmp_secMult_i_j = y_0 * z_1;
    tmp_secMult_j_i = y_1 * z_0;
    r_1_0 = r_0_1_3 ^ tmp_secMult_i_j;
    r_1_0 = r_1_0 ^ tmp_secMult_j_i;
    y_0 = y_0 * z_0;
    y_0 = y_0 ^ r_0_1_3;
    y_1 = y_1 * z_1;
    y_1 = y_1 ^ r_1_0;
    
    y_0 = affineF y_0;
    y_1 = affineF y_1;
  }
}

