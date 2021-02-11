import hashlib

# Prepare the transaction
sender = "0xAlice"
receiver = "0xBob"
amount = "10"

transaction = sender + ";" + receiver + ";" + amount + ";"
print("Transaction text: " + transaction)

salt = 0

# Loop over all salts and check if the condition is met
while True:
    salt = salt+1
    print("Trying salt " + str(salt))

    # Create a block with the current salt
    block = transaction + str(salt)
    print("Created block: " + block)

    # Hash the block
    blhash = hashlib.sha256(block.encode('utf-8')).hexdigest()
    print("Got hash: " + blhash)

    # Check for the leading zeros
    if blhash[0:3] == "000":
        print("Salt correct")
        print("Salt: " + str(salt) + " with hash " + blhash)
        break
    else:
        print("Salt incorrect")
    

print("Finished")
