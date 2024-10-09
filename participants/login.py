from participants import qrcode,send_email,create

def login(name,email,ph_no):

    create.insert(name, email, ph_no)

    # --------------------------------------------------- generating QR
    id = create.find_id()
    qrcode.generate_QR(id)

    # --------------------------------------------------- sending email
    to_add = create.find_email(id)
    send_email.sendingemail(to_add)