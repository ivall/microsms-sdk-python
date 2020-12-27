import re

from .exceptions import *


def validate_code(code):
    pattern = re.compile("^[A-Za-z0-9]{8}$")

    if not pattern.match(code):
        raise WrongCodeFormat("The code does not match with regex.")


def check_payment_status(payment_status):
    if payment_status == "E,2":
        raise NoPartnerOrService("Partner or service not found.")
    elif payment_status == "E,3":
        raise WrongSmsNumber("Sms number is not valid.")
    elif payment_status[0] == "1":
        paid = True
    else:
        paid = False
    return paid
