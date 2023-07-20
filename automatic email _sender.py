import os
import random
import smtplib

def message_email():
    user = input("Enter your name: ")
    email=input("Enter your mail: ")
    message = input(f"Dear {user},Welcome to the auto email AI ")
    s = smtplib.SMTP("smtp.gmiil.com",576)
    s.starttls()
    s.login("Your gmail account","Your password")
    s.sendmail("&&&&&&&&&",email,message)
    print("Email Sent")

message_email()    
