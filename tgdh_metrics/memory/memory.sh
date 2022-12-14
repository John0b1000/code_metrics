#!/bin/bash

# file: memory.sh
#

# run the memory program
#
for i in {2..100}
do
    python3 mem_test.py $i
    sleep 1
done

# end file: memory.sh
