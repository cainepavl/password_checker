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

- Check one or more passwords in a single session.
- Hidden input via `getpass` — passwords are never echoed to the screen,
  stored in shell history, or visible to other users via `ps`.
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

Run the script and enter passwords when prompted. Input is hidden as you type:

```bash
python3 checkmypass.py
```

```
Enter a password to check (input hidden). Press Enter on a blank line to finish.

Password:
```

Check as many passwords as you like, one per prompt — press Enter on a
blank line when you're done.

> Earlier versions of this script accepted passwords as command-line
> arguments (`python3 checkmypass.py password1 password2`). That approach
> left plaintext passwords sitting in shell history and visible to other
> local users via `ps`, so it was replaced with a hidden `getpass` prompt.

---

## 📸 Example Output

For a **SAFE** password the output will be GREEN:

```
Not found in any known breach -- good to go!
```

For a **COMPROMISED** password the output will be RED:

```
Found in 5 breach(es)... You should change it!
```

---

## 🔍 How It Works

1. **Password Hashing**: The program takes each password, hashes it using SHA-1, and sends only the first 5 characters of the hash to the Have I Been Pwned API — a k-anonymity model, so the full hash (and the password itself) never leaves your machine.

2. **API Response**: The API returns a list of hashes that start with those 5 characters, allowing the program to check how many times the full password hash appears in the database.

3. **Output**: The program displays whether each password is compromised or secure, with color-coded messages for better visibility. The password itself is never printed back to the terminal.

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
