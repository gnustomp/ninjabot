import requests
import urllib.parse

class Paste(object):
	def write(self, string, language='text', private=True):
		"""
		Write <string> to a new bpaste
		Returns bpaste URL or error message
		"""

		expire = '1week'

		url = 'https://bpaste.net/json/new'
		data = {
			'code': string,
			'lexer': language,
			'expiry': expire
		}

		res = requests.post(url, data=data)

		j = res.json()

		o = 'https://bpaste.net/show/{}'.format(urllib.parse.quote(j['paste_id']))

		return o


APIS = {
	# Making an instance to preserve old API
	'core.paste': Paste()
}
