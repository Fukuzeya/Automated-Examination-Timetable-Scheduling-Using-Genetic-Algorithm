from twilio.rest import Client


#function to send messages
def send_sms(phone_number,message):
    account_sid = 'AC40bfd1c96e6190d3ee0c5edef6863942'
    auth_token = '3b482973c1ea8aceb12fd2b019b266ec'
    client = Client(account_sid, auth_token)
    client.messages.create(
    body= message,
    from_='+13512137638',
    to = f"{phone_number}",
    )
    print(message.sid)


#recover code #RKHhiqpGhNuH8GR2KHVLyztIuHI-977ej9Bu37Ex