import string
import random

# characters to generate password
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    # user defines the length of the password
    password_length = int(input("Enter the password length:\n"))

    # shuffling the characters
    random.shuffle(characters)

    # picking random characters from the list provided above
    password = []
    for i in range(password_length):
        password.append(random.choice(characters))

    # shuffling the password again
    random.shuffle(password)

    # converting the list to a string and printing the password
    print("".join(password))


# invoking the password generator function
generate_random_password()