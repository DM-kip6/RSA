#Program to define functions used in RSA encryption project
#initial program ('textbook_RSA.py') provided by Dr. John Coleman in MTH 330: Cryptography


#-------------------------------------------------------------------------------------------------
#   Current things that work:
#       Key generation
#       Prime number generation
#       Encryption
#       Decryption
#           Both of above include string->ascii manipulation
#       Read/write from file
#
#   Current things that don't work:
#       File Input
#           Need to prompt user all 3 times in order to get correct file writes


#   Current things to add:
#       Padding
#           Pick a scheme
#
#       Storage for key pairs
#           Take from tkinter filedialog.askopenfile or .askopenfilename
#           Right now it just generates a new key pair every run, which won't work if we want to store an encrypted file and decrypt it later as we won't know the keys anymore
#-------------------------------------------------------------------------------------------------


from primeTesting import *
#from paddingScheme import *
#import tkinter
from tkinter import filedialog as fd



# Generate Pairs of Keys ()
def generate_key_pair():

    #choose two random large prime numbers
    p = generate_prime_number()
    q = generate_prime_number()

    #run a while loop to ensure p and q are not equal (ensuring distinct primes)
    while p == q:
        p = generate_prime_number()
        q = generate_prime_number()
    
    ##512-bit number multiplied by 512-bit number gives a 1024-bit modulus (relatively hard to break, though standard I believe is 2048-bit)
    n = p*q         

    #Euler's totient
    phi = (p-1) * (q-1)

    #public key and private key
    e = 65537
    d = pow(e,-1,phi)


    #defining the key pairs (NOT WORKING SO I WILL RETURN ABOVE DEFINITIONS AS SINGLES)
    #private_key = (d,n)
    #public_key = (e,n)

    return e,d,n



# Encryption/Decryption functions that include string-ascii manipulation
def encrypt(plaintext,public_key,modulus):
    ciphertext = [pow(ord(char), public_key, modulus) for char in plaintext]
    return ciphertext
    

def decrypt(plaintext,private_key,modulus):
    plaintext = ''.join([chr(pow(char,private_key,modulus)) for char in plaintext])
    return plaintext


def prompt_for_file():

    chosen_filename = fd.askopenfilename()

    return chosen_filename



#Dont need this main function, although I can still use it for testing

#Two different variations still here: Choosing a file through prompts, and hardcoding a specific file

def main():

    e,d,n = generate_key_pair()         #generating key pair with modulus

    #string = "Hello! This project is for MTH330: Cryptography, with Dr. John Coleman!"                         #Chosen plaintext for testing
    

    #changes
#    print("Choose a file to perform next tasks on")
#    file = prompt_for_file()
#    with open(file, "r") as file:
#        string = file.read()

#    print("\nPlaintext: ", string)
    #to here


    
    input_file = "TestFiles/sample1.txt"
    with open(input_file, "r") as file:
        string = file.read()

    print("\nPlaintext: ", string)
    


    #Encryption of File (sample1.txt)
    ciphertext = encrypt(string,e,n)    #encrypting the plaintext using public key and modulus
    print("\nCiphertext: ",ciphertext)


    #changing ciphertext (list) into a string in order to write to file
    ciphertext_string = ' '.join([str(elem) for elem in ciphertext])


    #Writing encryption to file
    
#    print("Choose a file to save encryption to")
#    encrypted_file = prompt_for_file()
#    with open(encrypted_file, "w") as encrypted_file1:
#        encrypted_file1.write(ciphertext_string)

#    print(f"\nEncrypted text written to: {encrypted_file}")


    encrypted_file = "TestFiles/encrypted_text"
    with open(encrypted_file, "w") as encrypted_file1:
        encrypted_file1.write(ciphertext_string)

    print(f"\nEncrypted text written to: {encrypted_file}")




    #Decryption of File (sample1.txt)
    plaintext = decrypt(ciphertext,d,n)
    print("\nPlaintext: ",plaintext)

    
    #writing decryption to file
#    print("Choose a file to save decryption to")
#    decrypted_file = prompt_for_file()
#    with open(decrypted_file, "w") as decrypted_file1:
#        decrypted_file1.write(plaintext)

#    print(f"\nDecrypted text written to: {decrypted_file}")

    decrypted_file = "TestFiles/sample1.txt"
    with open(decrypted_file, "w") as decrypted_file1:
        decrypted_file1.write(plaintext)

    print(f"\nDecrypted text written to: {decrypted_file}")





if __name__ == '__main__':
    main()












#Redundant/Optimized/Unused Functions



#Original Encryption/Decryption Functions 
#def encrypt(plaintext,public_key,modulus):
#    ciphertext = pow(plaintext,public_key,modulus)
#    return ciphertext
    

#def decrypt(plaintext,private_key,modulus):
#    plaintext = pow(plaintext,private_key,modulus)
#    return plaintext



#Unused function to try for a file prompt (WORKED, HAD OTHER ISSUES WITH FILE MANIPULATION)

#    def prompt_file():
#        """Create a Tk file dialog and cleanup when finished"""
#        top = tkinter.Tk()
#        top.withdraw() # hide window
#        file_name = tkinter.filedialog.askopenfilename(parent=top)
#        top.destroy()
#        return file_name





#Unused unctions for letter to number manipulation (DIDNT WORK GOING FROM ASCII TO STRING)
#def string_to_ascii(string):

    # Convert each character to its ASCII value and concatenate as a string
#    ascii_string = ''.join(str(ord(char)) for char in string)
    
    # Convert the concatenated string to an integer
#    result_int = int(ascii_string)
#    return result_int


#def int_to_string(input_int):
    # Convert the integer to a string
#    ascii_string = str(input_int)
    
    # Split the string into two-digit substrings
#    two_digit_substrings = [ascii_string[i:i+2] for i in range(0, len(ascii_string), 2)]
    
    # Convert each two-digit substring to the corresponding character and join them
#    result_string = ''.join(chr(int(substring)) for substring in two_digit_substrings)
    
#    return result_string