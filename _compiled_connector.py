import os
import hashlib
import json

# Path untuk menyimpan data pengguna
DATA_AKUN = "users.json"

# Fungsi untuk memuat data pengguna
def load_users():
    if os.path.exists(DATA_AKUN):
        with open(DATA_AKUN, "r") as file:
            return json.load(file)
    return {}

# Fungsi untuk menyimpan data pengguna
def save_users(users):
    with open(DATA_AKUN, "w") as file:
        json.dump(users, file, indent=4)

# Fungsi untuk menangani login
def login_action(email, password):
    users = load_users()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    if email in users and users[email]["password"] == hashed_password:
        return True, "Login sukses! Selamat Datang."
    elif email not in users:
        return False, "Email not found. Please sign up first."
    else:
        return False, "Incorrect password. Please try again."

# Fungsi untuk menangani registrasi
def register_action(email, password):
    users = load_users()
    if email in users:
        return False, "Email already registered. Please login."

    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    users[email] = {"password": hashed_password}
    save_users(users)
    return True, "Registration successful! You can now login."
