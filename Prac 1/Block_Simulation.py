import hashlib
import datetime

class S3PCOINBlock:
    def __init__(self, index, previous_block_hash, transaction_list, nonce=0):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.transaction_list = transaction_list
        self.previous_block_hash = previous_block_hash
        self.nonce = nonce # A number used in mining to vary the block hash

        # The 'data' attribute now explicitly represents the transactions
        self.data = "-".join(transaction_list) 
        
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        # All relevant block information is included in the hash calculation
        block_contents = str(self.index) + str(self.timestamp) + \
                         self.data + self.previous_block_hash + str(self.nonce)
        return hashlib.sha256(block_contents.encode()).hexdigest()

# Example Usage:
t1 = "Steve Sends 3 S3P to Tony"
t2 = "Bruce Sends 4 S3P to Tony"
t3 = "Tony Sends 1 S3P to Bruce"
t4 = "Chris Sends 4 S3P to Steve"
t5 = "Tony Sends 6 S3P to Natasha"
t6 = "Tony Sends 8 S3P to Chris"

# Creating the initial block
initial_block = S3PCOINBlock(0, "0", [t1, t2]) # Index 0, "0" for previous hash of genesis block

print("--- Initial Block ---")
print(f"Index: {initial_block.index}")
print(f"Timestamp: {initial_block.timestamp}")
print(f"Data: {initial_block.data}")
print(f"Previous Hash: {initial_block.previous_block_hash}")
print(f"Hash: {initial_block.block_hash}")
print(f"Nonce: {initial_block.nonce}")

# Creating a second block, linked to the first
second_block = S3PCOINBlock(1, initial_block.block_hash, [t3, t4])

print("\n--- Second Block ---")
print(f"Index: {second_block.index}")
print(f"Timestamp: {second_block.timestamp}")
print(f"Data: {second_block.data}")
print(f"Previous Hash: {second_block.previous_block_hash}")
print(f"Hash: {second_block.block_hash}")
print(f"Nonce: {second_block.nonce}")

# Creating a second block, linked to the first
third_block = S3PCOINBlock(2, second_block.block_hash, [t5, t6])

print("\n--- Third Block ---")
print(f"Index: {third_block.index}")
print(f"Timestamp: {third_block.timestamp}")
print(f"Data: {third_block.data}")
print(f"Previous Hash: {third_block.previous_block_hash}")
print(f"Hash: {third_block.block_hash}")
print(f"Nonce: {third_block.nonce}")