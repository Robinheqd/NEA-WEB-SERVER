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

Create_Member_Error = False
Create_Member_Success = False

Create_Group_Error = False
Create_Group_Success = False

New_Login_Host = False
Login_Host_Email = ""

Login_Host_Error = False
Login_Host_Success = False
Login_Host_Name = ""

New_Login_Member = False
Login_Member_Email = ""

Login_Member_Error = False
Login_Member_Success = False
Login_Member_Name = ""

Host_Get_Auctions = False
Host_Get_Auctions_Email = ""
Host_Get_Auctions_Result = ""
Host_Get_Auctions_Result_Worked = False

Host_Get_Auction_Manage_Result = []
Host_Get_Auction_Manage_Worked = False

Host_Auction_Manage = False
Host_Auction_Manage_Email = ""
Host_Auction_Manage_Title = ""

Member_Get_Groups = False
Member_Get_Groups_Email = ""

Member_Get_Group_Result = ""
Member_Get_Group_Result_Worked = False

Member_Join_Group = False
Member_Join_Group_Email = ""
Member_Join_Group_Name = ""

Member_Join_Group_Success = False
Member_Join_Group_Error = False

Group_Data = False
Group_Data_Name = ""
Group_Data_Email = ""

Group_Data_Result_Worked = False
Group_Data_Result = ""

Member_Add_Funds = False
Member_Add_Funds_Email = ""
Member_Add_Funds_Name = ""
Member_Add_Funds_Amount = ""

Member_Add_Funds_Success = False
Member_Add_Funds_Result = ""

Join_Auction = False
Join_Auction_Name = ""
Join_Auction_Title = ""

Join_Auction_Success = False
Join_Auction_Error = False

Member_Load_Auction = False
Member_Load_Auction_Name = ""
Member_Load_Auction_Title = ""

Member_Load_Auction_Worked = False
Member_Load_Auction_Result = ""

Place_Bid = False
Place_Bid_Name = ""
Place_Bid_Title = ""
Place_Bid_Amount = ""

Place_Bid_Success = False
Place_Bid_Error = False

@app.route('/')
def index():
	return "Nothing to see here"

