class Plugin:
	def __init__(self, controller):
		self.c = controller

	def trigger_help(self, msg):
		"Usage: help [trigger]. Lists avaliable triggers. If trigger is specified, will print help for that trigger (if avaliable)."

		prefix = self.c.plugins.prefix
		if len(msg.args) == 0:
			self.c.notice(msg.nick, 'Avaliable triggers:')
			self.c.notice(msg.nick, prefix+(', '+prefix).join(sorted(self.c.plugins.triggers.keys())))
			self.c.notice(msg.nick, 'For further info, type '+prefix+'help <trigger>')
		else:
			if msg.args[0].lstrip(prefix) in self.c.plugins.triggers:
				doc = self.c.plugins.triggers[msg.args[0].lstrip(prefix)].__doc__
				if doc:
					self.c.notice(msg.nick, doc)
				else:
					self.non_existant_help(msg)
			else:
				self.non_existant_help(msg)

	def non_existant_help(self, msg):
		self.c.notice(msg.nick, "Either that trigger does not exist, or it has no documentation.")
		

