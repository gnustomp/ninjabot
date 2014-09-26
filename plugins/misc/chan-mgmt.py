# Channel management plugin. Bot must be operator in the channels you wish to manage.

class Plugin(object):
	def load(self, bot, config):
		self.bot = bot
	
	def trigger_kick(self, msg):
		"Kicks nicks from channels. RFC-style format. When used in a channel message, channel to kick from is that channel."
		if not self.bot.is_admin(msg.nick):
			return

		if msg.type != 1:
			# If message is not received from a channel, use RFC-style syntax.
			if len(msg.args) < 2:
				self.bot.notice(msg.nick, "There must be at least one channel parameter and one user parameter")
				return
			channels = msg.args.pop(0).split(",")
			nicks = msg.args.pop(0).split(",")
			if len(channels) > 1:
				if len(channels) != len(nicks):
					self.bot.notice(msg.nick, "If there are multiple channel parameters, there must be as many user parameters")
					return
			comment = ""
			if msg.args:
				print(msg.args)
				comment = " ".join(msg.args)
			self.bot.irc_send("KICK {0} {1} :{2}".format(",".join(channels), ",".join(nicks), comment))

		else:
			# If the message is received from a channel, omit the channel.
			nicks = msg.args.pop(0)
			comment = ""
			if msg.args:
				comment = " ".join(msg.args)

			self.bot.irc_send("KICK {0} {1} :{2}".format(msg.channel, nicks, comment))

	def trigger_mode(self, msg):
		"Sets modes on a channel"
		if not self.bot.is_admin(msg.nick):
			return

		channel = msg.args.pop(0)
		modes = ' '.join(msg.args)
		self.bot.irc_send("MODE {0} {1}".format(channel, modes))

