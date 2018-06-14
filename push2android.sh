#!/bin/bash

for i in $1/* ; do
	adb push $i /storage/emulated/0/Download/
done
