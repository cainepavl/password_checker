# Password Checker

A simple command-line tool that checks if your passwords have been compromised using the [Have I Been Pwned](https://haveibeenpwned.com/) API. This tool helps users ensure their passwords are secure and encourages them to change compromised passwords. 

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
- [Example Output](#example-output)
- [How it Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- Check multiple passwords at once.  
- Clear console output for better readability.  
- Color-coded output indicating password security status.  

## Requirements  

- Python 3.x installed on your machine. You can download it from [Python](https://github.com/cainepavl/portfo/blob/main/LICENSE)
- `requests` library  
- `colorama` library  

You can install the required libraries using pip: 

```bash  
pip3 install requests colorama 
```
## Usage

1. Clone this repository:
   
```
git clone https://github.com/cainepavl/password-checker.git  
cd password-checker
```
   
2. Run the program with your passwords as command-line arguments:

```
python3 password_checker.py password1 password2 password3
```

... replace `password1`, `password2`, and `password3` with the passwords you want to check.

## Example Output

For a SAFE password the output will be GREEN:
```
password123 was found 5 times...</span> 
You should change it!</span> 
```

For a COMPROMISED password the output will be RED:
```
mySecurePassword is good to go!
```


## How It Works

1. Password Hashing: The program takes each password, hashes it using SHA-1, and sends the first 5 characters of the hash to the Have I Been Pwned API.
   
2. API Response: The API returns a list of hashes that start with those 5 characters, allowing the program to check how many times the full password hash appears in the database.
   
3. Output: The program displays whether each password is compromised or secure, with color-coded messages for better visibility.


## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to create a pull request or open an issue.

## License

This project is licensed under the MIT License - [LICENSE](https://github.com/cainepavl/password_checker/blob/main/LICENSE) see the  file for details.

## Acknowledgments

[HAVE I BEEN PWNED](https://haveibeenpwned.com/) for providing the API.

[COLORAMA](https://pypi.org/project/colorama/) for terminal color formatting.

[ZTM Academy](https://zerotomastery.io/courses/) for the course and walkthrough creating this site!

## Contact

If you have any questions, feel free to contact me at cainepavl@outlook.com
