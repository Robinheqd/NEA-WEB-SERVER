from flask import Flask, request
import json
import time

app = Flask(__name__)

New_Group = False
groupUserEmail = ""
groupName = ""
groupDescription = ""
groupMaxFunds = 0

New_Auction_User = False
auctionMemberName = ""
auctionMemberEmail = ""

New_Auction_Host = False
auctionHostName = ""
auctionHostEmail = ""

New_Auction = False
cauctionHostEmail = ""
auctionTitle = ""
auctionDescription = ""
auctionStartPrice = 0
auctionLength = 0

Create_Host_Error = False

Create_Host_Success = False

Create_Auction_Error = False

Create_Auction_Success = False

@app.route('/')
def index():
	return "Nothing to see here"

@app.route('/server')
def server():
	while True:
		time.sleep(0.001)
		global New_Group, groupName, groupDescription, groupMaxFunds, New_Auction_User, auctionMemberName, auctionMemberEmail, New_Auction_Host, auctionHostEmail, auctionHostName, New_Auction, auctionTitle, auctionDescription, auctionStartPrice, auctionLength
		if New_Group:
			data = {
			"action": "create-group",
			"groupName": groupName,
			"groupDescription": groupDescription,
			"groupMaxFundsPerUser": groupMaxFunds
			}
			New_Group = False
			return json.dumps(data)
		elif New_Auction_User:
			data = {
			"action": "create-member",
			"auctionMemberName": auctionMemberName,
			"auctionMemberEmail": auctionMemberEmail
			}
			New_Auction_User = False
			return json.dumps(data)
		elif New_Auction_Host:
			data = {
			"action": "create-host",
			"auctionHostName": auctionHostName,
			"auctionHostEmail": auctionHostEmail
			}
			New_Auction_Host = False
			return json.dumps(data)
		elif New_Auction:
			data = {
			"action": "create-auction",
			"auctionHostEmail": cauctionHostEmail,
			"auctionTitle": auctionTitle,
			"auctionDescription": auctionDescription,
			"auctionStartPrice": auctionStartPrice,
			"auctionLength": auctionLength
			}
			New_Auction = False
			return json.dumps(data)
		return "Nothing"

@app.route("/check-host")
def hostCheck():
	while True:
		time.sleep(0.001)
		global Create_Host_Error, Create_Host_Success
		if Create_Host_Success:
			Create_Host_Success = False
			return "Success"
		elif Create_Host_Error:
			Create_Host_Error = False
			return "Error"
		return "Nothing"

@app.route("/check-auction")
def auctionCheck():
	while True:
		time.sleep(0.001)
		global Create_Auction_Error, Create_Auction_Success
		if Create_Auction_Error:
			Create_Auction_Error = False
			return "Success"
		elif Create_Auction_Success:
			Create_Auction_Success = False
			return "Error"
		return "Nothing"

@app.route("/create-group", methods=['POST'])
def group():
	global New_Group, groupName, groupDescription, groupMaxFunds
	groupName = json.loads(request.json)['Name']
	groupDescription = json.loads(request.json)['Description']
	groupMaxFunds = json.loads(request.json)['Max Funds']
	New_Group = True
	return 'Done'

@app.route("/create-member", methods=['POST'])
def member():
	global New_Auction_User, auctionMemberName, auctionMemberEmail
	auctionMemberName = json.loads(request.json)['Name']
	auctionMemberEmail = json.loads(request.json)['Email']
	New_Auction_User = True
	return "Done"

@app.route("/create-host", methods=['POST'])
def host():
	global New_Auction_Host, auctionHostName, auctionHostEmail
	auctionHostName = json.loads(request.json)['Name']
	auctionHostEmail = json.loads(request.json)['Email']
	New_Auction_Host = True
	return "Done"

@app.route("/create-auction", methods=['POST'])
def auction():
	global New_Auction, cauctionHostEmail, auctionTitle, auctionDescription, auctionStartPrice, auctionLength
	cauctionHostEmail = json.loads(request.json)['Email']
	auctionTitle = json.loads(request.json)['Title']
	auctionDescription = json.loads(request.json)['Description']
	auctionStartPrice = json.loads(request.json)['Price']
	auctionLength = json.loads(request.json)['Length']
	New_Auction = True
	return "Done"

@app.route("/validate", methods=['POST'])
def validate():
	global Create_Host_Error, Create_Host_Success, Create_Auction_Error, Create_Auction_Success
	if json.loads(request.json)['Result'] == "Host-Created":
		Create_Host_Success = True
	elif json.loads(request.json)['Result'] == "Host-Exists":
		Create_Host_Error = True
	elif json.loads(request.json)['Result'] == "Auction-Created":
		Create_Auction_Success = True
	elif json.loads(request.json)['Result'] == "Auction-Exists":
		Create_Auction_Error = True
	return "done"

if __name__ == "__main__":
	app.run(debug=True, threaded=True)
