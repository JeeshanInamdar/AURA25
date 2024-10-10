import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from_add="jeeshaninamdar7@gmail.com"
key="Apna banake ke use karoo"

def sendingemail(to_add):
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # Sorting the sender email address
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = "QR Code"

    # body of email
    body = "<h1>Your QR Code for Aura 2025</h1>"

    # attach body with the msg insatnce
    msg.attach(MIMEText(body, 'html'))

    # open file to send
    f = "image1.png"
    attachment = open(f, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded from
    p.set_payload(attachment.read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', f'attachment; filename={f}')

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # Create SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_add, key)

    # Convert the multipart msg into a string
    text = msg.as_string()

    server.sendmail(from_add, to_add, text)

    server.quit()


#print("Email sent successfully!")