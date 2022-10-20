# POINT OF SALE SYSTEM
## TABLE OF CONTENTS
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Navigation](#navigation)
- [Requirements](#requirements)
- [Installation Guide](#installation-guide)
***
## Technologies Used
- [Python 3.10](https://www.python.org/downloads/release/python-3108/)
- [Pycharm IDE](https://www.jetbrains.com/pycharm/)
- [Json](https://www.json.org/json-en.html)
- [Gmail](https://www.google.com/gmail/about/)
***
## Features
The application has variety of features, here a user can create, update, delete and read customer, and product details. The user can also record the products that the customer wants to buy, and prints a receipt after the customer has paid the total cost of the products.
***
## Navigation
When the user runs the application, he will be taken to the main menu. Here, they will be able to navigate through the program using the menu choices that have been listed in front of them until they do the task that they wish to complete
***
## Requirements
To run this application, the user needs to have python3 installed in their system. They can download it [here](https://www.python.org/).\
You will also need to have a Gmail account to send the emails to customers. You can register [here](https://www.google.com/intl/en-GB/gmail/about/)
***
## Installation Guide
To install this program, you first need to download the program files from the repository using the command below in your command line:
```bash
git clone https://github.com/GabrielMcryu/pos-system
```
You'll first need to access the email_info.py file to add your email address and app password:
```bash
cd pos-system/purchase_operations
```
You'll need to modify the email_info.py file with a text editor. Replace the empty string of admin_email with your email and password with your app password.\
To get your app password, you'll need to access your Google account settings, security tab [here](https://myaccount.google.com/security) and generate an app password. Use that app password to replace the empty string of password:
```python
admin_email = ''
password = ''
```
The next step is to go back to the main directory of the application:
```bash
cd ..
```
Finally, you can run the program using this command:
```python
python3 main.py
```

