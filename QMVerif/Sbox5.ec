(* File Sbox5.ec *)
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
    
    (* ### Refresh masks for z ### *)
    refresh_0_1 = $distr;
    z_0 = z_0 ^ refresh_0_1;
    z_1 = z_1 ^ refresh_0_1;
    refresh_0_2 = $distr;
    z_0 = z_0 ^ refresh_0_2;
    z_2 = z_2 ^ refresh_0_2;
    
    (* ### SecMult of z and x ### *)
    out_0 = z_0 * x_0;
    out_1 = z_1 * x_1;
    out_2 = z_2 * x_2;
    s0 = $distr;
    tmp_secMult_i_j = z_0 * x_1;
    tmp_secMult_j_i = z_1 * x_0;
    sp = s0 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_0 = out_0 ^ s0;
    out_1 = out_1 ^ sp;
    s1 = $distr;
    tmp_secMult_i_j = z_0 * x_2;
    tmp_secMult_j_i = z_2 * x_0;
    sp = s1 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_0 = out_0 ^ s1;
    out_2 = out_2 ^ sp;
    s2 = $distr;
    tmp_secMult_i_j = z_1 * x_2;
    tmp_secMult_j_i = z_2 * x_1;
    sp = s2 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_1 = out_1 ^ s2;
    out_2 = out_2 ^ sp;
    y_0 = out_0;
    y_1 = out_1;
    y_2 = out_2;
    
    w_0 = pow4 y_0;
    w_1 = pow4 y_1;
    w_2 = pow4 y_2;
    
    (* ### Refresh masks for w ### *)
    refresh_1_1 = $distr;
    w_0 = w_0 ^ refresh_1_1;
    w_1 = w_1 ^ refresh_1_1;
    refresh_1_2 = $distr;
    w_0 = w_0 ^ refresh_1_2;
    w_2 = w_2 ^ refresh_1_2;
    
    (* ### SecMult of y and w ### *)
    out_0 = y_0 * w_0;
    out_1 = y_1 * w_1;
    out_2 = y_2 * w_2;
    s3 = $distr;
    tmp_secMult_i_j = y_0 * w_1;
    tmp_secMult_j_i = y_1 * w_0;
    sp = s3 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_0 = out_0 ^ s3;
    out_1 = out_1 ^ sp;
    s4 = $distr;
    tmp_secMult_i_j = y_0 * w_2;
    tmp_secMult_j_i = y_2 * w_0;
    sp = s4 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_0 = out_0 ^ s4;
    out_2 = out_2 ^ sp;
    s5 = $distr;
    tmp_secMult_i_j = y_1 * w_2;
    tmp_secMult_j_i = y_2 * w_1;
    sp = s5 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_1 = out_1 ^ s5;
    out_2 = out_2 ^ sp;
    y_0 = out_0;
    y_1 = out_1;
    y_2 = out_2;
    
    y_0 = pow16 y_0;
    y_1 = pow16 y_1;
    y_2 = pow16 y_2;
    
    (* ### SecMult of y and w ### *)
    out_0 = y_0 * w_0;
    out_1 = y_1 * w_1;
    out_2 = y_2 * w_2;
    s6 = $distr;
    tmp_secMult_i_j = y_0 * w_1;
    tmp_secMult_j_i = y_1 * w_0;
    sp = s6 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_0 = out_0 ^ s6;
    out_1 = out_1 ^ sp;
    s7 = $distr;
    tmp_secMult_i_j = y_0 * w_2;
    tmp_secMult_j_i = y_2 * w_0;
    sp = s7 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_0 = out_0 ^ s7;
    out_2 = out_2 ^ sp;
    s8 = $distr;
    tmp_secMult_i_j = y_1 * w_2;
    tmp_secMult_j_i = y_2 * w_1;
    sp = s8 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_1 = out_1 ^ s8;
    out_2 = out_2 ^ sp;
    y_0 = out_0;
    y_1 = out_1;
    y_2 = out_2;
    
    (* ### SecMult of y and z ### *)
    out_0 = y_0 * z_0;
    out_1 = y_1 * z_1;
    out_2 = y_2 * z_2;
    s9 = $distr;
    tmp_secMult_i_j = y_0 * z_1;
    tmp_secMult_j_i = y_1 * z_0;
    sp = s9 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_0 = out_0 ^ s9;
    out_1 = out_1 ^ sp;
    s10 = $distr;
    tmp_secMult_i_j = y_0 * z_2;
    tmp_secMult_j_i = y_2 * z_0;
    sp = s10 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_0 = out_0 ^ s10;
    out_2 = out_2 ^ sp;
    s11 = $distr;
    tmp_secMult_i_j = y_1 * z_2;
    tmp_secMult_j_i = y_2 * z_1;
    sp = s11 ^ tmp_secMult_i_j;
    sp = sp ^ tmp_secMult_j_i;
    out_1 = out_1 ^ s11;
    out_2 = out_2 ^ sp;
    y_0 = out_0;
    y_1 = out_1;
    y_2 = out_2;
    
    y_0 = affineF y_0;
    y_1 = affineF y_1;
    y_2 = affineF y_2;
    y_0 = y_0 ^ Ox63;
  }
}

