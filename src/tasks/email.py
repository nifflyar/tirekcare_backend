import asyncio
from email.message import EmailMessage
import aiosmtplib


from src.utils.celery_app import celery_app



admin_email = "nff@gmail.com"

@celery_app.task
def send_verification_code(email: str):
    async def send_email():
        message = EmailMessage()
        message["From"] = admin_email
        message["To"] = email
        message["Subject"] = "Verification code"
        message.set_content("Your code is 1234")

        await aiosmtplib.send(message, 
                            sender=admin_email,
                            recipients=[email],
                            hostname="localhost", 
                            port=1025)
        
    asyncio.run(send_email())
    return f"Email sent to {email}"