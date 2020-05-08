import env
import smtplib
from email.message import EmailMessage

# Create an instance of the EmailMessage() class and then configure it to our needs
email = EmailMessage()
email['from'] = 'Sunny Hebbar'
email['to'] = 'sunnyhebbar@hotmail.co.uk'
email['subject'] = 'Wassuuuuuuuupppppp!'
# Body of the email - can be anything we want (text, images, HTML, etc.)
email.set_content('Hey dude, how\'s it going?')

# Use the smtplib client to send the email
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # Initialise the server
    smtp.ehlo()
    # Encryption method to connect securely to the server
    smtp.starttls()
    # Login with credentials and send the email
    smtp.login(env.EMAIL_ADDRESS, env.EMAIL_PASSWORD)
    smtp.send_message(email)
    print('Email sent, all good!')
