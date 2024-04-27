from colorama import init, Fore
from twilio.rest import Client
from colorama import  Style
import time , sys 
from colored import stylize , fg , attr
from flask import Flask, request, Response
# Initialize coloram
init()

def display_banner():
    banner = '''
    ||----------------------------------------------------------------------||
    ||                                                                      ||
    ||                                                                      ||
    ||         ▄████████   ▄█        ▄██████▄   ▄██████▄  ████████▄         ||           
    ||         ███    ███  ███       ███    ███ ███    ███ ███   ▀███       ||
    ||         ███    █▀   ███       ███    ███ ███    ███ ███    ███       ||
    ||        ▄███▄▄▄      ███       ███    ███ ███    ███ ███    ███       ||
    ||        ▀▀███▀▀      ███       ███    ███ ███    ███ ███    ███       ||
    ||          ███        ███       ███    ███ ███    ███ ███    ███       ||
    ||          ███        ███▌    ▄ ███    ███ ███    ███ ███   ▄███       ||
    ||          ███        █████▄▄██  ▀██████▀   ▀██████▀  ████████▀        || 
    ||                     ▀                                                || 
    ||                                                     101              ||
    ||----------------------------------------------------------------------||
    '''

    banner = Fore.MAGENTA + banner
    banner += Style.RESET_ALL

    print(banner)

display_banner()


def print_red(message):
    red_text = Fore.RED + message + Fore.RESET
    print(red_text)

# Ask the user if they want to run the code
user_input = input(Fore.RED +'<<<-----Do you want to run this TOOL?----->>> (yes/no): ' +Fore.RESET)

if user_input.lower() == 'yes':
    choice = input(Fore.RED +'<<<<-----Do you want to make a call or send an SMS?----->>>> (call/sms): ' + Fore.RESET)
    if choice.lower() == 'call':
        # Twilio Account SID and Auth Token
        account_sid = 'your acount sid here'
        auth_token = 'your account token here'

        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # URL for the call
        call_url = 'https://<your ngrok random url>ngrok.com/call'

        # Spammer's phone number
        to_number = '+<the spammers number>'

        # Twilio phone number you purchased
        from_number = '+1<the twilio phone number you purchased>'

        # Interval in seconds between calls
        INTERVAL = 10  # 10 seconds

        # Function to make the call
        def make_call():
            call = client.calls.create(
                url=call_url,
                to=to_number,
                from_=from_number
            )
            return call

        count = 0

        while True:
            try:
                call_res = make_call()
                count += 1
                print(f'Number {count}, Status: {call_res.status}')
                time.sleep(INTERVAL)
            except Exception as e:
                print(f'Error occurred: {e}')
                break

     
    #One thing to keep in mind though is that if you want to do sms flood then it has to be done new api separately


    elif choice.lower() == 'sms':
        # Twilio Account SID and Auth Token
        account_sid = 'your acount sid here'
        auth_token = 'your account token here'

        # Initialize Twilio client
        client = Client(account_sid, auth_token)

        # Spammer's phone number
        to_number = '+<the spammers number>'

        # Twilio phone number you purchased
        from_number = '+1<the twilio phone number you purchased>'

        # Function to send SMS
        def send_sms():
            message = client.messages.create(
                body='Hello. It has come to my attention that you are a scammer.',
                from_=from_number,
                to=to_number
            )
            return message

        sms_res = send_sms()
        print(f'SMS sent. Message SID: {sms_res.sid}')
else:
    print_red('Code execution canceled..................................!')
