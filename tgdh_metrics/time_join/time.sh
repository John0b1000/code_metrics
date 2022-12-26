#!/bin/bash

# file: time.sh
#

# run the time program
#
for i in {2..100}
do
    python3 time_test.py $i
    sleep 1
done

# end file: time.sh

