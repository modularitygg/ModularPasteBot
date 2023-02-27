# -*- coding: utf-8 -*-
#!/usr/bin/env python
import discord
import os
import sys

sep = os.path.sep

class PasteButtons(discord.ui.View):
	def __init__(self, url: str):
		super().__init__()

		self.add_item(discord.ui.Button(label='View', url=url + "&raw=false"))
		self.add_item(discord.ui.Button(label='Raw', url=url + "&raw=true"))