from flask import Flask
from flask import request
from flask import Response
import requests
import json 

#get ur token using botfather
TOKEN = "<your bot token>"

app = Flask(__name__)

# Reading the JSON format when we send the text message and extracting the chat id of the user and the text that user send to the bot
def tel_parse_message(message):
	print("message-->", message)
	try:
		chat_id = message["message"]["chat"]["id"]
		txt = message["message"]["text"]
		print("chat_id-->", chat_id)
		print("txt-->", txt)

		return chat_id, txt
	except:
		print("No text found-->>")

#setting up sending text massage from a bot
def tel_send_message(chat_id, text):
	url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
	payload = {
			"chat_id" : chat_id,
			"text" : text
	}

	k = requests.post(url, json=payload)
	return k

#setting up image retrieval from a bot
def tel_send_image(chat_id):
	url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"
	payload = {
			"chat_id" : chat_id,
			"photo" : "https://telegra.ph/file/131533c0fc8d6b1ade492.jpg",
			"caption" : "This is a sample image"
	} 

	k = requests.post(url, json=payload)
	return k 

#setting up audio retrieval from a bot
def tel_send_audio(chat_id):
	url = f"https://api.telegram.org/bot{TOKEN}/sendAudio"
	payload = {
			"chat_id" : chat_id,
			"audio" : "https://od.lk/s/MzFfNDMyMzU2ODhf/sample%20music.mp3"
	}

	k = requests.post(url, json=payload)
	return k

#setting up video retrieval from a bot
def tel_send_video(chat_id):
	url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"
	payload = {
			"chat_id" : chat_id,
			"video" : "https://od.lk/s/MzFfNDMyNjQ1MzVf/production%20ID_4974883.mp4"
	}

	k = requests.post(url, json=payload)
	return k 

#setting up file retrieval from a bot
def tel_send_document(chat_id):
	url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
	payload = {
			"chat_id" : chat_id,
			"document" : "https://od.lk/s/MzFfNDMyNjg2Mzdf/RH_StudyGuide_V2.pdf"
	}

	k = requests.post(url, json=payload)
	return k 

#setting up poll retrieval from a bot
def tel_send_poll(chat_id):
	url = f"https://api.telegram.org/bot{TOKEN}/sendPoll"
	payload = {
			"chat_id" : chat_id,
			"question" : "What is the correct file extension for python files?",
			"options" : json.dumps([".pyth", ".pyt", ".py", ".pt"]),
			"is_anonymouse" : False,
			"type" : "quiz",
			"correct_option_id" : 2
	}

	k = requests.post(url, json=payload)
	return k 

#setting up button retrieval from a bot
def tel_send_button(chat_id):
	url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
	payload = {
			"chat_id" : chat_id,
			"text" : "Are you robot?",
					 "reply_markup" : {"keyboard" : [[{"text" : "Yes"}, {"text" : "No"}]]}
	}

	k = requests.post(url, json=payload)
	return k 

#setting up inline button retrieval from a bot
def tel_send_inlinebutton(chat_id):
	url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
	payload = {
			"chat_id" : chat_id,
			"text" : "Are you robot?",
			"reply_markup" : {
					"inline_keyboard" : [[
							{
								"text" : "No",
								"callback_data" : "km_No"
							},
							{
								"text" : "Yes",
								"callback_data" : "km_Yes"
							}
					]]
			}
	}

	k = requests.post(url, json=payload)
	return k 

# setting up inline button URL retrieval from a bot
def tel_send_inlineurl(chat_id):
	url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
	payload = {
			"chat_id" : chat_id,
			"text" : "Join us",
			"reply_markup" : {
					"inline_keyboard" : [
							[
								{"text" : "website", "url" : "https://hitechlk.com/"},
								{"text" : "telegram", "url" : "https://t.me/lkhitech"}
							]
					]
			}
	}

	k = requests.post(url, json=payload)
	return k

# reading the respomnse from the user and responding to it accordingly
@app.route("/", methods = ["GET", "POST"])
def index():
	if request.method == "POST":
		msg = request.get_json()
		try:
			chat_id, txt = tel_parse_message(msg)
			if txt == "hello":
				tel_send_message(chat_id, "Hello")
			elif txt == "img":
				tel_send_image(chat_id)
			elif txt == "audio":
				tel_send_audio(chat_id)
			elif txt == "video":
				tel_send_video(chat_id)
			elif txt == "doc":
				tel_send_document(chat_id)
			elif txt == "poll":
				tel_send_poll(chat_id)
			elif txt == "button":
				tel_send_button(chat_id)
			elif txt == "inbutton":
				tel_send_inlinebutton(chat_id)
			elif txt == "inlineurl":
				tel_send_inlineurl(chat_id)
			elif txt == "km_No":
				tel_send_message(chat_id, "Proceed")
			elif txt == "km_Yes":
				tel_send_message(chat_id, "Try again")
			else: 
				tel_send_message(chat_id, "Hello!, world")
		except:
			print("from index-->")

		return Response("ok", status=200)
	else:
		return "<h1>Hello!</h1>"

if __name__ == "__main__":
	app.run(threaded=True)
