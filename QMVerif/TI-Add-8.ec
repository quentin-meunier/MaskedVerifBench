(* File TI-Add-8.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)

op Ox01 byte;
op Ox02 byte;
op Ox04 byte;
op Ox07 byte;

module M = {
  proc main(x0 x2) = {

    r1 = $distr;
    r0 = x0 ^ r1;
    r3 = $distr;
    r2 = x2 ^ r3;

    r = $distr;
    r12 = Ox01 & r;

    tmp0 = r0 >> Ox01;
    tmpOR0 = bnot r12;
    tmpOR1 = bnot tmp0;
    r4 = tmpOR1 & tmpOR0;
    r12 = r0 << Ox07;
    r5 = r0 & r2;
    r6 = r0 & r3;
    r0 = r0 ^ r2;
    r5 = r5 ^ r4;
    r6 = r6 ^ r4;
    r9 = r1 & r2;
    r8 = r1 & r3;
    r1 = r1 ^ r3;
    r5 = r5 ^ r8;
    r6 = r6 ^ r9;
    tmp1 = r0 >> Ox01;
    tmpOR2 = bnot r12;
    tmpOR3 = bnot tmp1;
    r4 = tmpOR3 & tmpOR2;
    r12 = r0 << Ox07;
    tmp2 = r5 << Ox01;
    r7 = r0 & tmp2;
    tmp3 = r5 << Ox01;
    r8 = r1 & tmp3;
    tmp4 = r6 << Ox01;
    r10 = r0 & tmp4;
    tmp5 = r6 << Ox01;
    r11 = r1 & tmp5;
    r6 = r6 ^ r11;
    r6 = r6 ^ r10;
    r5 = r7 ^ r5;
    r5 = r8 ^ r5;
    tmp6 = r0 << Ox01;
    r2 = r0 & tmp6;
    tmp7 = r0 << Ox01;
    r3 = r1 & tmp7;
    tmp8 = r1 << Ox01;
    r10 = r0 & tmp8;
    tmp9 = r1 << Ox01;
    r11 = r1 & tmp9;
    r8 = r11 ^ r4;
    r8 = r10 ^ r8;
    r7 = r3 ^ r4;
    r7 = r7 ^ r2;
    tmp10 = r7 >> Ox01;
    tmpOR4 = bnot r12;
    tmpOR5 = bnot tmp10;
    r4 = tmpOR5 & tmpOR4;
    r12 = r7 << Ox07;
    tmp11 = r5 << Ox02;
    r2 = r7 & tmp11;
    tmp12 = r5 << Ox02;
    r3 = r8 & tmp12;
    tmp13 = r6 << Ox02;
    r10 = r7 & tmp13;
    tmp14 = r6 << Ox02;
    r11 = r8 & tmp14;
    r6 = r6 ^ r11;
    r6 = r6 ^ r10;
    r5 = r2 ^ r5;
    r5 = r3 ^ r5;
    tmp15 = r7 << Ox02;
    r2 = r7 & tmp15;
    tmp16 = r7 << Ox02;
    r3 = r8 & tmp16;
    tmp17 = r8 << Ox02;
    r10 = r7 & tmp17;
    tmp18 = r8 << Ox02;
    r11 = r8 & tmp18;
    r8 = r11 ^ r4;
    r8 = r10 ^ r8;
    r7 = r3 ^ r4;
    r7 = r7 ^ r2;
    tmp19 = r5 << Ox04;
    r2 = r7 & tmp19;
    tmp20 = r6 << Ox04;
    r3 = r7 & tmp20;
    tmp21 = r5 << Ox04;
    r9 = r8 & tmp21;
    tmp22 = r6 << Ox04;
    r10 = r8 & tmp22;
    r5 = r5 ^ r2;
    r6 = r6 ^ r3;
    r5 = r5 ^ r9;
    r6 = r6 ^ r10;
    tmp23 = r5 << Ox01;
    r0 = r0 ^ tmp23;
    tmp23 = r6 << Ox01;
    r1 = r1 ^ tmp23;
  }
}

