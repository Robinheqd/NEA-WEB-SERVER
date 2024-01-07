from flask import Flask, request
import json
import time

app = Flask(__name__)

New_Group = False
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
auctionName = ""
auctionDescription = ""
auctionStartPrice = 0
auctionLength = 0

Create_Host_Error = False

Create_Host_Success = False

@app.route('/')
def index():
	return "Nothing to see here"

@app.route('/server')
def server():
	while True:
		time.sleep(0.001)
		global New_Group, groupName, groupDescription, groupMaxFunds, New_Auction_User, auctionMemberName, auctionMemberEmail, New_Auction_Host, auctionHostEmail, auctionHostName, New_Auction, auctionName, auctionDescription, auctionStartPrice, auctionLength
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
			"auctionName": auctionName,
			"auctionDescription": auctionDescription,
			"auctionStartPrice": auctionStart,
			"auctionLength": auctionLength
			}
			New_Auction = False
			return json.dumps(data)
		return "Nothing"

@app.route("/check-host")
def hostCheck():
	While True:
		time.sleep(0.001)
		global Create_Host_Error, errorHostEmail, Create_Host_Success, successHostEmail
		if Create_Host_Success:
			return "Success"
		elif Create_Host_Error:
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

@app.route("/create-host", methods=['POST'])
def validate():
	global Create_Host_Error, errorHostEmail, Create_Host_Success, successHostEmail
	if json.loads(request.json)['Result'] == "Host-Created":
		Create_Host_Success = True
	elif json.loads(request.json)['Result'] == "Host-Exists":
		Create_Host_Error = True
	return "done"

if __name__ == "__main__":
	app.run(debug=True, threaded=True)
