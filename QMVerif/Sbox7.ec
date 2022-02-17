(* File Sbox7.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)

op Ox63 byte;

module M = {
  proc main(x) = {

    (* # Sharing x in 3 shares # *)
    x_0 = $distr;
    x_1 = $distr;
    x_2 = x ^ x_0 ^ x_1;

    (* # Sbox for x # *)
    
    (* ## SecExp254 of x ## *)
    z_0 = pow2 x_0;
    z_1 = pow2 x_1;
    z_2 = pow2 x_2;
    
    (* ### h : x -> x * pow2(x) ### *)
    rh_0_0_1 = $distr;
    rhp_0_0_1 = $distr;
    tmp_h_0 = pow2 rhp_0_0_1;
    tmp_h_0 = x_0 * tmp_h_0;
    tmp_h_0 = rh_0_0_1 ^ tmp_h_0;
    tmp_h_1 = pow2 x_0;
    tmp_h_1 = rhp_0_0_1 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_1 = x_1 ^ rhp_0_0_1;
    tmp_h_1 = pow2 tmp_h_1;
    tmp_h_1 = x_0 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_2 = pow2 x_0;
    tmp_h_1 = x_1 ^ rhp_0_0_1;
    tmp_h_1 = tmp_h_1 * tmp_h_2;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    rh_0_1_0 = tmp_h_0;
    rh_0_0_2 = $distr;
    rhp_0_0_2 = $distr;
    tmp_h_0 = pow2 rhp_0_0_2;
    tmp_h_0 = x_0 * tmp_h_0;
    tmp_h_0 = rh_0_0_2 ^ tmp_h_0;
    tmp_h_1 = pow2 x_0;
    tmp_h_1 = rhp_0_0_2 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_1 = x_2 ^ rhp_0_0_2;
    tmp_h_1 = pow2 tmp_h_1;
    tmp_h_1 = x_0 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_2 = pow2 x_0;
    tmp_h_1 = x_2 ^ rhp_0_0_2;
    tmp_h_1 = tmp_h_1 * tmp_h_2;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    rh_0_2_0 = tmp_h_0;
    rh_0_1_2 = $distr;
    rhp_0_1_2 = $distr;
    tmp_h_0 = pow2 rhp_0_1_2;
    tmp_h_0 = x_1 * tmp_h_0;
    tmp_h_0 = rh_0_1_2 ^ tmp_h_0;
    tmp_h_1 = pow2 x_1;
    tmp_h_1 = rhp_0_1_2 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_1 = x_2 ^ rhp_0_1_2;
    tmp_h_1 = pow2 tmp_h_1;
    tmp_h_1 = x_1 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_2 = pow2 x_1;
    tmp_h_1 = x_2 ^ rhp_0_1_2;
    tmp_h_1 = tmp_h_1 * tmp_h_2;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    rh_0_2_1 = tmp_h_0;
    tmp_h_0 = pow2 x_0;
    y_0 = x_0 * tmp_h_0;
    y_0 = y_0 ^ rh_0_0_1;
    y_0 = y_0 ^ rh_0_0_2;
    tmp_h_0 = pow2 x_1;
    y_1 = x_1 * tmp_h_0;
    y_1 = y_1 ^ rh_0_1_0;
    y_1 = y_1 ^ rh_0_1_2;
    tmp_h_0 = pow2 x_2;
    y_2 = x_2 * tmp_h_0;
    y_2 = y_2 ^ rh_0_2_0;
    y_2 = y_2 ^ rh_0_2_1;
    w_0 = pow4 y_0;
    w_1 = pow4 y_1;
    w_2 = pow4 y_2;
    
    (* ### h : y -> y * pow4(y) ### *)
    rh_1_0_1 = $distr;
    rhp_1_0_1 = $distr;
    tmp_h_0 = pow4 rhp_1_0_1;
    tmp_h_0 = y_0 * tmp_h_0;
    tmp_h_0 = rh_1_0_1 ^ tmp_h_0;
    tmp_h_1 = pow4 y_0;
    tmp_h_1 = rhp_1_0_1 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_1 = y_1 ^ rhp_1_0_1;
    tmp_h_1 = pow4 tmp_h_1;
    tmp_h_1 = y_0 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_2 = pow4 y_0;
    tmp_h_1 = y_1 ^ rhp_1_0_1;
    tmp_h_1 = tmp_h_1 * tmp_h_2;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    rh_1_1_0 = tmp_h_0;
    rh_1_0_2 = $distr;
    rhp_1_0_2 = $distr;
    tmp_h_0 = pow4 rhp_1_0_2;
    tmp_h_0 = y_0 * tmp_h_0;
    tmp_h_0 = rh_1_0_2 ^ tmp_h_0;
    tmp_h_1 = pow4 y_0;
    tmp_h_1 = rhp_1_0_2 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_1 = y_2 ^ rhp_1_0_2;
    tmp_h_1 = pow4 tmp_h_1;
    tmp_h_1 = y_0 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_2 = pow4 y_0;
    tmp_h_1 = y_2 ^ rhp_1_0_2;
    tmp_h_1 = tmp_h_1 * tmp_h_2;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    rh_1_2_0 = tmp_h_0;
    rh_1_1_2 = $distr;
    rhp_1_1_2 = $distr;
    tmp_h_0 = pow4 rhp_1_1_2;
    tmp_h_0 = y_1 * tmp_h_0;
    tmp_h_0 = rh_1_1_2 ^ tmp_h_0;
    tmp_h_1 = pow4 y_1;
    tmp_h_1 = rhp_1_1_2 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_1 = y_2 ^ rhp_1_1_2;
    tmp_h_1 = pow4 tmp_h_1;
    tmp_h_1 = y_1 * tmp_h_1;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    tmp_h_2 = pow4 y_1;
    tmp_h_1 = y_2 ^ rhp_1_1_2;
    tmp_h_1 = tmp_h_1 * tmp_h_2;
    tmp_h_0 = tmp_h_0 ^ tmp_h_1;
    rh_1_2_1 = tmp_h_0;
    tmp_h_0 = pow4 y_0;
    y_0 = y_0 * tmp_h_0;
    y_0 = y_0 ^ rh_1_0_1;
    y_0 = y_0 ^ rh_1_0_2;
    tmp_h_0 = pow4 y_1;
    y_1 = y_1 * tmp_h_0;
    y_1 = y_1 ^ rh_1_1_0;
    y_1 = y_1 ^ rh_1_1_2;
    tmp_h_0 = pow4 y_2;
    y_2 = y_2 * tmp_h_0;
    y_2 = y_2 ^ rh_1_2_0;
    y_2 = y_2 ^ rh_1_2_1;
    
    y_0 = pow16 y_0;
    y_1 = pow16 y_1;
    y_2 = pow16 y_2;
    
    (* ### SecMult of y and w ### *)
    r_0_0_1 = $distr;
    tmp_secMult_i_j = y_0 * w_1;
    tmp_secMult_j_i = y_1 * w_0;
    r_0_1_0 = r_0_0_1 ^ tmp_secMult_i_j;
    r_0_1_0 = r_0_1_0 ^ tmp_secMult_j_i;
    r_0_0_2 = $distr;
    tmp_secMult_i_j = y_0 * w_2;
    tmp_secMult_j_i = y_2 * w_0;
    r_0_2_0 = r_0_0_2 ^ tmp_secMult_i_j;
    r_0_2_0 = r_0_2_0 ^ tmp_secMult_j_i;
    r_0_1_2 = $distr;
    tmp_secMult_i_j = y_1 * w_2;
    tmp_secMult_j_i = y_2 * w_1;
    r_0_2_1 = r_0_1_2 ^ tmp_secMult_i_j;
    r_0_2_1 = r_0_2_1 ^ tmp_secMult_j_i;
    y_0 = y_0 * w_0;
    y_0 = y_0 ^ r_0_0_1;
    y_0 = y_0 ^ r_0_0_2;
    y_1 = y_1 * w_1;
    y_1 = y_1 ^ r_0_1_0;
    y_1 = y_1 ^ r_0_1_2;
    y_2 = y_2 * w_2;
    y_2 = y_2 ^ r_0_2_0;
    y_2 = y_2 ^ r_0_2_1;
    
    (* ### SecMult of y and z ### *)
    r_1_0_1 = $distr;
    tmp_secMult_i_j = y_0 * z_1;
    tmp_secMult_j_i = y_1 * z_0;
    r_1_1_0 = r_1_0_1 ^ tmp_secMult_i_j;
    r_1_1_0 = r_1_1_0 ^ tmp_secMult_j_i;
    r_1_0_2 = $distr;
    tmp_secMult_i_j = y_0 * z_2;
    tmp_secMult_j_i = y_2 * z_0;
    r_1_2_0 = r_1_0_2 ^ tmp_secMult_i_j;
    r_1_2_0 = r_1_2_0 ^ tmp_secMult_j_i;
    r_1_1_2 = $distr;
    tmp_secMult_i_j = y_1 * z_2;
    tmp_secMult_j_i = y_2 * z_1;
    r_1_2_1 = r_1_1_2 ^ tmp_secMult_i_j;
    r_1_2_1 = r_1_2_1 ^ tmp_secMult_j_i;
    y_0 = y_0 * z_0;
    y_0 = y_0 ^ r_1_0_1;
    y_0 = y_0 ^ r_1_0_2;
    y_1 = y_1 * z_1;
    y_1 = y_1 ^ r_1_1_0;
    y_1 = y_1 ^ r_1_1_2;
    y_2 = y_2 * z_2;
    y_2 = y_2 ^ r_1_2_0;
    y_2 = y_2 ^ r_1_2_1;
    
    y_0 = affineF y_0;
    y_1 = affineF y_1;
    y_2 = affineF y_2;
    y_0 = y_0 ^ Ox63;
  }
}

