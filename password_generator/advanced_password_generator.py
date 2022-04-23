import string
import random

# characters to generate password
alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    # user defines the length of the password
    password_length = int(input("Enter the password length:\n"))

    # user inputs rhe number of character types
    alphabets_count = int(input("Enter alphabets count in password:\n"))
    digits_count = int(input("Enter digits count in password:\n"))
    special_characters_count = int(input("Enter special characters count in password:\n"))

    characters_count = alphabets_count + digits_count + special_characters_count

    # confirm whether password_length and characters_count are equal
    if characters_count > password_length:
        print("Characters total count is greater than the password length")
        return
    """elif characters_count < password_length:
        print("Characters total count is less than the password length")
        return"""

    # initializing the password
    password = []

    # picking random alphabets
    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    # picking random digits
    for i in range(digits_count):
        password.append(random.choice(digits))

    # picking random alphabets
    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    """ if the total characters count is less than the password length
    add random characters to make it equal to the length"""
    if characters_count < password_length:
        random.shuffle(characters)
        for i in range(password_length - characters_count):
            password.append(random.choice(characters))

    # shuffling the resultant password
    random.shuffle(password)

    # converting the list to a string and printing the password
    print("".join(password))


# invoking the password generator function
generate_random_password()
