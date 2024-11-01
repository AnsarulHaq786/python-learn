import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_gmail(subject, body, sender_email, receiver_email, password):
    """
    Sends an email via a local SMTP server.
    """
    smtp_server = "localhost"
    smtp_port = 587

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print(f"{subject} email sent successfully via local SMTP.")
    except Exception as e:
        print(f"this is our exception: {e}")