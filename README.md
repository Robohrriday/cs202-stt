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

### Raw Results:

| n    | threads | dist | run | time (s) |
|------|---------|------|-----|----------|
| 1    | 1       | no   | 1   | 14       |
| 1    | 1       | no   | 2   | 9        |
| 1    | 1       | no   | 3   | 10       |
| 1    | 1       | load | 1   | 11       |
| 1    | 1       | load | 2   | 10       |
| 1    | 1       | load | 3   | 10       |
| 1    | auto    | no   | 1   | 424      |
| 1    | auto    | no   | 2   | 430      |
| 1    | auto    | no   | 3   | 426      |
| 1    | auto    | load | 1   | 428      |
| 1    | auto    | load | 2   | 428      |
| 1    | auto    | load | 3   | 430      |
| auto | 1       | no   | 1   | 8        |
| auto | 1       | no   | 2   | 7        |
| auto | 1       | no   | 3   | 6        |
| auto | 1       | load | 1   | 8        |
| auto | 1       | load | 2   | 7        |
| auto | 1       | load | 3   | 7        |
| auto | auto    | no   | 1   | 196      |
| auto | auto    | no   | 2   | 196      |
| auto | auto    | no   | 3   | 201      |
| auto | auto    | load | 1   | 198      |
| auto | auto    | load | 2   | 196      |
| auto | auto    | load | 2   | 200      |


### Average Time Per Configuration

<!-- The table below shows the average time per configuration, calculated by averaging the times across all runs for each configuration: -->

| n    | threads | dist | avg time (s) |
|------|---------|------|--------------|
| 1    | 1       | no   | 11.0         |
| 1    | 1       | load | 10.3         |
| 1    | auto    | no   | 426.7        |
| 1    | auto    | load | 428.7        |
| auto | 1       | no   | 7.0          |
| auto | 1       | load | 7.3          |
| auto | auto    | no   | 197.7        |
| auto | auto    | load | 198.0        |

### Speedup

<!-- The table below shows the speedup of the parallel execution over the sequential execution (`Tseq = 9.8s`) for each configuration: -->

| n    | threads | dist | speedup |
|------|---------|------|---------|
| 1    | 1       | no   | 0.89    |
| 1    | 1       | load | 0.95    |
| 1    | auto    | no   | 0.02    |
| 1    | auto    | load | 0.02    |
| auto | 1       | no   | 1.40    |
| auto | 1       | load | 1.34    |
| auto | auto    | no   | 0.05    |
| auto | auto    | load | 0.05    |

### Combined Results

| configuration | average execution time (s)  | speedup (wrt seq)  | workers | failing tests | flaky tests |
|---------------|-----------------------------|--------------------|---------|---------------|-------------|
| 1-1-no        | 11.0                        | 0.89               | 1       | 0             | 0           |
| 1-1-load      | 10.3                        | 0.95               | 1       | 0             | 0           |
| 1-auto-no     | 426.7                       | 0.02               | 1       | 3             | 0           |
| 1-auto-load   | 428.7                       | 0.02               | 1       | 3             | 0           |
| auto-1-no     | 7.0                         | 1.40               | 6       | 0             | 0           |
| auto-1-load   | 7.3                         | 1.34               | 6       | 0             | 0           |
| auto-auto-no  | 197.7                       | 0.05               | 6       | 4             | 1           |
| auto-auto-load| 198.0                       | 0.05               | 6       | 4             | 1           |

Failing Tests Detected:
- test_heap.py::TestBinaryHeap::test_insert
- tests/test_heap.py::TestBinaryHeap::test_remove_min
- tests/test_linkedlist.py::TestSuite::test_is_palindrome
- tests/test_compression.py::TestHuffmanCoding::test_huffman_coding

Flaky Tets Detected:
- tests/test_compress.py::TestHuffmanCoding::test_huffman_coding
