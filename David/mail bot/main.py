# Description: This is the main file for the mail bot
# Author: David
# Date: 17-apr-2023

import win32com.client
import json


class Outlook():
    def __init__(self):
        self.unread = None
        self.outlook = win32com.client.Dispatch("Outlook.Application")
        self.MAPI = self.outlook.GetNamespace("MAPI")
        self.config = json.load(open('config.json'))

    def send(self, subject=None, body=None, to=None):
        olmailitem = 0x0
        newMail = self.outlook.CreateItem(olmailitem)
        newMail.Subject = subject if subject is not None else self.config['subject']
        newMail.Body = body if body is not None else self.config['body']
        newMail.To = to if to is not None else self.config['to']
        newMail.Send()

    def get_unread(self):
        return [
            mail
            for mail in self.outlook.GetNamespace("MAPI")
            .Folders[0]
            .Folders[1]
            .Items
            if mail.UnRead
        ]

    def load_unread(self):
        unread = self.get_unread()
        mails = [[mail.Subject, mail.Body, mail.SenderEmailAddress] for mail in unread]
        self.unread = mails


a = Outlook()
a.load_unread()
