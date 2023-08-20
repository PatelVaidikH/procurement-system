from django.conf import settings
from django.core.mail import EmailMessage, get_connection

def send_reset_password(email,token):  
    Subject = "Password Reset Link"
    Body = f"A request has been received to reset the password for your Comms Lodge account. Click on the link to rest your password http://127.0.0.1:8000/resetpass/{token}/. The link will remain active for next 10 mins."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = email
    with get_connection(  
        host=settings.EMAIL_HOST, 
        port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS  
    ) as connection:  
        subject = Subject  
        email_from = settings.EMAIL_HOST_USER  
        recipient_list = [email]  
        message = Body
        EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
        return True

def send_room_add(email,room_name):  

    Body = f"Hope this email finds you well. We am excited to inform you that you have been added to {room_name}. We are delighted to have you on board. Log in with your credentials to access the room"

    Subject = f"Welcome to {room_name}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    with get_connection(  
        host=settings.EMAIL_HOST, 
        port=settings.EMAIL_PORT,  
        username=settings.EMAIL_HOST_USER, 
        password=settings.EMAIL_HOST_PASSWORD, 
        use_tls=settings.EMAIL_USE_TLS  
    ) as connection:  
        subject = Subject  
        email_from = settings.EMAIL_HOST_USER  
        recipient_list = [email]  
        message = Body
        EmailMessage(subject, message, email_from, recipient_list, connection=connection).send()  
        return True
