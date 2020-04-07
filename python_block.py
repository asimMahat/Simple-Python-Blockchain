#importing the necessary libraries
import hashlib
import datetime

class block:

    def __init__(self,previous_blockhash,data,timestamp):

        self.previous_blockhash=previous_blockhash
        self.data=data
        self.timestamp=timestamp
        self.hash=self.get_hash()

    @staticmethod
    def genesis_block():
        return block("0","0",datetime.datetime.now())


    def get_hash(self):
        header=(str(self.previous_blockhash) +
               str(self.data) +
               str(self.timestamp)).encode()
        
        inner_hash=hashlib.sha256(header).hexdigest().encode()

        outer_hash=hashlib.sha256(inner_hash).hexdigest()
        return outer_hash





            




