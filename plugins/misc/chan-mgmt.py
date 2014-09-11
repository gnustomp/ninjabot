class Plugin(object):
	def load(self, bot, config):
		self.bot = bot
	
	def trigger_rkick(self, msg):
		if not self.bot.is_admin(msg.nick):
			return

		if len(msg.args) < 2:
			self.bot.notice(msg.nick, "u dun goofd")
			return
		channels = msg.args.pop(0).split(",")
		nicks = msg.args.pop(0).split(",")
		if len(channels) > 1:
			if len(channels) != len(nicks):
				self.bot.notice(msg.nick, "must equal no")
				return
		comment = ""
		if msg.args:
			print(msg.args)
			comment = " ".join(msg.args)
		self.bot.irc_send("KICK {0} {1} :{2}".format(",".join(channels), ",".join(nicks), comment))

	def trigger_kick(self, msg):
		if msg.type != 1:
			self.bot.notice(msg.nick, "kick must be used in a channel. Use rkick otherwise")
			return

		if not self.bot.is_admin(msg.nick):
			return

		nicks = msg.args.pop(0)
		comment = ""
		if msg.args:
			comment = " ".join(msg.args)

		self.bot.irc_send("KICK {0} {1} :{2}".format(msg.channel, nicks, comment))

	def trigger_mode(self, msg):
		if not self.bot.is_admin(msg.nick):
			return

		if len(msg.args) < 2:
			channel = msg.channel
		else:
			channel = ' '.join(msg.args)
		if len(channel.split(",")) > 1:
			self.bot.notice(msg.nick, "Can only specify one channel")
			return

		modes = msg.args.pop(0)
		self.bot.irc_send("MODE {0} {1}".format(channel, modes))

