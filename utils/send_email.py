import random


def send_otp_mail():
    return str(random.randint(100000, 999999))

print(send_otp_mail())