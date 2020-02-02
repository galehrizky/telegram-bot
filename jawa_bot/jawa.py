import requests,warnings,json
from requests.packages.urllib3.exceptions import InsecureRequestWarning

class jawa_koe():
	"""docstring for jawa_koe"""
	def __init__(self):
		self.base = "https://mongosilakan.net/api/v1/translate/translate"

	def _conver_indo_to_jawa(self,text):
		url = self.base
		payloads = {
			'from' : 'id-ID',
			'to' : 'jv-NG',
			'source' : text
		   }
		warnings.simplefilter('ignore',InsecureRequestWarning)
		r = requests.post(url=url, data=payloads, verify=False).json()

		if r is not None:
			return r["content"]["model"]["basic"]
