# -*- coding: utf-8 -*-
#!/usr/bin/env python
from pathlib 					import Path
from glob						import glob
from datetime 					import datetime, timedelta
import discord
import shutil
import requests
import time
import os
import sys

from data						import Constants, Folders, Variables
from view						import PasteBotButtons

def setupEvents():

	@Variables.pasteBotClient.event
	async def on_ready():
		print('Initialized client as {0.user}.'.format(Variables.pasteBotClient))

		return


	@Variables.pasteBotClient.event
	async def on_message(message):
		if message.author == Variables.pasteBotClient.user:
			return

		attachments = message.attachments # []

		if len(attachments) > 0:
			for attachment in attachments:
				if not str(attachment.content_type).startswith("text"):
					continue

				size = attachment.size
				if size > 8000000:
					continue

				filename = attachment.filename
				url = attachment.url
				urlsuffix = url.split("discordapp.com/attachments/")[1]

				original_output_file_path = Folders.getPasteWebRoot() + Constants.sep + urlsuffix.replace("/", "_").replace("_" + filename, "")
				Path(original_output_file_path).mkdir(parents=True, exist_ok=True)

				original_file_request = requests.get(url)
				original_file_request.encoding = "utf-8"

				original_content = original_file_request.text

				with open(original_output_file_path + Constants.sep + filename, 'w', encoding="utf-8") as outfile:
					outfile.write(original_content)

				output = "Paste created of `" + filename + "`, uploaded by `" + message.author.display_name + "`."

				pasteView = PasteBotButtons.PasteButtons(Constants.getPasteBotUrlPrefix() + url)
				await message.channel.send(output, view=pasteView)

		return


	@Variables.pasteBotClient.event
	async def on_message_delete(message):
		if message.author == Variables.pasteBotClient.user:
			return

		attachments = message.attachments # []

		if len(attachments) > 0:
			for attachment in attachments:
				filename = attachment.filename
				url = attachment.url
				urlsuffix = url.split("discordapp.com/attachments/")[1]

				file_path = Folders.getPasteWebRoot() + Constants.sep + urlsuffix.replace("/", "_").replace("_" + filename, "") + Constants.sep + filename

				if os.path.isfile(file_path):
					os.remove(file_path)

					async for next_message in message.channel.history(limit=10, after=message):
						if next_message.author == Variables.pasteBotClient.user:
							if filename in next_message.content:
								await next_message.delete()

		return

	return