
# MaskedVerifBench: Verification of Benchmarks Composed of Masked Programs

MaskedVerifBench is a set of masked programs for the following tools: LeakageVerif [1], maskVerif [2] and QMVerif [3].
It was used in the article presenting LeakageVerif for the comparison of the different tools, which are all designed to check for leakages in symbolic expressions of masked programs.

## Benchmarks List

Description of each of the benchmark and their origin:

  * ISW AND: this is the basic ISW scheme applied for the logical AND with two shares [4].
  * P1 to P17: these are boolean C++ programs from the publicly available cryptographic software implementations [5]. We translated the C++ code to adapt it for each tool.
  * Secmult: this is the secure Galois field multiplication as described in [6]. The codes for the different tools as written directly by hand, unrolling loops when necessary.
  * SecmultSM: this is the Secmult algorithm with symbolic multiplication.
  * A2B01 and B2A01: these are arithmetic to boolean and boolean to arithmetic masking conversion programs, as presented in [7].
  * A2B14 and B2A14: these are arithmetic to boolean and boolean to arithmetic masking conversion programs, as designed in [8].
  * B2A17: this is a boolean to arithmetic masking conversion program, described in [9].
  * TI-Add, TI-Add-Opt, TI-Add-8 and TI-Add-Opt-8: the first two benchmarks are assembly programs performing the masked addition of two 32-bit masked values, given in [10]. The versions ending with '8' are 8-bit adaptations of the 32-bit programs: we made those because QMVerif only supports 8-bit variables, and cannot implement the 32-bit versions.
  * Sbox1 to Sbox8: these are different implementation of a masked SBox, based on an idea in [3]. More information can be found in [1] on each version. All versions were written using the algorithms and description given in the referenced articles.
  * AES-Herbst: this is the AES with the masking scheme described in [11], comprising the key schedule and the ten rounds.
  * AES-SM: this is a masked implementation adapted from [12]. It implements the same masking scheme as the one in [11], but with a symbolic Galois field multiplication by constants 2 and 3 in the mix-columns step, and does not mask the key schedule.
  * AES-FSE13: this is an implementation of the AES following the scheme in [13]. The code was given to us as QMVerif file by the authors of this tool. We created the LeakageVerif code from this file.
  * k3 to k254: following an idea in [3], these programs are buggy implementations of the exponentiation used in the AES.

For more informations, see [1].


## References

[1] Meunier, Q. L., Pons, E. and Heydemann, K. (2021). LeakageVerif: Scalable and Efficient Leakage Verification in Symbolic Expressions". Cryptology ePrint Archive (2021).

[2] Barthe, G., Belaïd, S., Cassiers, G., Fouque, P. A., Grégoire, B. and Standaert, F. X. (2019, September). maskverif: Automated verification of higher-order masking in presence of physical defaults. In European Symposium on Research in Computer Security (pp. 300-318). Springer, Cham.

[3] Pengfei, G., Hongyi, X., Sun, P., Zhang, J., Song, F. and Chen, T. (2020). Formal verification of masking countermeasures for arithmetic programs. IEEE Transactions on Software Engineering.

[4] Ishai, Y., Sahai, A. and Wagner, D. (2003, August). Private circuits: Securing hardware against probing attacks. In Annual International Cryptology Conference (pp. 463-481). Springer, Berlin, Heidelberg.

[5] Eldib, H., Wang, C. and Schaumont, P. (2014, April). SMT-based verification of software countermeasures against side-channel attacks. In International Conference on Tools and Algorithms for the Construction and Analysis of Systems (pp. 62-77). Springer, Berlin, Heidelberg.

[6] Rivain, M. and Prouff, E. (2010, August). Provably secure higher-order masking of AES. In International Workshop on Cryptographic Hardware and Embedded Systems (pp. 413-427). Springer, Berlin, Heidelberg.

[7] Goubin, L. (2001, May). A sound method for switching between boolean and arithmetic masking. In International Workshop on Cryptographic Hardware and Embedded Systems (pp. 3-15). Springer, Berlin, Heidelberg.

[8] Coron, J. S., Großschädl, J. and Vadnala, P. K. (2014, September). Secure conversion between boolean and arithmetic masking of any order. In International Workshop on Cryptographic Hardware and Embedded Systems (pp. 188-205). Springer, Berlin, Heidelberg.

[9] Coron, J. S. (2017, September). High-order conversion from boolean to arithmetic masking. In International Conference on Cryptographic Hardware and Embedded Systems (pp. 93-114). Springer, Cham.

[10] Jungk, B., Petri, R. and Stöttinger, M. (2018). Efficient side-channel protections of ARX ciphers. IACR Transactions on Cryptographic Hardware and Embedded Systems, 627-653.

[11] Herbst, C., Oswald, E. and Mangard, S. (2006, June). An AES smart card implementation resistant to power analysis attacks. In International conference on applied cryptography and network security (pp. 239-252). Springer, Berlin, Heidelberg.

[12] Yao, Y., Yang, M., Patrick, C., Yuce, B. and Schaumont, P. (2018, April). Fault-assisted side-channel analysis of masked implementations. In 2018 IEEE International Symposium on Hardware Oriented Security and Trust (HOST) (pp. 57-64). IEEE.

[13] Coron, J. S., Prouff, E., Rivain, M. and Roche, T. (2013, March). Higher-order side channel security and mask refreshing. In International Workshop on Fast Software Encryption (pp. 410-424). Springer, Berlin, Heidelberg.


