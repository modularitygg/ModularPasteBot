# -*- coding: utf-8 -*-
# !/usr/bin/env python
from glob						import glob
from datetime 					import datetime, timedelta
from pathlib 					import Path
import shutil
import json
import os

from data						import Constants, Folders

sep = os.path.sep

def main():
	os.environ['TZ'] = 'Europe/Amsterdam'

	now = datetime.now()
	for folder in glob(Folders.getPasteWebRoot() + Constants.sep + "*" + Constants.sep):
		date = datetime.fromtimestamp(os.stat(folder).st_mtime)
		if (now - date).days > 7:
			shutil.rmtree(folder)

	return


if __name__ == "__main__":
	main()