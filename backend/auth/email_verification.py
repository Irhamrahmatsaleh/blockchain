import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

SMTP_EMAIL = os.getenv("SMTP_EMAIL")
SMTP_APP_PASSWORD = os.getenv("SMTP_APP_PASSWORD")

def send_verification_email(to_email: str, verification_link: str):
    subject = "Verify your Neutron (NTR) Account"
    body = f"Click the link below to verify your account:\n\n{verification_link}"

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = SMTP_EMAIL
    message["To"] = to_email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(SMTP_EMAIL, SMTP_APP_PASSWORD)
            server.send_message(message)
            print(f"✅ Verification email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        raise
