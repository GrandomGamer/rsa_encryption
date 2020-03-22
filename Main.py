#Name: Alexander Trepasso
#Description: This program is a very basic implementation of the RSA Algorithm
#It will take in a persons input and two prime numbers and work through encryption and decryption
#While explaining the results.
#Stackoverflow was a big help in figuring out minor functions such as ord() and chr() https://stackoverflow.com/questions/50314440/what-does-the-name-of-the-ord-function-stand-for , https://stackoverflow.com/questions/28184134/python-chr-explain
#Also I used the RSA Algorithm wikipedia for finding the actual operations math wise for key gen. https://en.wikipedia.org/wiki/RSA_(cryptosystem)

#Variable Setup
import random
from math import gcd
pubkey = []
encryptlet = []
primes = []
#Get User inputs for prime numbers for key generation and turn them into integers
#Also welcome the user.
print('Welcome to the encryptor.')
print('This program will allow you to encrypt and decrypt any string you want and show you the math as you go.')

#Overall checking for primes > 1
def checkprime(input):
    if input>1:
        for x in range(2, input//2):
            if(input % x) == 0:
                return False
        else:
            return True
    else:
        return False

#Ask if they want to generate primes, if so create them.
def generatePrimes():
    selection = input("Would you like to input your own prime numbers?\nType 'yes' or 'no'\n")
    if selection == 'yes':
        while len(primes) < 2:
            getInputs()
    elif selection == 'no':
        print('Generating primes...')
        while len(primes) < 2:
            new_number = random.randint(2,100)
            if checkprime(new_number) == True:
                primes.append(new_number)


#Get the user inputs.
def getInputs():
    num_input = int(input("Please enter a prime number: "))
    if checkprime(num_input) == True:
        primes.append(num_input)
    else:
        print("WARNING! Only enter prime numbers that are greater than 1.")

generatePrimes()
#Key Generator Function that also does the math for the RSA Algorithm
def keygen():
    gfound = False
    dfound = False
    multiplied_prime = primes[0]*primes[1]
    subtracted_prime = (primes[0]-1)*(primes[1]-1)
    e = 2
    priv_exponent = 0
    #Get Public Key and Print it out
    while gfound == False:
        if gcd(e,subtracted_prime) == 1:
            pubkey.append(e)
            pubkey.append(multiplied_prime)
            print("Public Key:",pubkey)
            gfound = True
        else:
            e = e + 1
    #Get Private and Print it Out
    while dfound == False:
        f = e*priv_exponent
        if f%subtracted_prime == 1:
            privkey = priv_exponent
            print("Private Key:",privkey)
            dfound = True
        else:
            priv_exponent = priv_exponent+1
    return privkey
#Call Keygeneration function to allow multiple runs.
privkey = keygen()

#Get and encrypt the string that was picked by the user.
def tonum(st):
    chars = []
    for ch in st:
        cur = ord(ch) ** pubkey[0]
        charnum = cur % pubkey[1]
        chars.append(charnum)
        encryptlet.append(charnum)
    print("Encrypted output: " + str(encryptlet))
    return chars
st = input("What would you like to encrypt? ")

charlist = tonum(st)
#Take the encrypted string and decrypt it.
def tolet():
    out = ""
    for i in range(0, len(charlist)):
        charnum = (charlist[i] ** privkey) % pubkey[1]
        out = out + chr(charnum)
    print("Decrypted output: " + out)

tolet()
