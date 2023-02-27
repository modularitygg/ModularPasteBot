# -*- coding: utf-8 -*-
#!/usr/bin/env python
from datetime 					import datetime
from pytz 						import timezone
import string
import re
import os
import sys

def getCurTime(notime=False, divide=False):
	timetz = datetime.now(timezone('Europe/Amsterdam'))
	if notime:
		return timetz.strftime("%Y%m%d")
	if divide:
		return timetz.strftime("%Y%m%d_%H%M%S")
	return timetz.strftime("%Y%m%d%H%M%S")

def naturalsort(l):
	convert = lambda text: int(text) if text.isdigit() else text.lower()
	alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
	return sorted(l, key = alphanum_key)