#!/usr/bin/bash
lasttime=1535148000

while true
do
	/home/dzvinka/anaconda3/bin/python update_data.py $lasttime
	python2.7 align_sentences.py
	lasttime=date+%s
	sleep 1d
done
