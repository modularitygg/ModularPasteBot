# -*- coding: utf-8 -*-
# !/usr/bin/env python
import discord
import json
import os
import sys

from data						import Constants, Variables
from events 					import PasteBotEvents
from subscripts					import paste_cleanup

sep = os.path.sep

def main():
	os.environ['TZ'] = 'Europe/Amsterdam'

	args = sys.argv
	if len(args) <= 1:
		print("No run argument provided.")
		return

	# Paste Bot
	if args[1] == "bot":
		Variables.pasteBotClient = discord.Client(intents=Constants.pasteBotIntents)
		PasteBotEvents.setupEvents()
		Variables.pasteBotClient.run(Constants.getPasteBotToken())
	elif args[1] == "cleanup":
		paste_cleanup.main()

	return


if __name__ == "__main__":
	main()