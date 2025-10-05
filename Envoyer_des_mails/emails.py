import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

config_email = "louise.marie.lom@gmail.com"
config_password = "wkrj xbpy hwmf zlwl"
config_server = "smtp.gmail.com"
config_server_port = 587

def envoyers_emails(email_destinataire, sujet, message):

    multipart_message = MIMEMultipart()
    multipart_message["Subject"] = sujet
    multipart_message["From"] = config_email
    multipart_message["To"] = email_destinataire

    multipart_message.attach(MIMEText(message, "plain"))

    serveur_mail = smtplib.SMTP(config_server, config_server_port)
    serveur_mail.starttls()
    serveur_mail.login(config_email, config_password)
    serveur_mail.sendmail(config_email, email_destinataire, multipart_message.as_string()) 
    serveur_mail.quit()


message_email = """Bonjour Draken!

Comment allez-vous?

Merci
"""

envoyers_emails("andriniaina.2am@gmail.com", "Mail depuis python", message_email)