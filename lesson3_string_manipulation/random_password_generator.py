import string, random

LETTERS = string.ascii_letters
DIGITS = string.digits
PUNCTUATION = string.punctuation

def password_generator(length = 8):
    printable = list(f'{LETTERS}{DIGITS}{PUNCTUATION}')
    random.shuffle(printable)
    
    random_password = random.choices(printable, k = length)
    random_password = ''.join(random_password)
    
    return random_password

def get_password_length():
    password_length = int(input("How long do you want your password: "))
    return password_length

def main():
    password_length = get_password_length()
    password = password_generator(password_length)
    print(password)

if __name__ == "__main__":
    main()