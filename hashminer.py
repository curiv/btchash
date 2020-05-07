import os, hashlib

def genblock(message, complexity):
    print(f"Initial message: {message}")
    encoded_message = message.encode()
    padding = hash_block =  b''

    while hash_block[0:complexity] != '0'*complexity:
        encoded_message += padding
        hash_block = hashlib.sha256(encoded_message).hexdigest()
        print(f"hash of a message: {hash_block}")

        padding  = os.urandom(16)

if  __name__ == "__main__":
    # Message is a fact of transaction "
    message = "Alice sent 10 btc to Bob"

    # Complexity is a number of zeroes at the beginning 
    complexity = 2

    genblock(message, complexity)
