import random
import string
from typing import Dict, Any


def get_random_email(prefix="", length=1):
    letters = string.ascii_lowercase
    return prefix + "".join(random.choice(letters) for i in range(length)) + "@testmail.com"


def generate_user_data(user_name="test_123") -> dict:

    user_data = {
        "name": user_name,
        "email": get_random_email(user_name, 5),
        "password": "passw0rd",
        "day": "15",
        "month": "5",
        "year": "1991",
        "first_name": "John",
        "last_name": "Doe",
        "company": "Kantorka",
        "address1": "315 Whiskey rd.",
        "country": "Canada",
        "state": "Ontario",
        "city": "Ottawa",
        "zip_code": "K2W 1C8",
        "phone": "1234567890",
    }

    return user_data
