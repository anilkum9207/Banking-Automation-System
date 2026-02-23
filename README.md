🏦 **R&T Banking & Finance Application**

Developed by: Anil Kumar
Tech Stack: Python | Tkinter | SQLite | Pillow

**Project Overview**

R&T Banking & Finance is a desktop-based banking management system built using Python (Tkinter) and SQLite.

The application enables both Admin and Users to manage accounts, perform transactions, and securely access account information using CAPTCHA verification and email-based OTP authentication.

**Features**
**Admin**

Create new user accounts

Delete accounts with OTP verification

View account details

Secure admin login

**User**

Secure login with account number, password, and captcha

Update profile and upload profile picture

Deposit and withdraw money

Transfer funds between accounts

View transaction history

Check account details

**Installation**

**Clone the repository**:

git clone <repository-url>

**Install dependencies**:

pip install pillow

**Run the application:**

python main.py

**Database Structure**

###  Accounts Table

| Column Name      | Data Type | Description |
|------------------|----------|------------|
| account_number   | INTEGER (Primary Key) | Unique account ID |
| name             | TEXT     | Account holder name |
| mobile           | TEXT     | Mobile number |
| email            | TEXT     | Email address |
| address          | TEXT     | Full address |
| gender           | TEXT     | Gender |
| account_type     | TEXT     | Savings / Current |
| balance          | FLOAT    | Account balance |
| aadhar_number    | TEXT     | Aadhar number |
| pan_number       | TEXT     | PAN number |
| pincode          | TEXT     | Area pincode |
| IFSC             | TEXT     | Bank IFSC code |
| password         | TEXT     | Login password |

---

###  Account_Statements Table

| Column Name     | Data Type | Description |
|----------------|----------|------------|
| account_number | INTEGER  | Linked account number |
| amount         | FLOAT    | Transaction amount |
| type           | TEXT     | Deposit / Withdraw / Transfer |
| date_time      | TEXT     | Transaction timestamp |
| balance        | FLOAT    | Balance after transaction |
| txn_id         | TEXT     | Unique transaction ID |

 **Screenshots**

Add screenshots inside a folder named images/ and display them like this:

![Login Screen](images/login_screen.png)
<img width="1000" height="550" alt="image" src="https://github.com/user-attachments/assets/07c26f07-7209-4856-a181-4d32e435a96d" />

![User Dashboard](images/user_dashboard.png)
<img width="1000" height="550" alt="image" src="https://github.com/user-attachments/assets/742981c8-c78a-420d-90c7-6e8e425064ad" />


![Admin Dashboard](images/admin_dashboard.png)
<img width="1000" height="550" alt="image" src="https://github.com/user-attachments/assets/bb34e819-8c8e-435e-b408-d9562358cbf1" />


**Libraries Used**

Tkinter – GUI

SQLite3 – Database

Pillow – Image processing

Random & String – OTP & Captcha

OS & Time – File & timestamp handling

👤 Author

Anil Kumar
📍 New Delhi, India
📧 Anil.kum9207@gmail.com
