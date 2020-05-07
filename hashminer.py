import os, hashlib
def genblock(message, complexity):
    print(f"Initial message: {message}")
    encoded_message = message.encode()

    # Initialize static padding and hash_block 
    N       = complexity
    padding = hash_block =  b'0'*(N+1)

    # Keep trying to find a correct padding to accord needed complexity
    # The first N'th elements must be zeroes but N+1 is not
    while (hash_block[:N] != '0'*N or hash_block[N] == '0'):
        print(f"hash of a message: {hash_block}")

        # Get the sha hash
        hash_block = hashlib.sha256(encoded_message + padding).hexdigest()

        # Randomize padding
        padding    = os.urandom(16)

    print(f"RESULT: {hash_block}")

if  __name__ == "__main__":
    # Message is a fact of transaction "
    message = "Alice sent 10 btc to Bob"

    # Complexity is a number of zeroes at the beginning 
    complexity = 6

    genblock(message, complexity)
