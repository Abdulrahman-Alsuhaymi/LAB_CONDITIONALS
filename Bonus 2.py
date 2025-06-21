name = input("Please enter your name: ")
email = input("Please enter your email: ")

if len(name) <= 2:
    print("the name length must be more than 2 characters, please provide a valid name. ")
elif "gmail.com" in email and email.endswith("gmail.com") and email.index("@") > 0:
    print(f"welcome {name}, you registered with the email {email}")
else:
    print("the email is not valid , please provide a valid email.")