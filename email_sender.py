import env
import smtplib
from email.message import EmailMessage
# Allows us to get our index.html file and convert it to a template so we can set the variable values
from string import Template
from pathlib import Path

# Create a HTML object which is the template of the index.html - use Template and Path to get the path and read as text
html = Template(Path('index.html').read_text())

# Create an instance of the EmailMessage() class and then configure it to our needs
email = EmailMessage()
email['from'] = 'Sunny Hebbar'
email['to'] = 'sunnyhebbar@hotmail.co.uk'
email['subject'] = 'Wassuuuuuuuupppppp!'

# Body of the email - can be anything we want (text, images, HTML, etc.)
# Here, we want to set the value of the name variable in the index.html file, so we can either do this by stating
# the kwargs (name='Sunny'), or by using an object and passing in various params ({'name': 'Sunny'})
# The second set_content argument specifies that the content will be HTML
email.set_content(html.substitute(name='Sunny'), 'html')

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
