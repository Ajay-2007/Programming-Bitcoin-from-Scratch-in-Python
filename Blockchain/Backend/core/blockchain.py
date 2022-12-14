import sys

sys.path.append('/home/ajay/upwork/github/Programming-Bitcoin-from-Scratch-in-Python')

import json
import time

from Blockchain.Backend.core.block import Block
from Blockchain.Backend.core.blockheader import BlockHeader
from Blockchain.Backend.utils.util import hash256

ZERO_HASH = '0' * 64
VERSION = 1
class Blockchain:
    def __init__(self):
        self.chain = []
        self.GenesisBlock()

    def GenesisBlock(self):
        BlockHeight = 0
        prevBlockHash = ZERO_HASH
        self.addBlock(BlockHeight, prevBlockHash)

    def addBlock(self, BlockHeight, prevBlockHash):
        timestamp = int(time.time())
        Transaction = f"Codies Alert sent {BlockHeight} Bitcoins to Joe"
        merkleRoot = hash256(Transaction.encode()).hex()
        bits = 'ffff001f'
        blockheader = BlockHeader(VERSION, prevBlockHash, merkleRoot, timestamp, bits)
        blockheader.mine()
        self.chain.append(Block(BlockHeight, 1, blockheader.__dict__, 1, Transaction).__dict__)
        print(json.dumps(self.chain, indent=4))

    def main(self):
        while True:
            lastBlock = self.chain[::-1]
            BlockHeight = lastBlock[0]['Height'] + 1
            prevBlockHash = lastBlock[0]['BlockHeader']['blockHash']
            self.addBlock(BlockHeight, prevBlockHash)


if __name__ == "__main__":
    blockchain = Blockchain()
    blockchain.main()
