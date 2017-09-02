Pyvobar
=====
A python app that automates billing for a private bar system
works with a google sheet and Gmail.
Tested with python 3.5 but should work with all versions of python3

#### Setting it up
* To get integration with your google sheet follow [this tutorial](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html?utm_source=youtube&utm_medium=video&utm_campaign=youtube_python_google_sheets).
Basically, you have to add a credentials.json to your project directory and share the sheet with Google API email address. 
Make sure to change the file name at main.py line 32
* E-mail works with Oauth2 and configures your email at first run. You only have to change the email address at mail.py line 28
