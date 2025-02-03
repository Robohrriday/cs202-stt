#!/bin/bash

#pre-clean and setup
echo "performing pre-clean and setup..."
rm -rf temp
rm -rf $1_results
rm -f *.xml *.dot
mkdir $1_results
python3 getCommitsInfo.py $1
python3 analyzeDiffs.py $1
rm -rf $1


