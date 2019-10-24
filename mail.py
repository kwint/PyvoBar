from __future__ import print_function
import httplib2
import os
from email.mime.text import MIMEText

import base64
import textwriter

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/gmail-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/gmail.compose'
CLIENT_SECRET_FILE = 'credentials_mail.json'
APPLICATION_NAME = 'Pivobar'
sendadress = "pivobar@demohicanen.nl"
subject = "Barupdate!"


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """

    credential_path = 'gmail-python-quickstart.json'

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials


def init():
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)
    print("Mail succesfully initialized")
    return service


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text, 'html')

    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    # raw = base64.urlsafe_b64encode(message.as_bytes())
    # raw = raw.decode
    string = message.as_string()
    raw = base64.urlsafe_b64encode(string.encode('UTF-8')).decode('ascii')
    return {'raw': raw}


def send_message(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """

    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print('Message Id: %s' % message['id'])
    return message


def main(service, data):
    """Shows basic usage of the Gmail API.

    Creates a Gmail API service object and outputs a list of label names
    of the user's Gmail account.
    """
    html = textwriter.make(data)
    message = create_message(sendadress, str(data[1]), subject, html)
    send = send_message(service, "me", message)
    print(send)
    print("done")




