import email.utils
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$'
    return bool(re.match(pattern, email))

n = int(input().strip())
for _ in range(n):
    name, email_address = email.utils.parseaddr(input().strip())
    if is_valid_email(email_address):
        print(f"{name} <{email_address}>")