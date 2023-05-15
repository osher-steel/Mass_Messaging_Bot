import sys
import functions
from twilio.rest import Client

# -------------------Connecting to Twilio Account and Testing Twilio number-------------------#
account_sid = input("Enter your account sid: ")
auth_token = input("Enter your auth token: ")

try:
    client = Client(account_sid, auth_token)
except Exception as e:
    sys.exit("Failed to create client" + str(e))

twilio_num = input("Enter your Twilio phone number: ")


try:  # Test message to see if twilio number is correct
    message = client.messages.create(
        body="Testing Twilio number",
        from_=twilio_num,
        to="+17864453842"
    )
except:
    sys.exit("Twilio number is invalid")

# -------------------Formatting Spreadsheet-------------------#
file = 'spreadsheet.csv'
df = functions.get_dataframe(file)

df.dropna()
df = df.filter(['Name', 'Phone'])
if df.shape[1] != 2:
    print(df.shape)
    sys.exit("File is not formatted correctly")

# -------------------Confirming User Message-------------------#
message = input("Enter the message that you want and add @ where you want the name of person to be (ex: Hello @ how "
                "are you?):\n"x)
message_tokens = message.split('@')

while len(message_tokens) > 2:
    print("Only enter @ once")
    message = input("Enter message again:\n")
    message_tokens = message.split('@')

confirm = 'a'
while confirm != 'c':
    if len(message_tokens) == 2:
        print("Message:"+message_tokens[0] + "(name)" + message_tokens[1])
    else:
        print("Message:" + message)

    confirm = input("\nPress c to confirm\n")
    if confirm != 'c':
        message = input(
            "Enter message:\n")
        message_tokens = message.split('@')

# -------------------Sending Personalized Message to Each Person-------------------#
for index, row in df.iterrows():
    row['Phone'] = functions.switch_to_international(row['Phone'])
    if row['Phone'] != 0:

        if len(message_tokens) == 2:
            personalized_message = message_tokens[0] + row['Name'] + message_tokens[1]
        else:
            personalized_message = message

        try:
            message = client.messages.create(
                body=personalized_message,
                from_=twilio_num,
                to=row['Phone']
            )
        except:
            print("Error sending message to " + row['Name'])
    else:
        print("Invalid phone number for" + row['Name'])
