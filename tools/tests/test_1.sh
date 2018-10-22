#!/bin/bash

python ./yaml_to_md.py tests/data/ tests/test_temp.md

diff tests/test_temp.md tests/test_1.md 1> /dev/null
if [ $? -eq 0 ];
then
	echo "Good"
else
	echo "Bad"
fi
