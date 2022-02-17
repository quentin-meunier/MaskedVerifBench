(* File P1.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)


module M = {
    proc main(x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 k0 k1 k2 k3 k4 k5 k6 k7 k8 k9 k10 k11 k12 k13 k14 k15) = {

    r0 = $distr;
    r1 = $distr;
    r2 = $distr;
    r3 = $distr;
    r4 = $distr;
    r5 = $distr;
    r6 = $distr;
    r7 = $distr;
    r8 = $distr;
    r9 = $distr;
    r10 = $distr;
    r11 = $distr;
    r12 = $distr;
    r13 = $distr;
    r14 = $distr;
    r15 = $distr;

    n011 = k0 ^ x0;
    n012 = n011 ^ r0;
    n021 = k1 ^ x1;
    n022 = n021 ^ r1;
    n031 = k2 ^ x2;
    n032 = n031 ^ r2;
    n041 = k3 ^ x3;
    n042 = n041 ^ r3;
    n051 = k4 ^ x4;
    n052 = n051 ^ r4;
    n061 = k5 ^ x5;
    n062 = n061 ^ r5;
    n071 = k6 ^ x6;
    n072 = n071 ^ r6;
    n081 = k7 ^ x7;
    n082 = n081 ^ r7;
    n091 = k8 ^ x8;
    n092 = n091 ^ r8;
    n101 = k9 ^ x8;
    n102 = n101 ^ r9;
    n111 = k10 ^ x10;
    n112 = n111 ^ r10;
    n121 = k11 ^ x11;
    n122 = n121 ^ r11;
    n131 = k12 ^ x12;
    n132 = n131 ^ r12;
    n141 = k13 ^ x13;
    n142 = n141 ^ r13;
    n151 = k14 ^ x14;
    n152 = n151 ^ r14;
    n161 = k15 ^ x15;
    n162 = n161 ^ r15;
    output = n012 ^ n022 ^ n032 ^ n042 ^ n052 ^ n062 ^ n072 ^ n082 ^ n092 ^ n102 ^ n112 ^ n122 ^ n132 ^ n142 ^ n152 ^ n162;
  }
}

