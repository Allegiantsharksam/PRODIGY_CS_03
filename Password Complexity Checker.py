import re

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password

    def check_length(self):
        return len(self.password) >= 8

    def check_uppercase(self):
        return bool(re.search(r'[A-Z]', self.password))

    def check_lowercase(self):
        return bool(re.search(r'[a-z]', self.password))

    def check_digit(self):
        return bool(re.search(r'\d', self.password))

    def check_special_char(self):
        return bool(re.search(r'\W', self.password))

    def check_strength(self):
        checks = [
            self.check_length(),
            self.check_uppercase(),
            self.check_lowercase(),
            self.check_digit(),
            self.check_special_char()
        ]
        strength = sum(checks)
        return strength

def main():
    password = input("Enter your password: ")
    checker = PasswordStrengthChecker(password)
    strength = checker.check_strength()

    if strength == 5:
        print("Your password is very strong.")
    elif strength == 4:
        print("Your password is strong.")
    elif strength == 3:
        print("Your password is moderate.")
    else:
        print("Your password is weak.")

if __name__ == "__main__":
    main()
