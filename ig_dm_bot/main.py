import random
import sys
import time
import getpass

from ig_functions import auth, send_message, get_dataframe

file = 'spreadsheet.csv'
df = get_dataframe(file)

df.dropna()
df = df.filter(['Name', 'Username'])
if df.shape[1] != 2:
    print(df.shape)
    sys.exit("File is not formatted correctly")

message = input("Enter the message that you want and add @ where you want the name of person to be (ex: Hello @ how "
                "are you?):\n")
message_tokens = message.split('@')

while len(message_tokens) > 2:
    print("Only enter @ once")
    message = input("Enter message again:\n")
    message_tokens = message.split('@')

confirm = 'a'
while confirm != 'c':
    if len(message_tokens) == 2:
        print("Message:" + message_tokens[0] + "(name)" + message_tokens[1])
    else:
        print("Message:" + message)

    confirm = input("\nPress c to confirm\n")
    if confirm != 'c':
        message = input(
            "Enter message:\n")
        message_tokens = message.split('@')

my_username = 'osher_steel'
my_password = getpass.getpass('Enter your password:')

auth(my_username, my_password)
time.sleep(random.randrange(5, 10))
send_message(df, message_tokens)
