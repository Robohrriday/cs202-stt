start_time=$(date +%s)
nruns=5
for n in $(seq 1 $nruns)
do
    python3 -m pytest ./tests/ --cov=algorithms --cov-report=html:../../cs202-stt/suiteA/suiteA-results/
done

end_time=$(date +%s)
execution_time=$((end_time - start_time))

echo "Total execution time: $execution_time seconds"