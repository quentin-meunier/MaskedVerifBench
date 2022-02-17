(* File Secmult.ec *)
(*                                                                                       *)
(* Copyright (C) 2021, Sorbonne Universite, LIP6                                         *)
(* This file is part of the MaskedVerifBench project, under the GPL v3.0 license         *)
(* See https://www.gnu.org/licenses/gpl-3.0.en.html for license information              *)
(* SPDX-License-Identifier: GPL-3.0-only                                                 *)
(* Author(s): Etienne Pons                                                               *)

op Ox00 byte;
op Ox01 byte;
op Ox07 byte;
op Ox1b byte;
op Ox80 byte;

module M = {
  proc main(a b) = {

    (* # Sharing a in 2 shares # *)
    a_0 = $distr;
    a_1 = a ^ a_0;
    (* # Sharing b in 2 shares # *)
    b_0 = $distr;
    b_1 = b ^ b_0;

    m01 = $distr;
    
    (* ############################### *)
    p = Ox00;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    tmp0 = p;

    e0 = m01 ^ tmp0;
    
    (* ############################### *)
    p = Ox00;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e1 = p;

    m10 = e0 ^ e1;
    
    (* ############################### *)
    p = Ox00;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    e0 = b_0 >> Ox01;
    b_0 = e0;
    
    e0 = b_0 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_0;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_0 << Ox01;
    e1 = a_0 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_0 = e4;
    c0 = p;

    c0 = c0 ^ m01;
    
    (* ############################### *)
    p = Ox00;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    e0 = b_1 >> Ox01;
    b_1 = e0;
    
    e0 = b_1 & Ox01;
    e1 = e0 << Ox07;
    e2 = e1 >> Ox07;
    e3 = e2 & a_1;
    e4 = e3 ^ p;
    p = e4;
    e0 = a_1 << Ox01;
    e1 = a_1 & Ox80;
    e2 = e1 >> Ox07;
    e3 = e2 & Ox1b;
    e4 = e0 ^ e3;
    a_1 = e4;
    c1 = p;

    c1 = c1 ^ m10;
  }
}

