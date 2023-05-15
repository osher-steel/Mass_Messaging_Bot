# Mass_Messaging_Bot
This repository contains two programs that each send mass sms or instagram dms using a spreadsheet
Selenium, Pandas and the Twilio library need to be installed on the user's computer. To execute the scripts place a .csv or .xlsx file titled spreadsheets in the program folder.

Spreadsheet formatting:
For mass_text_bot, there needs to be a column named 'Name' which has the list of names and a column named 'Phone' which has the corresponding phone numbers (the script automatically converts phone-numbers to international format)
For mass_dm_bot, the only change is that 'Phone' column needs to be replaced by 'Username' which has the corresponding instagram usernames
