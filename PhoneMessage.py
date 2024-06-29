import smtplib
import sys

EMAIL = 'jupiter.am705@gmail.com'
def send_message(phn, carrier, message):
    recipient = phn+carrier
    auth = (EMAIL, PSW)
    
    server = smtplib.SMTP("smtp-mail.outlook.com", port=587)
    server.starttls()
    server.login(auth[0], auth[1])
    
    server.sendmail(auth[0], recipient, message)
    

send_message('8328089405', '@vzwpix.com', "How are you doing?")