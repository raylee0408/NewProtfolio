import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "nzexcel007@gmail.com"
    password = "xlqa sycg qmuu ccxp"
    receiver = "raylee598@gmail.com"
    context = ssl.create_default_context()


    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

# if __name__ == "__main__":
#     send_email("Subject: Test\n\nThis is a test email from Python.")

