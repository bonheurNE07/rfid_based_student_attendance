from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
import os

# Generate a key from the passowrd using PBKDF2
def generateKey(password, salt=b'salt', iterations=100000):
    return PBKDF2(password, salt, dkLen=32, count=iterations)

# Encrypt data using AES
def encryptData(data, key):
    cipher = AES.new(key, AES.MODE_EAX)
    cipher_text, tag = cipher.encrypt_and_digest(data.encode())
    return cipher.nonce, tag, cipher_text

# Decrypt data using AES
def decryptData(nonce, tag, cipher_text, key):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(cipher_text, tag)
    return plaintext.decode()

# Store encrypted credentials in a file
def storeCredentials(filename, key, username, password, email):
    with open(filename, 'wb') as file:
        nonce, tag, cipher_text = encryptData(f"{username}\n{password}\n{email}", key)
        file.write(nonce)
        file.write(tag)
        file.write(cipher_text)


# Read and decrypt credentials from a file
def readCredentials(filename, key):
    with open(filename, 'rb') as file:
        nonce = file.read(16)
        tag = file.read(16)
        cipher_text = file.read()
        decrypted_data = decryptData(nonce, tag, cipher_text, key)
        # Split decrypted data into separate fields
        username, password, email = decrypted_data.split('\n')
        return [username, password, email]

###################################################################################
#                                                                                 #
# ! USE TO GENERATE THE CRYPTED FILE ! PROVIDE DATA AND AFTER DETE THEM FROM HERE #
#                                                                                 #
###################################################################################

if __name__ == "__main__":
    filename = "../credentials.enc" # Encypted file name and path
    secret_password = "bonheurNDEZEemmanuel37" # Administartor's password to be encrypted ( this will be used to generate the key but not stored on the file)
    key = generateKey(secret_password.encode()) # Generate the key from the password

    admin_password = "bonheurBNE37"
    admin_name = "Admin"
    admin_email = "ndezeBE@gmail.com"

    # Store encrypted credentials
    # Check if the file already exists
    if not os.path.exists(filename):
        # Create the file if it doesn't exist
        storeCredentials(filename, key, admin_name, admin_password, admin_email)
        print(f"Credentials stored in {filename}")
    else:
        print(f"File {filename} already exists. Delete or rename the file to store new credentials.")
    

    # Read and decrypt credentials
    decrypted_data = readCredentials(filename, key)
    print(f"Decrypted Credentials: {decrypted_data}")


