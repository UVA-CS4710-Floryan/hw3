#!/bin/bash
FILES=[a-z][a-z][a-z][0-9]*.py
for a in $FILES
do
	for b in $FILES
	do
		aUserId=${a%%.*}
		bUserId=${b%%.*}

		python negotiator_framework.py $aUserId $bUserId sample_scenario.csv
	done
done
