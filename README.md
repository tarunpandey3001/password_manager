# 🔐 Password Manager

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)  
A secure and easy-to-use **Password Manager** built with **Python** and a sleek **Tkinter GUI**. Store, retrieve, and generate strong passwords with confidence and convenience.

---

## ✨ Features

- 🔒 **Secure Storage** using local file encryption
- 🎨 **Modern GUI** with Tkinter
- 🔑 **Random Password Generator** (customizable length and complexity)
- 📁 **Save & Retrieve** passwords by website or app name
- 📋 **Copy to Clipboard** functionality
- 🚀 **Lightweight and fast** — no internet required

---

## 🖼️ Interface Preview

> *(Insert screenshots here if available)*  
> You can add screenshots to this section to showcase the UI.

---

## 🛠️ Tech Stack

- **Python 3.10+**
- **Tkinter** for GUI
- **`json`** for data storage
- **`secrets`** and **`random`** for secure password generation
- **`pyperclip`** (optional) for clipboard functionality

---

## 🧩 How It Works

1. **Enter** website, email/username, and password.
2. **Click** “Add” to save credentials securely.
3. **Use** the “Search” function to retrieve saved logins.
4. **Generate** secure random passwords with ease.

> All credentials are stored locally in a JSON file. Optionally, encryption can be added for improved security.

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.10+
- `tkinter` (usually pre-installed with Python)
- `pyperclip` *(optional, for clipboard)*

### 📥 Installation

```bash
git clone https://github.com/tarunpandey3001/password-manager.git
cd password-manager
pip install -r requirements.txt
python main.py
