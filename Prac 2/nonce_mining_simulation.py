import hashlib
import datetime
import time

class S3PCOINBlock:
    def __init__(self, index, previous_block_hash, transaction_list, nonce=0):
        self.index = index
        self.timestamp = datetime.datetime.now()
        self.transaction_list = transaction_list
        self.previous_block_hash = previous_block_hash
        self.nonce = nonce # A number used in mining to vary the block hash

        # The 'data' attribute now explicitly represents the transactions
        self.data = "-".join(transaction_list) 
        
        # The block_hash will be calculated in mineBlock or on demand
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        # All relevant block information is included in the hash calculation
        block_contents = str(self.index) + str(self.timestamp) + \
                         self.data + self.previous_block_hash + str(self.nonce)
        return hashlib.sha256(block_contents.encode()).hexdigest()

    def mineBlock(self, difficulty_prefix):
        print(f"Mining block {self.index} with difficulty '{difficulty_prefix}'...")
        start_time = time.time()
        attempts = 0

        while True:
            self.block_hash = self.calculate_hash()
            attempts += 1
            if self.block_hash.startswith(difficulty_prefix):
                end_time = time.time()
                time_taken = end_time - start_time
                print(f"Block mined in {attempts} attempts and {time_taken:.4f} seconds.")
                print(f"Block Hash: {self.block_hash}")
                return True
            self.nonce += 1 # Increment nonce for the next attempt

# Example Transactions
t1 = "Steve Sends 2 S3P to Tony"
t2 = "Bruce Sends 2 S3P to Tony"
t3 = "Tony Sends 2 S3P to Bruce"
t4 = "Chris Sends 2 S3P to Steve"
t5 = "Tony Sends 2 S3P to Natasha"
t6 = "Tony Sends 2 S3P to Chris"

# --- Create and Mine Initial Block (Genesis Block) ---
print("--- Mining Initial Block ---")
initial_block = S3PCOINBlock(0, "0", [t1, t2]) # Index 0, "0" for previous hash of genesis block
difficulty = "0000" # Target: hash must start with "0000"
initial_block.mineBlock(difficulty)

print("\n--- Initial Block Details ---")
print(f"Index: {initial_block.index}")
print(f"Timestamp: {initial_block.timestamp}")
print(f"Data: {initial_block.data}")
print(f"Previous Hash: {initial_block.previous_block_hash}")
print(f"Hash: {initial_block.block_hash}")
print(f"Nonce: {initial_block.nonce}")

# --- Create and Mine Second Block ---
print("\n--- Mining Second Block ---")
second_block = S3PCOINBlock(1, initial_block.block_hash, [t3, t4, t5])
second_block.mineBlock(difficulty)

print("\n--- Second Block Details ---")
print(f"Index: {second_block.index}")
print(f"Timestamp: {second_block.timestamp}")
print(f"Data: {second_block.data}")
print(f"Previous Hash: {second_block.previous_block_hash}")
print(f"Hash: {second_block.block_hash}")
print(f"Nonce: {second_block.nonce}")

# --- Create and Mine Third Block with different difficulty ---
print("\n--- Mining Third Block (Higher Difficulty) ---")
third_block = S3PCOINBlock(2, second_block.block_hash, [t6])
higher_difficulty = "00000" # Target: hash must start with "00000"
third_block.mineBlock(higher_difficulty)

print("\n--- Third Block Details ---")
print(f"Index: {third_block.index}")
print(f"Timestamp: {third_block.timestamp}")
print(f"Data: {third_block.data}")
print(f"Previous Hash: {third_block.previous_block_hash}")
print(f"Hash: {third_block.block_hash}")
print(f"Nonce: {third_block.nonce}")