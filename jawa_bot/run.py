import sys,os.path,time
from bot import telegram_bot
from jawa import jawa_koe

bot = telegram_bot("config.conf")
belekok = jawa_koe()


def handleCommands(text):
	if text == str("Hello") or text == str("hello") or text == str("/hello") or text == str("/start"):
		message = "Hallo Saya JawaBot Sebuah Bot Translate dari bahasa indonesia ke bahasa jawa, Selamat mencoba"
	else:
		message = belekok._conver_indo_to_jawa(text)
	return message

def main():
	updated_id = 0
	if os.path.isfile("last_update_on"):
		with open("last_update_on", "r") as value:
			for x in value:
				updated_id = x

	r = bot._getUpdate(offset=updated_id)
	if r is not None:
		for x in r["result"]:
			chat_id = x["message"]["chat"]["id"]
			reply_to = x["message"]["message_id"]
			last_update_id = x["update_id"] +1 
			text = x["message"]["text"]
		print(text)
		message = handleCommands(text)
		bot._sendMessage(message, chat_id, reply_to)
		bot._write_last_updated("last_update_on", last_update_id)

		print(message)
	print(updated_id)


if __name__ == '__main__':
	while True:
		try:
			time.sleep(2)
			main()
		except KeyboardInterrupt as e:
			print("[-] Bot Sleeping !!!")
			sys.exit()

