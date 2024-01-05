#Library to define basic padding scheme used

#Unused

import os

def pad(plaintext, block_size):

    # Calculate the number of bytes needed for padding
    padding_size = block_size - len(plaintext) % block_size

    # Generate random padding bytes
    padding = os.urandom(padding_size - 1)  # Subtract 1 to ensure padding is not zero

    # Combine plaintext and padding
    padded_text = plaintext.encode() + padding
    return padded_text


def unpad(padded_text):


    # Find the position of the first zero byte (end of original plaintext)
    null_byte_position = padded_text.find(b'\x00')

    # Extract the original plaintext
    original_text = padded_text[:null_byte_position]
    return original_text.decode()

