import re
import dns.resolver
import smtplib
import random
import os
from dotenv import load_dotenv
load_dotenv()

# function to check email format using regex
def check_format(email):
    pattern = r'^[a-zA-Z][a-zA-Z0-9._]*@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True
    else:
        return False

# function to check if email domain exists using MX records
def check_domain(email):
    try:
        domain = email.split("@")[1]
        records = dns.resolver.resolve(domain, "MX")
        return True
    except:
        return False

# function to send OTP for verification
def send_otp(email):

    otp = random.randint(100000,999999)
    
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    

    message = f"Subject: Email Verification OTP\n\nYour OTP is {otp}"

    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()

    try:
       server.login(sender,password)
    except smtplib.SMTPAuthenticationError:
       print("Email login failed. Check your App Password.")
       exit()
    server.sendmail(sender,email,message)

    server.quit()

    return otp


# main program

email = input("Enter your email: ")

# Step 1: format validation
if not check_format(email):
    print("Invalid Email Format")
    exit()

print("Format Valid")

# Step 2: domain validation
if not check_domain(email):
    print("Domain does not exist")
    exit()

print("Domain Verified")

# Step 3: OTP verification

otp = send_otp(email)

user_otp = int(input("Enter OTP sent to your email: "))

if user_otp == otp:
    print("Email Successfully Verified")
else:
    print("Incorrect OTP")