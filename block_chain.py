from python_block import block #calling block class from python file "python_block.py"
import datetime

# b1= block.genesis_block()
# print(b1.hash)
blockchain=[block.genesis_block()]
print("Block 0 - Genesis Block")
print("Block 0 DATA : can be anything")
print("Block 0 Hash : %s" % blockchain[-1].hash)
print("----------------------------------------------------------------------------------------")
num_of_block=10
#inclusive
for i in range(1,num_of_block +1):

    blockchain.append(block(blockchain[-1].hash,
                            "data !",
                            datetime.datetime.now()))
    

    print("Block %d " % i)
    print("Block %d DATA : can be anything" % i )
    print("Block %d HASH : %s"  %(i, blockchain[i].hash))
    print('----------------------------------------------------------------------------------------')
