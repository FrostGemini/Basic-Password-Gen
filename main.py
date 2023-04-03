import random
import string

def generate_password(length):
    """
    Generate a random password of a given length.
    """
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def main():
    while True:
        try:
            pass_len = int(input("How many characters? "))
            if pass_len < 8:
                raise ValueError("Password length must be at least 8 characters.")
            pass_count = int(input("How many to generate? "))
            if pass_count <= 0:
                raise ValueError("Number of passwords to generate must be greater than 0.")
            for i in range(pass_count):
                password = generate_password(pass_len)
                print(f"Password {i+1}: {password}")
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting password generator.")
            break

if __name__ == '__main__':
    main()
