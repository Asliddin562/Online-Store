import random

def generate_otp():
    return str(random.randint(100000, 999999))

def to_clean_phone(phone):
    if phone.startswith("+"):
        phone = phone[1:]
    return phone