@app.route('/server')
def server():
	while True:
		time.sleep(0.001)
		global New_Group, groupUserEmail, groupName, groupDescription, groupMaxFunds, New_Auction_User, auctionMemberName, auctionMemberEmail, New_Auction_Host, auctionHostEmail, auctionHostName, New_Auction, auctionTitle, auctionDescription, auctionStartPrice, auctionLength, New_Login_Host, Login_Host_Email, New_Login_Member, Login_Member_Email, Host_Get_Auctions, Host_Get_Auctions_Email, Host_Auction_Manage, Host_Auction_Manage_Email, Host_Auction_Manage_Title, Member_Get_Groups, Member_Get_Groups_Email, Member_Join_Group, Member_Join_Group_Email, Member_Join_Group_Name, Group_Data, Group_Data_Name, Group_Data_Email, Member_Add_Funds, Member_Add_Funds_Email, Member_Add_Funds_Name, Member_Add_Funds_Amount, Join_Auction, Join_Auction_Name, Join_Auction_Title, Member_Load_Auction, Member_Load_Auction_Name, Member_Load_Auction_Title, Place_Bid, Place_Bid_Name, Place_Bid_Title, Place_Bid_Amount
		if New_Group:
			data = {
			"action": "create-group",
			"auctionMemberEmail": groupUserEmail,
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
		elif New_Login_Host:
			data = {
			"action": "host-login",
			"auctionHostEmail": Login_Host_Email
			}
			New_Login_Host = False
			return json.dumps(data)
		elif New_Login_Member:
			data = {
			"action": "member-login",
			"auctionMemberEmail": Login_Member_Email
			}
			New_Login_Member = False
			return json.dumps(data)
		elif Host_Get_Auctions:
			data = {
			"action": "get-auctions",
			"auctionHostEmail": Host_Get_Auctions_Email
			}
			Host_Get_Auctions = False
			return json.dumps(data)
		elif Host_Auction_Manage:
			data = {
			"action": "manage-auction",
			"auctionHostEmail": Host_Auction_Manage_Email,
			"auctionTitle": Host_Auction_Manage_Title
			}
			Host_Auction_Manage = False
			return json.dumps(data)
		elif Member_Get_Groups:
			data = {
			"action": "get-groups",
			"auctionMemberEmail": Member_Get_Groups_Email
			}
			Member_Get_Groups = False
			return json.dumps(data)
		elif Member_Join_Group:
			data = {
			"action": "join-group",
			"auctionMemberEmail": Member_Join_Group_Email,
			"groupName": Member_Join_Group_Name
			}
			Member_Join_Group = False
			return json.dumps(data)
		elif Group_Data:
			data = {
			"action": "group-data",
			"groupName": Group_Data_Name,
			"auctionMemberEmail": Group_Data_Email
			}
			Group_Data = False
			return json.dumps(data)
		elif Member_Add_Funds:
			data = {
			"action": "add-funds",
			"auctionMemberEmail": Member_Add_Funds_Email,
			"groupName": Member_Add_Funds_Name,
			"funds": Member_Add_Funds_Amount
			}
			Member_Add_Funds = False
			return json.dumps(data)
		elif Join_Auction:
			data = {
			"action": "join-auction",
			"groupName": Join_Auction_Name,
			"auctionTitle": Join_Auction_Title
			}
			Join_Auction = False
			return json.dumps(data)
		elif Member_Load_Auction:
			data = {
			"action": "member-load-auction",
			"groupName": Member_Load_Auction_Name,
			"auctionTitle": Member_Load_Auction_Title
			}
			Member_Load_Auction = False
			return json.dumps(data)
		elif Place_Bid:
			data = {
			"action": "place-bid",
			"groupName": Place_Bid_Name,
			"auctionTitle": Place_Bid_Title,
			"amount": Place_Bid_Amount
			}
			Place_Bid = False
			return json.dumps(data)
		return "Nothing"

@app.route("/create-group", methods=['POST'])
def group():
	global New_Group, groupUserEmail, groupName, groupDescription, groupMaxFunds
	groupUserEmail = json.loads(request.json)['Email']
	groupName = json.loads(request.json)['Name']
	groupDescription = json.loads(request.json)['Description']
	groupMaxFunds = json.loads(request.json)['Max Funds']
	New_Group = True
	return 'Done'

@app.route("/check-group")
def groupCheck():
	while True:
		time.sleep(0.001)
		global Create_Group_Error, Create_Group_Success
		if Create_Group_Error:
			Create_Group_Error = False
			return "Error"
		elif Create_Group_Success:
			Create_Group_Success = False
			return "Success"
		return "Nothing"

@app.route("/create-member", methods=['POST'])
def member():
	global New_Auction_User, auctionMemberName, auctionMemberEmail
	auctionMemberName = json.loads(request.json)['Name']
	auctionMemberEmail = json.loads(request.json)['Email']
	New_Auction_User = True
	return "Done"

@app.route("/check-member")
def memberCheck():
	while True:
		time.sleep(0.001)
		global Create_Member_Error, Create_Member_Success
		if Create_Member_Error:
			Create_Member_Error = False
			return "Error"
		elif Create_Member_Success:
			Create_Member_Success = True
			return "Success"
		return "Nothing"

@app.route("/create-host", methods=['POST'])
def host():
	global New_Auction_Host, auctionHostName, auctionHostEmail
	auctionHostName = json.loads(request.json)['Name']
	auctionHostEmail = json.loads(request.json)['Email']
	New_Auction_Host = True
	return "Done"

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

@app.route("/check-auction")
def auctionCheck():
	while True:
		time.sleep(0.001)
		global Create_Auction_Error, Create_Auction_Success
		if Create_Auction_Error:
			Create_Auction_Error = False
			return "Error"
		elif Create_Auction_Success:
			Create_Auction_Success = False
			return "Success"
		return "Nothing"

@app.route("/validate", methods=['POST'])
def validate():
	global Create_Host_Error, Create_Host_Success, Create_Auction_Error, Create_Auction_Success, Create_Member_Error, Create_Member_Success, Create_Group_Error, Create_Group_Success, Login_Host_Error, Login_Host_Success, Login_Host_Name, Login_Member_Error, Login_Member_Success, Login_Member_Name, Host_Get_Auctions_Result, Host_Get_Auctions_Result_Worked, Host_Get_Auction_Manage_Result, Host_Get_Auction_Manage_Worked, Member_Get_Group_Result, Member_Get_Group_Result_Worked, Member_Join_Group_Error, Member_Join_Group_Success, Group_Data_Result_Worked, Group_Data_Result, Member_Add_Funds_Success, Member_Add_Funds_Result, Join_Auction_Success, Join_Auction_Error, Member_Load_Auction_Worked, Member_Load_Auction_Result, Place_Bid_Success, Place_Bid_Error
	if json.loads(request.json)['Result'] == "Host-Created":
		Create_Host_Success = True
	elif json.loads(request.json)['Result'] == "Host-Exists":
		Create_Host_Error = True
	elif json.loads(request.json)['Result'] == "Auction-Created":
		Create_Auction_Success = True
	elif json.loads(request.json)['Result'] == "Auction-Exists":
		Create_Auction_Error = True
	elif json.loads(request.json)['Result'] == "Member-Created":
		Create_Member_Success = True
	elif json.loads(request.json)['Result'] == "Member-Exists":
		Create_Member_Error = True
	elif json.loads(request.json)['Result'] == "Group-Created":
		Create_Group_Success = True
	elif json.loads(request.json)['Result'] == "Group-Exists":
		Create_Group_Error = True
	elif json.loads(request.json)['Result'] == "Host-Login":
		Login_Host_Success = True
		Login_Host_Name = json.loads(request.json)['Username']
	elif json.loads(request.json)['Result']  == "Host-Invalid":
		Login_Host_Error = True
	elif json.loads(request.json)['Result'] == "Member-Login":
		Login_Member_Success = True
		Login_Member_Name = json.loads(request.json)['Username']
	elif json.loads(request.json)['Result'] == "Member-Invalid":
		Login_Member_Error = True
	elif json.loads(request.json)['Result'] == "Auctions-Found":
		Host_Get_Auctions_Result_Worked = True
		Host_Get_Auctions_Result = json.loads(request.json)['Auctions']
	elif json.loads(request.json)['Result'] == "Auction-Found":
		Host_Get_Auction_Manage_Worked = True
		Host_Get_Auction_Manage_Result = {
		"StartPrice": json.loads(request.json)['StartPrice'],
		"HighestBid": json.loads(request.json)['HighestBid'],
		"EndDate": json.loads(request.json)['EndDate'],
		"Description": json.loads(request.json)['Description']
		}
	elif json.loads(request.json)['Result'] == "Groups-Found":
		Member_Get_Group_Result_Worked = True
		Member_Get_Group_Result = json.loads(request.json)['Groups']
	elif json.loads(request.json)['Result'] == "Group-Joined":
		Member_Join_Group_Success = True
	elif json.loads(request.json)['Result'] == "Group-Invalid":
		Member_Join_Group_Error = True
	elif json.loads(request.json)['Result'] == "Group-Data":
		Group_Data_Result_Worked = True
		Group_Data_Result = json.loads(request.json)['groupData']
	elif json.loads(request.json)['Result'] == "Funds-Added":
		Member_Add_Funds_Success = True
		Member_Add_Funds_Result = json.loads(request.json)['Funds']
	elif json.loads(request.json)['Result'] == "Auction-Joined":
		Join_Auction_Success = True
	elif json.loads(request.json)['Result'] == "Auction-Not-Joined":
		Join_Auction_Error = True
	elif json.loads(request.json)['Result'] == "Member-Auction-Load":
		Member_Load_Auction_Worked = True
		Member_Load_Auction_Result = json.loads(request.json)['Auction']
	elif json.loads(request.json)['Result'] == "Bid-Placed":
		Place_Bid_Success = True
	elif json.loads(request.json)['Result'] == "Bid-Reject":
		Place_Bid_Error = True
	return "done"

@app.route("/login-host", methods=['POST'])
def hostLogin():
	global New_Login_Host, Login_Host_Email
	Login_Host_Email = json.loads(request.json)['Email']
	New_Login_Host = True
	return "Done"
	
@app.route("/check-host-login")
def hostLoginCheck():
	global Login_Host_Error, Login_Host_Success, Login_Host_Name
	if Login_Host_Error:
		Login_Host_Error = False
		return "Error"
	elif Login_Host_Success:
		Login_Host_Success = False
		return Login_Host_Name
	return "Nothing"

@app.route("/auction-list", methods=['POST'])
def hostAuctionGet():
	global Host_Get_Auctions, Host_Get_Auctions_Email
	Host_Get_Auctions = True
	Host_Get_Auctions_Email = json.loads(request.json)['Email']
	return "Done"

@app.route("/get-auction-list")
def hostAuctionReturn():
	global Host_Get_Auctions_Result, Host_Get_Auctions_Result_Worked
	if Host_Get_Auctions_Result_Worked:
		Host_Get_Auctions_Result_Worked = False
		return Host_Get_Auctions_Result
	else:
		return "Nothing"

@app.route("/group-list", methods=['POST'])
def memberGroupGet():
	global Member_Get_Groups, Member_Get_Groups_Email
	Member_Get_Groups = True
	Member_Get_Groups_Email = json.loads(request.json)['Email']
	return "Done"

@app.route("/get-group-list")
def memberGroupReturn():
	global Member_Get_Group_Result, Member_Get_Group_Result_Worked
	if Member_Get_Group_Result_Worked:
		Member_Get_Group_Result_Worked = False
		return Member_Get_Group_Result
	else:
		return "Nothing"
		
@app.route("/join-group", methods=['POST'])
def memberGroupJoin():
	global Member_Join_Group, Member_Join_Group_Email, Member_Join_Group_Name
	Member_Join_Group = True
	Member_Join_Group_Email = json.loads(request.json)['Email']
	Member_Join_Group_Name = json.loads(request.json)['Name']
	return "Done"

@app.route("/check-join-group")
def memberCheckGroupJoin():
	global Member_Join_Group_Success, Member_Join_Group_Error
	if Member_Join_Group_Success:
		Member_Join_Group_Success = False
		return "Success"
	elif Member_Join_Group_Error:
		Member_Join_Group_Error = False
		return "Error"
	return "Nothing"

@app.route("/manage-auction", methods=['POST'])
def hostAuctionManage():
	global Host_Auction_Manage, Host_Auction_Manage_Email, Host_Auction_Manage_Title
	Host_Auction_Manage = True
	Host_Auction_Manage_Email = json.loads(request.json)['Email']
	Host_Auction_Manage_Title = json.loads(request.json)['Title']
	return "Done"

@app.route("/get-manage-auction")
def hostGetAuctionManage():
	global Host_Get_Auction_Manage_Result, Host_Get_Auction_Manage_Worked
	if Host_Get_Auction_Manage_Worked:
		Host_Get_Auction_Manage_Worked = False
		return json.dumps(Host_Get_Auction_Manage_Result)
	else:
		return "Nothing"

@app.route("/login-member", methods=['POST'])
def memberLogin():
	global New_Login_Member, Login_Member_Email
	Login_Member_Email = json.loads(request.json)['Email']
	New_Login_Member = True
	return "Done"
	
@app.route("/check-member-login")
def memberLoginCheck():
	global Login_Member_Error, Login_Member_Success, Login_Member_Name
	if Login_Member_Error:
		Login_Member_Error = False
		return "Error"
	elif Login_Member_Success:
		Login_Member_Success = False
		return Login_Member_Name
	return "Nothing"

@app.route("/group-data", methods=['POST'])
def memberGroupData():
	global Group_Data, Group_Data_Name, Group_Data_Email
	Group_Data = True
	Group_Data_Name = json.loads(request.json)['groupName']
	Group_Data_Email = json.loads(request.json)['Email']
	return "Done"

@app.route("/get-group-data")
def memberGetGroupData():
	global Group_Data_Result_Worked, Group_Data_Result
	if Group_Data_Result_Worked:
		Group_Data_Result_Worked = False
		return Group_Data_Result
	else:
		return "Nothing"
	
@app.route("/add-funds", methods=['POST'])
def memberAddFunds():
	global Member_Add_Funds, Member_Add_Funds_Email, Member_Add_Funds_Name, Member_Add_Funds_Amount
	Member_Add_Funds = True
	Member_Add_Funds_Email = json.loads(request.json)['Email']
	Member_Add_Funds_Name = json.loads(request.json)['groupName']
	Member_Add_Funds_Amount = json.loads(request.json)['Funds']
	return "Done"

@app.route("/add-funds-result")
def memberAddFundsResult():
	global Member_Add_Funds_Success, Member_Add_Funds_Result
	if Member_Add_Funds_Success:
		Member_Add_Funds_Success = False
		return Member_Add_Funds_Result
	return "Nothing"

@app.route("/join-auction", methods=['POST'])
def memberJoinAuction():
	global Join_Auction, Join_Auction_Name, Join_Auction_Title
	Join_Auction = True
	Join_Auction_Name = json.loads(request.json)['groupName']
	Join_Auction_Title = json.loads(request.json)['auctionTitle']
	return "Done"

@app.route("/check-join-auction")
def memberCheckJoinAuction():
	global Join_Auction_Success, Join_Auction_Error
	if Join_Auction_Success:
		Join_Auction_Success = False
		return "Success"
	elif Join_Auction_Error:
		Join_Auction_Error = False
		return "Error"
	return "Nothing"

@app.route("/load-auction-member", methods=['POST'])
def memberLoadAuction():
	global Member_Load_Auction, Member_Load_Auction_Name, Member_Load_Auction_Title
	Member_Load_Auction = True
	Member_Load_Auction_Name = json.loads(request.json)['groupName']
	Member_Load_Auction_Title = json.loads(request.json)['Title']
	return "Done"

@app.route("/get-member-auction")
def memberGetLoadAuctin():
	global Member_Load_Auction_Worked, Member_Load_Auction_Result
	if Member_Load_Auction_Worked:
		Member_Load_Auction_Worked = False
		return Member_Load_Auction_Result
	return "Nothing"

@app.route("/place-bid", methods=['POST'])
def placeBid():
	global Place_Bid, Place_Bid_Name, Place_Bid_Title, Place_Bid_Amount
	Place_Bid = True
	Place_Bid_Name = json.loads(request.json)['groupName']
	Place_Bid_Title = json.loads(request.json)['auctionTitle']
	Place_Bid_Amount = json.loads(request.json)['Amount']
	return "Done"

@app.route("/bid-result")
def placeBidResult():
	global Place_Bid_Success, Place_Bid_Error
	if Place_Bid_Success:
		Place_Bid_Success = False
		return "Success"
	elif Place_Bid_Error:
		Place_Bid_Error = False
		return "Error"
	return "Nothing"

if __name__ == "__main__":
	app.run(debug=True, threaded=True)
