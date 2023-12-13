from cryptography.fernet import Fernet
import os

class SimpleKMS:
    def __init__(self, key_file='key.key'):
        self.key_file = key_file
        self.ensure_key()

    def ensure_key(self):
        """
        Ensures that a key exists; if not, it generates a new one.
        """
        if not os.path.exists(self.key_file):
            self.generate_key()

    def generate_key(self):
        """
        Generates a new key and saves it to the specified file.
        """
        key = Fernet.generate_key()
        with open(self.key_file, 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        """
        Loads the key from the specified file.
        """
        with open(self.key_file, 'rb') as key_file:
            key = key_file.read()
        return key

    def encrypt(self, message):
        """
        Encrypts a given message.
        """
        key = self.load_key()
        f = Fernet(key)
        encrypted_message = f.encrypt(message.encode())
        return encrypted_message.decode()

    def decrypt(self, encrypted_message):
        """
        Decrypts an encrypted message.
        """
        key = self.load_key()
        f = Fernet(key)
        decrypted_message = f.decrypt(encrypted_message.encode())
        return decrypted_message.decode()
