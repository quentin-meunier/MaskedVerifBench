(* File B2A01.ec *)
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
    (* # Boolean To Arthimetic for x # *)
	gamma = $distr;
	T = x_0 ^ gamma;
	T = T - gamma;
	T = T ^ x_0;
	gamma = gamma ^ x_1;
	x_0 = x_0 ^ gamma;
	x_0 = x_0 - gamma;
	x_0 = x_0 ^ T;
  }
}

