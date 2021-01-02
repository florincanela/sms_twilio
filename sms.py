from twilio.rest import Client 
from sys import	argv


receiver = argv[1]

with open('sms_body.txt', 'r') as s:
	sms_body = s.read()
 
account_sid = #sid 
auth_token = #auth token 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(
   							  from_=#twilio number,
                              body=sms_body,      
                              to=receiver 
                          ) 
 
print(f"Message sent to {receiver}")
