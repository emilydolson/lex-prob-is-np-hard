# Calculating Lexicase Selection Probabilities is NP-Hard

[![preprint](https://img.shields.io/badge/preprint-arXiv:2301.06724-brightgreen)](https://arxiv.org/abs/2301.06724)
[![paper](https://img.shields.io/badge/published%20in-GECCO%2023-yellow)](https://dl.acm.org/doi/10.1145/3583131.3590356)
[![Code](https://github.com/emilydolson/lex-prob-is-np-hard/actions/workflows/python-app.yml/badge.svg)](https://github.com/emilydolson/lex-prob-is-np-hard/actions/workflows/python-app.yml)
[![Code DOI](https://zenodo.org/badge/630644309.svg)](https://zenodo.org/badge/latestdoi/630644309)

This repository contains scripts that implement the reductions (from Satisfiability to epsilon-lexicase and from epsilon-lexicase to lexicase) used in the paper "Calculating Lexicase Selection Probabilities is NP-Hard" to prove that these problems are all NP-Hard. Brute-force code to calculate lexicase and epsilon lexicase selection probabilities is in the [EC Ecology Toolbox](https://github.com/emilydolson/ec_ecology_toolbox).

![Example reduction from Satisfiability to Epsilon Lexicase Selection](paper/figs/SAT_to_eps_example.png)

## Abstract

Lexicase selection is a state-of-the-art parent selection algorithm in evolutionary computation.
Recently, there have been efforts to develop stronger theoretical analyses of lexicase selection.
Many of these analyses hinge on calculating the probability of an individual solution being selected under lexicase selection. Discovering a fast way to perform this calculation would be very helpful to the development of theory regarding lexicase selection, and  would also have implications for efforts to develop practical improvements to lexicase selection. Here, I prove that this problem of calculating selection probabilities under lexicase selection, which I name lex-prob, is NP-Hard. I achieve this proof by reducing SAT, a well-known NP-Complete problem, to lex-prob in polynomial time. This reduction involves an intermediate step in which a popular variant of lexicase selection, epsilon-lexicase selection, is reduced to standard lexicase selection. This result also has deeper theoretical implications about the relationship between epsilon-lexicase selection and lexicase selection and the relationship between lex-prob and other NP-Hard problems. Finally, I present a highly-optimized brute-force algorithm (and accompanying open-source implementation) for performing these calculations. While the worst-case time complexity of this solution is, of course, exponential it is capable of solving realistically-sized instances of the problem in approximately one second.

## Repository Contents

- [paper](/paper): contains all latex code for the paper
- [scripts](/scripts): contains relevant python scripts
  - benchmark.py: For benchmarking optimized brute force algorithm
  - reduce_sat_to_eps.py: Implements reduction from SAT to epsilon lexicase selection
  - reduce_eps_to_lex.py: Implements reduction fo epsilon lexicase selection to lexicase selection.

## Author

- [Emily Dolson](https://emilyldolson.com)
