from fbchat import Client, log
from fbchat.models import *
import json

class Bot(Client):
    def onMessage(self, mid, author_id, message, message_object, thread_id, thread_type, ts, metadata, msg):
        if author_id != self.uid:
            print(message)
            if message == "hi":
                self.send(Message(text="Hello Nerfe"), thread_id=thread_id, thread_type=thread_type)

def login_with_cookies():
    try:
        with open('cookies.json', 'r') as file:
            session_cookies = json.load(file)
        client = Bot('', '', session_cookies=session_cookies)
        return client
    except:
        return None

def login_with_email_password():
    print("Enter Your Facebook Credentials\n")
    email = input("Email: ")
    password = input("Password: ")
    client = Bot(email, password)
    if client.isLoggedIn():
        with open('cookies.json', 'w') as file:
            json.dump(client.getSession(), file,indent=4)
        return client
    else:
        return None

def login():
    client = login_with_cookies()
    if client is None:
        client = login_with_email_password()
    return client

client = login()
if client is not None:
    log.info("Login Successfully...")
    client.listen()
else:
    print("Login failed.")
