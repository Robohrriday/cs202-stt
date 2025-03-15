nruns=3
nreps=5
s=0
for rep in $(seq 1 $nreps)
do
    start_time=$(date +%s)
    for n in $(seq 1 $nruns)
    do
        python3 -m pytest tests --cov=algorithms --cov-report=html:../cs202-stt/suiteE-results/
    done
    end_time=$(date +%s)
    execution_time=$((end_time - start_time))
    s=$((s+execution_time))

    echo "Total execution time: $execution_time seconds"
done
avg=$(echo "scale=2; $s / $nreps" | bc)
echo "Average execution time: $avg seconds"