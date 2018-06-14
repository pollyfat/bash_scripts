#!/bin/bash

# 推整个文件夹到手机的Download目录

for i in $1/* ; do
	adb push $i /storage/emulated/0/Download/
done
