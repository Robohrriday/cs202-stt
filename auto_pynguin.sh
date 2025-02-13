pynguin --project-path . --output-path ../suiteB/tests --module-name algorithms.stack.remove_min --create-coverage-report True --report-dir ../suiteB/reports
pynguin --project-path . --output-path ../suiteB/tests --module-name algorithms.strings.first_unique_char --create-coverage-report True --report-dir ../suiteB/reports
pynguin --project-path . --output-path ../suiteB/tests --module-name algorithms.backtrack.palindrome_partitioning --create-coverage-report True --report-dir ../suiteB/reports
pynguin --project-path . --output-path ../suiteB/tests --module-name algorithms.strings.domain_extractor --create-coverage-report True --report-dir ../suiteB/reports
pynguin --project-path . --output-path ../suiteB/tests --module-name algorithms.arrays.limit --create-coverage-report True --report-dir ../suiteB/reports
# --maximum_search_time 30


# post-processing
sed -i "s|import algorithms.arrays.limit as module_0|import algorithms.arrays as module_0|" "../suiteB/tests/test_algorithms_arrays_limit.py"
sed -i "s|import algorithms.stack.remove_min as module_0|import algorithms.stack as module_0|" "../suiteB/tests/test_algorithms_stack_remove_min.py"
sed -i "s|import algorithms.strings.first_unique_char as module_0|import algorithms.strings as module_0|" "../suiteB/tests/test_algorithms_strings_first_unique_char.py"
sed -i "s|import algorithms.backtrack.palindrome_partitioning as module_0|import algorithms.backtrack as module_0|" "../suiteB/tests/test_algorithms_backtrack_palindrome_partitioning.py"
sed -i "s|import algorithms.strings.domain_extractor as module_0|import algorithms.strings as module_0|" "../suiteB/tests/test_algorithms_strings_domain_extractor.py"


python3 -m pytest ../suiteB/tests/ --cov=algorithms --cov-report=html:../../cs202-stt/suiteB-results/
