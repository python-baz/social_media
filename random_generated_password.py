from colorama import Fore, Style
import time
import random
import string

def generate_password():
    length_word = random.randint(4, 13)
    return ''.join(
        random.sample(
            (string.ascii_letters + string.digits),
            length_word
        )
    )

def password_strength(password):
    def is_weak(password):
        return len(password) < 8
    
    def is_strong(password):
        return (
            len(password) >= 11 and
            all(any(method(c) for c in password)
                for method in (str.islower, str.isupper, str.isdigit)
                )
        )
    
    if is_weak(password):
        return "weak"
    elif is_strong(password):
        return "strong"
    else:
        return "medium"

while True:
    password = generate_password()
    strength = password_strength(password)
    # print(f"{password} is {strength}")
    if strength == "strong":
        print(f"{Fore.GREEN}{password}{Style.RESET_ALL}")
    elif strength == "medium":
        print(f"{Fore.YELLOW}{password}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}{password}{Style.RESET_ALL}")
    time.sleep(4)

    





