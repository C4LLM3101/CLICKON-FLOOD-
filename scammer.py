from colorama import init 
from colorama import Fore, Style
from twilio.rest import Client
import time , sys 
import pyfiglet
import colored
from colored import stylize , fg , attr

# Initialize colorama

init()

def display_banner(): 
    banner = "                                                          █████████╗     ██████╗ ██████╗██████╗     \n"
    banner += "                                                         ██╔════██║    ██╔═══████╔═══████╔══██╗    \n"
    banner += "                                                         █████╗ ██║    ██║   ████║   ████║  ██║    \n"
    banner += "                                                         ██╔══╝ ██║    ██║   ████║   ████║  ██║    \n"
    banner += "                                                         ██║    ███████╚██████╔╚██████╔██████╔╝   \n" 
    banner += "                                                         ╚═╝    ╚══════╝╚═════╝ ╚═════╝╚═════╝   \n "
    banner += "                                                            created by 101\n"       

    banner = Fore.RED + banner  # Set the color to dark red
    banner += Style.RESET_ALL  # Reset the color to default after the banner

    print(banner)

display_banner()
user_input = input('Do you want to run this TOOL? ...............>>--(yes/no): ')

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
