from email.message import EmailMessage
from purchase_operations.email_info import admin_email, password
import ssl
import smtplib
import json
customer_file = 'storage/customers.json'


def send_to_email(c_id, s_id, item_data, total):
    with open(customer_file, 'r') as f:
        temp = json.load(f)
    [open_list] = temp

    email_sender = admin_email
    email_password = password
    receiver_name = open_list[c_id]["name"]
    email_receiver = open_list[c_id]["email"]

    subject = f"Shopping Receipt {s_id}"
    body = """"""
    body += "Payment confirmed. Thank you for shopping with us!\n\n"
    body += f"Customer: {receiver_name} \n"
    for item in item_data:
        p_name = item_data[item]["product name"]
        p_quantity = item_data[item]["product quantity"]
        p_cost = item_data[item]["product cost"]
        body += f"Product: {p_name}   Quantity: {p_quantity}   Cost: {p_cost} \n"
    body += f"Total Cost: {total} Kshs"

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())



