# cs202-stt

### Lab 6: Python Test Parallelization

Repository used: [keon/algorithms](https://github.com/keon/algorithms) <br>
Commit Analyzed: cad4754bc71742c2d6fcbd3b92ae74834d359844<br>

- suiteD - 10 sequential execs of tests (with failing+flaky tests)
    - Run `pytest_seq1.sh`
    - Terminal log in `suiteD-log.txt`
    - No flaky tests detected
    - `tests/test_array.py ..................F...F......` < Only failing test
    - Coverage: *70%*
    - Total exec time: *108s (10 repetitons)*
    - Average exec time per test run: *10.8s*
- suiteE - 3 sequential execs of tests repeated 5 times (without failing+flaky tests)
    - Run `pytest_seq2.sh`
    - Terminal log in `suiteE-log.txt`
    - Coverage: *70%*
    - Total exec time: *154s (5 repetitons of 3 sequential test runs)*
    - Average execution time of five repetitions, `Tseq`: *30.80s*
- suiteF - 
