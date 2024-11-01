import os
from dotenv import load_dotenv
import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

def send_gmail(subject, body, sender_email, receiver_email, password):
    """
    Sends an email via Gmail SMTP server.
    """
    smtp_server = os.getenv("smtp_server")
    smtp_port = os.getenv("smtp_port")
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject
 
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"{subject} email sent successfully via Gmail.")
    except Exception as e:
        print(f"Error sending Gmail email: {e}")
 
def send_water_reminder():
    email = os.getenv("sender")
    reciever =  os.getenv("receiver")
    password =  os.getenv("password")
    subject = "Reminding you for Drinkning Water"
    body = "It's time to drink water. Gulp 200ml. "
    send_gmail(subject, body, email, reciever, password)

send_water_reminder()