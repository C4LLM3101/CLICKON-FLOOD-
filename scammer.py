from colorama import init, Fore
from twilio.rest import Client
import time , sys 
import pyfiglet
import colored
from colored import stylize , fg , attr

# Initialize colorama
init()

# Generate ASCII art
bannar= """

  ███████▓    ▒█████  ▒█████ ▓█████▄ 
▓██   ▓██▒   ▒██▒  ██▒██▒  ██▒██▀ ██▌
▒████ ▒██░   ▒██░  ██▒██░  ██░██   █▌
░▓█▒  ▒██░   ▒██   ██▒██   ██░▓█▄   ▌
░▒█░  ░██████░ ████▓▒░ ████▓▒░▒████▓ 
 ▒ ░  ░ ▒░▓  ░ ▒░▒░▒░░ ▒░▒░▒░ ▒▒▓  ▒ 
 ░    ░ ░ ▒  ░ ░ ▒ ▒░  ░ ▒ ▒░ ░ ▒  ▒ 
 ░ ░    ░ ░  ░ ░ ░ ▒ ░ ░ ░ ▒  ░ ░  ░ 
          ░  ░   ░ ░     ░ ░    ░    
                              ░      

                       created by :- 101                         
"""
def merry():
	bannar_color = colored.fg("orange_red_1") + colored.attr("bold")
	for i in bannar:
		time.sleep(0.00000000000001)
		sys.stdout.write(stylize(i, bannar_color))
		sys.stdout.flush()
#ascii_art = pyfiglet.figlet_format(ascii_text)

#print(ascii_art)

# Ask the user if they want to run the code
user_input = input('Do you want to run this code? ...............>>--(yes/no): ')

if user_input.lower() == 'yes':
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
else:
    print('Code execution canceled.')
