# Description: This is the main file for the mail bot
# Author: David
# Date: 17-apr-2023

import win32com.client
import json

config = json.load(open('config.json'))
outlook = win32com.client.Dispatch("Outlook.Application")


def send_mail(config, outlook):
    """
    Send an email using outlook
    Parameters
    ----------
    config : JSON file
        The configuration file for the email
        Must contain "to" "subject" and "body"
    outlook : win32com.client.Dispatch("Outlook.Application")
        The outlook application
    """
    olmailitem = 0x0
    newMail = outlook.CreateItem(olmailitem)
    newMail.Subject = config['subject']
    newMail.Body = config['body']
    newMail.To = config['to']
    newMail.Send()
