# cs202-stt

### Lab 6: Python Test Parallelization

Repository used: [keon/algorithms](https://github.com/keon/algorithms) <br>
Commit Analyzed: cad4754bc71742c2d6fcbd3b92ae74834d359844<br>

- suiteA - 10 sequential execs of tests (with failing+flaky tests)
    - Run `pytest_seq1.sh`
    - Terminal log in `suiteA-log.txt`
    - No flaky tests detected
    - `tests/test_array.py ..................F...F......` < Only failing test
    - Coverage: *69%*
    - Total exec time: *95s (10 repetitons)*
    - Average exec time per test run: *9.5s*
- suiteB - 5 sequential execs of tests (without failing+flaky tests)
    - Run `pytest_seq2.sh`
    - Terminal log in `suiteB-log.txt`
    - Coverage: *69%*
    - Total exec time: *49s* (5 repetitons)*
    - Average execution time of five repetitions, `Tseq`: *9.8s*
- suiteC - Parellel exec (same test suite as suiteB)
    - Run `pytest_par.sh`
    - Terminal log in `suiteC-log.txt`
