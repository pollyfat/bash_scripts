#!/usr/bin/env python  
#encoding: utf-8

# 过滤掉除字母和.号外的所有字符, 并且把大写改成小写

import re
import sys
import os
reload(sys)  
sys.setdefaultencoding('utf8') 

pattern = u'[^a-zA-z\.]'
for i in os.listdir(sys.argv[1]):
	os.rename(sys.argv[1]+i, sys.argv[1]+re.sub(pattern,'', i).lower())
