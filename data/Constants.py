# -*- coding: utf-8 -*-
#!/usr/bin/env python
import discord
import os

sep = os.path.sep

pasteBotIntents = discord.Intents.default()
pasteBotIntents.message_content = True

isDevEnvironment = not os.getcwd().startswith(sep)

def getPasteBotUrlPrefix():
	if isDevEnvironment:
		return "http://localhost/paste?content="
	return "https://paste.modularity.gg/paste?content="

def getPasteBotToken():
	if isDevEnvironment:
		return os.environ.get('ModularDevBotToken')
	return os.environ.get('ModularPasteBotToken')