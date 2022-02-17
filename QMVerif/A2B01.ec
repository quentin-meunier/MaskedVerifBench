(* File A2B01.ec *)
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

    gamma = $distr;
    T = gamma + gamma;
    y_0 = gamma ^ x_1;
    omega = gamma & y_0;
    y_0 = T ^ x_0;
    gamma = gamma ^ y_0;
    gamma = gamma & x_1;
    omega = omega ^ gamma;
    gamma = T & x_0;
    omega = omega ^ gamma;
    gamma = T & x_1;
    gamma = gamma ^ omega;
    T = T & x_0;
    gamma = gamma ^ T;
    T = gamma + gamma;
    gamma = T & x_1;
    gamma = gamma ^ omega;
    T = T & x_0;
    gamma = gamma ^ T;
    T = gamma + gamma;
    gamma = T & x_1;
    gamma = gamma ^ omega;
    T = T & x_0;
    gamma = gamma ^ T;
    T = gamma + gamma;
    gamma = T & x_1;
    gamma = gamma ^ omega;
    T = T & x_0;
    gamma = gamma ^ T;
    T = gamma + gamma;
    gamma = T & x_1;
    gamma = gamma ^ omega;
    T = T & x_0;
    gamma = gamma ^ T;
    T = gamma + gamma;
    gamma = T & x_1;
    gamma = gamma ^ omega;
    T = T & x_0;
    gamma = gamma ^ T;
    T = gamma + gamma;
    gamma = T & x_1;
    gamma = gamma ^ omega;
    T = T & x_0;
    gamma = gamma ^ T;
    T = gamma + gamma;
    y_0 = y_0 ^ T;
    y_1 = x_1;
  }    
}

