export PYNGUIN_DANGER_AWARE=x
PYNGUIN_DANGER_AWARE=x

python3 -m pytest ./tests/ --cov=algorithms --cov-report=html:../../cs202-stt/suiteA/suiteA-results/

pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.stack.remove_min
pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.strings.first_unique_char
pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.backtrack.palindrome_partitioning
pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.strings.domain_extractor
pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.arrays.limit
pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.sort.insertion_sort
pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.strings.count_binary_substring
pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.arrays.remove_duplicates
pynguin --project-path . --output-path ../../cs202-stt/suiteB/tests --module-name algorithms.dp.longest_increasing --maximum_search_time 30


# post-processing
sed -i "s|import algorithms.arrays.limit as module_0|import algorithms.arrays as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_arrays_limit.py"
sed -i "s|import algorithms.stack.remove_min as module_0|import algorithms.stack as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_stack_remove_min.py"
sed -i "s|import algorithms.strings.first_unique_char as module_0|import algorithms.strings as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_strings_first_unique_char.py"
sed -i "s|import algorithms.backtrack.palindrome_partitioning as module_0|import algorithms.backtrack as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_backtrack_palindrome_partitioning.py"
sed -i "s|import algorithms.strings.domain_extractor as module_0|import algorithms.strings as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_strings_domain_extractor.py"
sed -i "s|import algorithms.sort.insertion_sort as module_0|import algorithms.sort as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_sort_insertion_sort.py"
sed -i "s|import algorithms.strings.count_binary_substring as module_0|import algorithms.strings as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_strings_count_binary_substring.py"
sed -i "s|import algorithms.arrays.remove_duplicates as module_0|import algorithms.arrays as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_arrays_remove_duplicates.py"
sed -i "s|import algorithms.dp.longest_increasing as module_0|import algorithms.dp as module_0|" "../../cs202-stt/suiteB/tests/test_algorithms_dp_longest_increasing.py"

python3 -m pytest ../../cs202-stt/suiteB/tests/ --cov=algorithms --cov-report=html:../../cs202-stt/suiteB/suiteB-results/
