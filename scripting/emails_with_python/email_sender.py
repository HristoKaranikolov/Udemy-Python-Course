import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Type the mail sender!'
email['to'] = 'Type the mail receiver!'
email['subject'] = 'You won a million dollars!'

email.set_content('I am Python dev.')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('Type your mail here!', 'Type your password here!')
    smtp.send_message(email)
    print('All good boss!')
