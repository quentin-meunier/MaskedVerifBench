(* File P2.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)


module M = {
  proc main(k1 k2 k3 k4 k5 k6 k7 k8) = {

    r11 = $distr;
    r12 = $distr;
    r13 = $distr;
    r14 = $distr;
    r15 = $distr;
    r16 = $distr;
    r17 = $distr;
    r18 = $distr;
    r21 = $distr;
    r22 = $distr;
    r23 = $distr;
    r24 = $distr;
    r25 = $distr;
    r26 = $distr;
    r27 = $distr;
    r28 = $distr;

    n11 = k1 ^ r11;
    n12 = k2 ^ r12;
    n13 = k3 ^ r13;
    n14 = k4 ^ r14;
    n15 = k5 ^ r15;
    n16 = k6 ^ r16;
    n17 = k7 ^ r17;
    n18 = k8 ^ r18;
    n21 = n11 ^ r11;
    n22 = n12 ^ r12;
    n23 = n13 ^ r13;
    n24 = n14 ^ r14;
    n25 = n15 ^ r15;
    n26 = n16 ^ r16;
    n27 = n17 ^ r17;
    n28 = n18 ^ r18;
    n31 = n21 ^ r21;
    n32 = n22 ^ r22;
    n33 = n23 ^ r23;
    n34 = n24 ^ r24;
    n35 = n25 ^ r25;
    n36 = n26 ^ r26;
    n37 = n27 ^ r27;
    n38 = n28 ^ r28;
    output = n31 ^ n32 ^ n33 ^ n34 ^ n35 ^ n36 ^ n37 ^ n38;
  }
}

