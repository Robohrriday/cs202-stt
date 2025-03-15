nruns=3
underscore="_"

for n in 1 auto
do
    for threads in 1 auto
    do
        for dist in no load
        do
            total_time=0
            echo "########################### n=$n, threads=$threads, dist=$dist ###########################"
            
            for i in $(seq 1 $nruns)
            do
                start_time=$(date +%s)
                python3 -m pytest tests \
                    --cov=algorithms \
                    --cov-report=html:"../cs202-stt/suiteF-results/${n}${underscore}${threads}${underscore}${dist}" \
                    -n $n --dist $dist --parallel-threads $threads
                end_time=$(date +%s)
                
                run_time=$((end_time - start_time))
                total_time=$((total_time + run_time))
                
                echo "Run $i execution time: $run_time seconds"
            done
            
            average_time=$((total_time / nruns))
            echo "Average execution time for n=$n, threads=$threads, dist=$dist: $average_time seconds"
        done
    done
done
