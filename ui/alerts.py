import smtplib
from email.mime.text import MIMEText


def send_email_alert(subject: str, body: str, to_email: str, from_email: str, smtp_server: str, smtp_port: int, username: str, password: str):
    """
    Send an email alert using SMTP.
    """
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = from_email
        msg["To"] = to_email

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)
    except Exception as e:
        print(f"Failed to send email: {e}")


# TODO: Add Telegram Bot alerts (via Bot API)