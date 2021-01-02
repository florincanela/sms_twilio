from twilio.rest import Client 
from sys import	argv


receiver = argv[1]

with open('sms_body.txt', 'r') as s:
	sms_body = s.read()
 
account_sid = 'AC77607503b9681527a34b003573dc3cf6' 
auth_token = '3181d5fdf3028d57151d1c38ada00291' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(
   							  from_='+12566854801',
                              body=sms_body,      
                              to=receiver 
                          ) 
 
print(f"Message sent to {receiver}")
