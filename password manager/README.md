# Py-projects
# 🔐 Password Manager using Cryptography

This is a simple command-line Password Manager written in Python that uses the `cryptography` library's **Fernet** encryption to securely store and retrieve passwords.

## 📌 Features

- Store account passwords securely in a local file
- Encrypt passwords using symmetric encryption (Fernet)
- View stored passwords (automatically decrypts them)
- Easy-to-use menu-driven interface

## 🚀 How It Works

- A secret key (`key.key`) is generated and saved.
- Passwords are encrypted using that key and saved in `password.txt`.
- The same key is used to decrypt and view the saved passwords.

## 🧪 Requirements

- Python 3.6+
- `cryptography` library

Install dependencies:
```bash
pip install cryptography
