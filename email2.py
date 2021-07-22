import smtplib
sender_email = "botpythontest123@gmail.com"
rec_email = input("input the email you want to send it to\n")
password = input("type down your password\n")
automated = input("would you like to type down your own message? if so, type down (y). however, if you'd like to send an automated test message, type (n)\n")
message = "test test 123"
if automated == "y":
    own_message = input("type down your message\n")
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, rec_email, own_message)

elif automated == "n":
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, rec_email, message,)
