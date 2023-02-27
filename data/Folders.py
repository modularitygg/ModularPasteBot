# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys

from data						import Constants

def getPasteWebRoot():
	web_root_folder = os.environ.get('WebRootFolder')
	if Constants.isDevEnvironment:
		return web_root_folder + Constants.sep + "cdn.modularity.gg" + Constants.sep + "public_html" + Constants.sep + "paste"
	return web_root_folder + Constants.sep + "cdn.modularity.gg" + Constants.sep + "paste"