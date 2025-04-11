# 🛡️ 3.Password Hashing and Login System 🖥️
This project provides a login system that securely checks user credentials using SHA-256 hashing. It allows users to log in using their email and password, while ensuring password security by comparing hashed values.

# 🚀 Features
🔐 Password Hashing: Stores passwords securely by hashing them using SHA-256.

📧 Email-based Login: Users log in using their email, and passwords are checked against their hashed version.

🔍 Password Verification: Passwords are compared after hashing, making the login process secure and resistant to direct password retrieval.

# 💡 Usage
# 1. Add Users:
The system stores email addresses and their hashed passwords.

When users log in, their entered password is hashed and compared to the stored hash.

# 2. Login Flow:
Input your email and password.

The system will check if the hashed version of the entered password matches the stored hash.

# 3. Sample Logins:
The following users are pre-set in the system:

example@gmail.com: "password"

code_in_placer@cip.org: "karel"

student@stanford.edu: "123!456?789"

# Example:

Login with email: example@gmail.com
Enter your password: password