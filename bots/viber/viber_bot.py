import json
import os

import requests

# # data={
# # 		"url":        "https://8754-178-36-10-40.eu.ngrok.io",
# # 		"auth_token": "4f88462e4fb2aba1-1e7d4b58ff9485ae-2cda7320cb96f082",
# # 		"status":         0,
# # 		"status_message": "ok",
# #
# # 		}
#
# # aa=requests.post(url='https://chatapi.viber.com/pa/get_account_info', data=json.dumps(data))
#
# deta_to_send={
#     "auth_token":"4f88462e4fb2aba1-1e7d4b58ff9485ae-2cda7320cb96f082",
#     "from": "cr1rb1fsJglYP5Scd0kpAw==",
#     "type": "text",
#     "text": "Хейка!"
# }
#
# aa1=requests.post(url='https://chatapi.viber.com/pa/post', data=json.dumps(deta_to_send), headers=headers)
# a=5
class ViberSender():
	def __init__(self, server_url, auth_token):
		self.auth_token=auth_token
		self.superadmins=self.get_superadmins(server_url)
		self.headers={'Content-Type':'application/json'}
		a=5


	def send_text_message(self, message):
		data_to_send = {
			"auth_token": self.auth_token, #"4f88462e4fb2aba1-1e7d4b58ff9485ae-2cda7320cb96f082",
			"from":       self.superadmins[0]['id'], #"cr1rb1fsJglYP5Scd0kpAw==",
			"type":       "text",
			"text":       message
			}

		requests.post(url='https://chatapi.viber.com/pa/post', data=json.dumps(data_to_send), headers=self.headers)

	def send_picture(self, message, file_name):
		data_to_send = {
			"auth_token": self.auth_token, #"4f88462e4fb2aba1-1e7d4b58ff9485ae-2cda7320cb96f082",
			"from":       self.superadmins[0]['id'], #"cr1rb1fsJglYP5Scd0kpAw==",
			"type":       "picture",
			"text":       message,
			"media": 		file_name
			# "media": 		file_name #os.path.join(os.getcwd(), 'media', file_name),
			}
		aa=requests.post(url='https://chatapi.viber.com/pa/post', data=json.dumps(data_to_send), headers=self.headers)
		print(aa.content)
		print(file_name)
		a=5


	def get_superadmins(self, server_url):
		data={
				"url":        server_url, #"https://8754-178-36-10-40.eu.ngrok.io",
				"auth_token": self.auth_token, #"4f88462e4fb2aba1-1e7d4b58ff9485ae-2cda7320cb96f082",
				"status":         0,
				"status_message": "ok",

				}

		result=requests.post(url='https://chatapi.viber.com/pa/get_account_info', data=json.dumps(data))
		res_json=json.loads(result.content)
		superadmins=[x for x in res_json['members'] if x['role']=='superadmin']
		return superadmins if superadmins else []

viber_sender=ViberSender(server_url='https://0c6f-178-36-10-40.eu.ngrok.io',
						auth_token='4f88462e4fb2aba1-1e7d4b58ff9485ae-2cda7320cb96f082',
						 )


def main():
	# viber_sender.send_text_message('Йоу__')
	viber_sender.send_picture('Йоу__','test')

if __name__ == "__main__":
	main()