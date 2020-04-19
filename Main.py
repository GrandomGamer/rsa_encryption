"""
The main file for my encryption integration project.
Description: This program is a very basic implementation of the RSA Algorithm,
it will take in a persons input and two prime numbers and work through
encryption and decryption while explaining the results.
Stackoverflow was a big help in figuring out minor functions such as ord()
and chr()
https://stackoverflow.com/questions/50314440/what-does-the-name-of-the-ord-function-stand-for,
https://stackoverflow.com/questions/28184134/python-chr-explain
Also I used the RSA Algorithm wikipedia for finding the actual operations math
wise for key gen. https://en.wikipedia.org/wiki/RSA_(cryptosystem)
"""
___author___ = "Alexander Trepasso"


import random
from math import gcd

pubkey = []
encryptlet = []
primes = []
print('Welcome to the encryptor.')
print('This program will allow you to encrypt and decrypt any string you '
      'want and show you the math as you go.')


def checkprime(number):
    """
    Checks if the number is prime and returns true or false.
    """
    try:
        num = int(number)
    except ValueError:
        return False
    if num > 1:
        for x in range(2, num // 2):
            if (num % x) == 0:
                return False
        else:
            return True
    else:
        return False



def generate_primes():
    """
    Asks the user if they want the computer to generate primes or input their
    own, if so it generates the primes.
    """
    selection = input("Would you like to input your own prime numbers?\nType "
                      "'yes' or 'no'\n")
    if selection == 'yes':
        while len(primes) < 2:
            get_inputs()
    elif selection == 'no':
        print('Generating primes...')
        while len(primes) < 2:
            new_number = random.randint(2, 100)
            if checkprime(new_number):
                primes.append(new_number)
                print(primes)
    else:
        print('Please enter a valid response.')
        generate_primes()


def get_inputs():
    """
    Gets the user inputs for their chosen primes.
    """
    num_input = input("Please enter a prime number: ")
    if checkprime(num_input):
        primes.append(int(num_input))
    else:
        print("WARNING! Only enter prime numbers that are greater than 1.")


generate_primes()


def keygen():
    """
    Implements the RSA Algorithm to generate the public and private keys.
    """
    gfound = False
    dfound = False
    priv = 0
    multiplied_prime = primes[0] * primes[1]
    subtracted_prime = (primes[0] - 1) * (primes[1] - 1)
    e = 2
    priv_exponent = 0
    while not gfound:
        if gcd(e, subtracted_prime) == 1:
            pubkey.append(e)
            pubkey.append(multiplied_prime)
            print("Public Key:", pubkey)
            gfound = True
        else:
            e += 1
    while not dfound:
        f = e * priv_exponent
        if f % subtracted_prime == 1:
            priv = priv_exponent
            print("Private Key:", priv)
            dfound = True
        else:
            priv_exponent += 1
    if gfound and dfound:
        # noinspection PyUnboundLocalVariable
        return priv


privkey = keygen()


def tonum(string):
    """

    Takes the user string and encrypts it by turning it into numbers.
    """
    chars = []
    encryptedstr = ""
    for ch in string:
        cur = ord(ch) ** pubkey[0]
        charnum = cur % pubkey[1]
        chars.append(charnum)
        encryptedstr += chr(charnum)
        encryptlet.append(charnum)
    print("Encrypted output: " + str(encryptlet) + " = " + encryptedstr)
    return chars


st = input("What would you like to encrypt? ")

charlist = tonum(st)


def tolet():
    """
    Take the encrypted string and decrypt it.
    """
    out = ""
    for i in range(0, len(charlist)):
        charnum = (charlist[i] ** privkey) % pubkey[1]
        out += chr(charnum)
    print("Decrypted output: " + out)


tolet()
