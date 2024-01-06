from flask import Flask, request
import json

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

@app.route('/')
def index():
	return "Nothing to see here"

@app.route('/server')
def server():
	while True:
		time.sleep(0.1)
		if New_Group:
			data = {
			"action": "create-group",
			"groupName": groupName,
			"groupDescription": groupDescription,
			"groupMaxFundsPerUser": groupMaxFunds
			}
			
			return json.dumps(data)
		elif New_Auction_User:
			data = {
			"action": "create-member",
			"auctionMemberName": auctionMemberName,
			"auctionMemberEmail": auctionMemberEmail
			}
			
			return json.dumps(data)
		elif New_Auction_Host:
			data = {
			"action": "create-host",
			"auctionHostName": auctionHostName,
			"auctionHostEmail": auctionHostEmail
			}
			
			return json.dumps(data)
		elif New_Auction:
			data = {
			"action": "create-auction",
			"auctionName": auctionName,
			"auctionDescription": auctionDescription,
			"auctionStartPrice": auctionStart,
			"auctionLength": auctionLength
			}
			return json.dumps(data)

@app.route("/create-group", methods=['POST'])
def group():
	groupName = request.json['Name']
	groupDescription = request.json['Description']
	groupMaxFunds = request.json['Max Funds']
	New_Group = True
	return True

if __name__ == "__main__":
	app.run(debug=True, threaded=True)
