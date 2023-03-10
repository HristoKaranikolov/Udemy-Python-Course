import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()

email['from'] = 'Type the mail sender!'
email['to'] = 'Type the mail receiver!'
email['subject'] = 'You won a million dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Type your mail here!', 'Type your password here!')
    smtp.send_message(email)
    print('All good boss!')
