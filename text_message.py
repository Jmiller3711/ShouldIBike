from twilio.rest import Client

account = "ACe5eb7cdb2facc86e91b64a939736cfb5"
token = "a132adaf13b801a30432c92f97113eb0"
my_twilio_number = '+18317776316'
myCellPhone = '+14056253791'


def text_myself(message):
    client = Client(account, token)
    client.messages.create(to=myCellPhone, from_=my_twilio_number, body=message)
