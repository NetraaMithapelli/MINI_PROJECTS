# **Smart Email Validator**

A Python-based email validation system that performs multiple levels of verification to ensure that an email address is structurally correct, belongs to a real domain, and can be verified using an OTP.
This project demonstrates practical validation techniques commonly used in real-world applications such as signup systems, authentication platforms, and secure communication services.

## Features

1)**Email Format Validation** : 
  Uses Regular Expressions (Regex) to verify correct email syntax.

2)**Domain Verification** : 
  Checks whether the email domain actually exists using DNS MX record lookup.

3)**OTP Email Verification** : 
  Sends a One-Time Password (OTP) to the provided email to confirm ownership.

4)**Security with Environment Variables** : 
  Sensitive credentials such as the sender email password are stored in a `.env` file and excluded from version control using `.gitignore`.

## Technologies Used

* Python
* `re` (Regular Expressions)
* `dns.resolver` (Domain verification)
* `smtplib` (Email sending via SMTP)
* `random` (OTP generation)

## Example Workflow
1. User enters an email address.
2. Program validates the email format.
3. The domain is checked using DNS records.
4. An OTP is sent to the email.
5. User enters OTP to confirm verification.

---

This project is part of the **MINI_PROJECTS** repository created for practicing real-world programming concepts.
