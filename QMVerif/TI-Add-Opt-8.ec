(* File TI-Add-Opt-8.ec *)
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
    r11 = tmpOR1 & tmpOR0;
    r12 = r0 << Ox07;
    tmp1 = bnot r3;
    tmpOR2 = bnot r0;
    tmpOR3 = bnot tmp1;
    r4 = tmpOR3 & tmpOR2;
    r6 = r2 & r0;
    tmp2 = bnot r3;
    tmpOR4 = bnot r1;
    tmpOR5 = bnot tmp2;
    r5 = tmpOR5 & tmpOR4;
    r7 = r2 & r1;
    r5 = r7 ^ r5;
    r4 = r6 ^ r4;
    r2 = r2 ^ r0;
    r3 = r1 ^ r3;
    r5 = r5 ^ r11;
    r4 = r11 ^ r4;
    tmp2 = r4 << Ox01;
    r8 = r3 & tmp2;
    tmp3 = r4 << Ox01;
    r9 = r2 & tmp3;
    r4 = r9 ^ r4;
    r4 = r8 ^ r4;
    tmp4 = r5 << Ox01;
    r10 = r3 & tmp4;
    tmp5 = r5 << Ox01;
    r11 = r2 & tmp5;
    r5 = r10 ^ r5;
    r5 = r11 ^ r5;
    tmp5 = r3 << Ox01;
    tmp6 = bnot tmp5;
    tmpOR6 = bnot r3;
    tmpOR7 = bnot tmp6;
    r8 = tmpOR7 & tmpOR6;
    tmp7 = r2 << Ox01;
    r10 = r3 & tmp7;
    tmp8 = r3 << Ox01;
    tmp9 = bnot tmp8;
    tmpOR8 = bnot r2;
    tmpOR9 = bnot tmp9;
    r9 = tmpOR9 & tmpOR8;
    tmp10 = r2 << Ox01;
    r11 = r2 & tmp10;
    r7 = r10 ^ r8;
    r6 = r9 ^ r11;
    tmp11 = r4 << Ox02;
    r8 = r7 & tmp11;
    tmp12 = r4 << Ox02;
    r9 = r6 & tmp12;
    r4 = r9 ^ r4;
    r4 = r8 ^ r4;
    tmp13 = r5 << Ox02;
    r10 = r7 & tmp13;
    tmp14 = r5 << Ox02;
    r11 = r6 & tmp14;
    r5 = r10 ^ r5;
    r5 = r11 ^ r5;
    tmp15 = r7 << Ox02;
    tmp16 = bnot tmp15;
    tmpOR10 = bnot r7;
    tmpOR11 = bnot tmp16;
    r8 = tmpOR11 & tmpOR10;
    tmp17 = r6 << Ox02;
    r10 = r7 & tmp17;
    tmp18 = r7 << Ox02;
    tmp19 = bnot tmp18;
    tmpOR12 = bnot r6;
    tmpOR13 = bnot tmp19;
    r9 = tmpOR13 & tmpOR12;
    tmp21 = r6 << Ox02;
    r11 = r6 & tmp21;
    r7 = r10 ^ r8;
    r6 = r9 ^ r11;
    tmp22 = r4 << Ox04;
    r9 = r7 & tmp22;
    tmp23 = r4 << Ox04;
    r8 = r6 & tmp23;
    r4 = r9 ^ r4;
    r4 = r8 ^ r4;
    tmp24 = r5 << Ox04;
    r11 = r7 & tmp24;
    tmp25 = r5 << Ox04;
    r10 = r6 & tmp25;
    r5 = r11 ^ r5;
    r5 = r10 ^ r5;
    tmp26 = r4 << Ox01;
    r0 = r2 ^ tmp26;
    tmp27 = r5 << Ox01;
    r1 = r3 ^ tmp27;
  }
}

