#Make sure you register for Twilio API and select WhatsApp with python

from twilio.rest import Client 
import requests
from bs4 import BeautifulSoup


url = 'https://www.hltv.org'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
result = requests.get(url, headers=headers)

src = result.content
soup = BeautifulSoup(src, 'lxml')

news = (soup.find(lambda tag: tag.name == 'div' and 
                                   tag.get('class') == ['newstext']))

time = (soup.find(lambda tag: tag.name == 'div' and 
                                   tag.get('class') == ['newsrecent']))

account_sid = '' #enter your account_sid
auth_token = '' #enter your authorization token
client = Client(account_sid, auth_token) 
to_number = '' #enter To number which is registered on Twilio
from_number = '' #enter from number from Twilio API

message = client.messages.create( 
                              from_='whatsapp:+{}'.format(from_number),  
                              body='HLTV Latest Post! \n\n{} \n\n- Posted {}'.format(news.text, time.text),      
                              to='whatsapp:+{}'.format(to_number) 
) 
 
print("Message sent!")
