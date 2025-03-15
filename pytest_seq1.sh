start_time=$(date +%s)
nruns=10
for n in {1..nruns}
do
    python3 -m pytest tests --cov=algorithms --cov-report=html:../cs202-stt/suiteD-results/
done

end_time=$(date +%s)
execution_time=$((end_time - start_time))

echo "Total execution time: $execution_time seconds"