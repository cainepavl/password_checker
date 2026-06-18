# 🕵️ Password Checker

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.x](https://img.shields.io/badge/python-3.x-blue.svg)]()
[![HIBP API](https://img.shields.io/badge/HIBP_API-Integrated-red.svg)]()

A simple command-line tool that checks if your passwords have been compromised using the [Have I Been Pwned](https://haveibeenpwned.com/) API. This tool helps users ensure their passwords are secure and encourages them to change compromised passwords.

## 📋 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Contact/Connect](#contactconnect)

---

## ✨ Features

- Check multiple passwords at once.
- Clear console output for better readability.
- Color-coded output indicating password security status.

---

## ⬇️ Requirements

- [Python 3.x](https://www.python.org/downloads/) installed on your machine
- `requests` library
- `colorama` library

---

## 🛠️ Installation

### 🐍 Verify Python

```bash
python3 --version
# Requires Python 3.x
```

### 📥 Clone the Repository

```bash
git clone https://github.com/cainepavl/password_checker.git
cd password_checker
```

### ⬇️ Install Dependencies

```bash
pip3 install requests colorama
```

---

## 🚀 Usage

Run the program with your passwords as command-line arguments:

```bash
python3 password_checker.py password1 password2 password3
```

Replace `password1`, `password2`, and `password3` with the passwords you want to check.

---

## 📸 Example Output

For a **SAFE** password the output will be GREEN:

```
mySecurePassword is good to go!
```

For a **COMPROMISED** password the output will be RED:

```
password123 was found 5 times...
You should change it!
```

---

## 🔍 How It Works

1. **Password Hashing**: The program takes each password, hashes it using SHA-1, and sends the first 5 characters of the hash to the Have I Been Pwned API.

2. **API Response**: The API returns a list of hashes that start with those 5 characters, allowing the program to check how many times the full password hash appears in the database.

3. **Output**: The program displays whether each password is compromised or secure, with color-coded messages for better visibility.

---

## 🔧 Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to create a pull request or open an issue.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- [HAVE I BEEN PWNED](https://haveibeenpwned.com/) for providing the API.
- [COLORAMA](https://pypi.org/project/colorama/) for terminal color formatting.
- [ZTM Academy](https://zerotomastery.io/courses/) for the course and walkthrough creating this tool!

---

## 📩 Contact/Connect

**Caine Pavlosky**

* Email: [cainepavl@outlook.com](mailto:cainepavl@outlook.com)
* Portfolio: [fairdinkumstudios.com](https://fairdinkumstudios.com/)
* LinkedIn: [linkedin.com/in/cainepavlosky008](https://linkedin.com/in/cainepavlosky008)
