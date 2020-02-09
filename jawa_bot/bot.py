import requests,json
import configparser as conf


class telegram_bot():
	"""Telegram Bot"""
	def __init__(self, config):
		self._token = self.read_config(config)
		self._endpoint = "https://api.telegram.org/bot{}/".format(self._token)

	def _getRequest(self,url):
		r = requests.get(url)
		return r.json()

	def _getUpdate(self, offset=None):
		url = self._endpoint + "getUpdates"
		# check if offset not None
		if offset:
			url = url +"?offset={}".format(offset)
		r = self._getRequest(url)
		if len(r["result"]) != 0:
			return r

	def _sendMessage(self, message, chat_id, reply_to):
		url = self._endpoint + "sendMessage?text={}&chat_id={}&reply_to_message_id={}".format(message, chat_id, reply_to)
		if message is not None:
			r = self._getRequest(url)

	def read_config(self, config):
		r = conf.ConfigParser()
		r.read(config)
		return r.get('credential', 'token')

	def _write_last_updated(self, file_name, data):
		f = open(file_name, "w")
		f.write(str(data))
		f.close()
		return f


		