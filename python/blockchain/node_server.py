from hashlib import sha256
import json
import time

from flask import Flask, request
import requests


class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce

    def compute_hash(self):
        """
        返回区块哈希值
        """
        block_string = json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode("UTF-8")).hexdigest()


class Blockchain:
    # PoW算法难度等级
    difficulty = 2

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []

    def create_genesis_block(self):
        """
        生成创始区块，并将其附加到链上。
        改区块索引为 0，previous_hash 为0，为有效哈希值。
        """
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_block(self, block, proof):
        """
        区块验证后，增加到链中。验证包括：
        * 检查证明是否有效；
        * 区块的previous_hash值和最新区块的哈希值匹配。
        """
        previous_hash = self.last_block.hash

        if previous_hash != block.previous_hash:
            return False

        if not Blockchain.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)

        return True

    def proof_of_work(self, block):
        """
        尝试不同的随机数以获得满足难度标准的哈希值。
        """
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()

        return computed_hash

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    @classmethod
    def is_valid_proof(cls, block, block_hash):
        """
        检查 block_hash 是否是一个有效的区块哈希值，且是否符合难度标准。
        """
        return (block_hash.startswith('0' * Blockchain.difficulty) and
                block_hash == block.compute_hash())

    @classmethod
    def check_chain_validity(cls, chain):
        result = True
        previous_hash = "0"

        for block in chain:
            block_hash = block.hash
            # 删除哈希值并重新计算
            delattr(block, "hash")

            if not cls.is_valid_proof(block, block.hash) or \
                    previous_hash != block.previous_hash:
                result = False
                break

            block.hash, previous_hash = block_hash, block_hash

        return result

    def mine(self):
        """
        接口：通过将事务加入区块，并计算出工作证明，从而将其加入区块链中。
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(index=last_block.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        self.unconfirmed_transactions = []
        # 想网络公告
        announce_new_block(new_block)
        return new_block.index


app = Flask(__name__)

# 节点的区块链副本
blockchain = Blockchain()
blockchain.create_genesis_block()

# 网络中其它参与成员的地址
peers = set()


@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    print("====== new_transaction start ======")

    tx_data = request.get_json()
    required_fields = ["author", "content"]

    print(tx_data)
    print(required_fields)

    for field in required_fields:
        if not tx_data.get(field):
            return "无效事务数据", 404

    tx_data["timestamp"] = time.time()
    blockchain.add_new_transaction(tx_data)

    return "ok", 201

@app.route('/chain', methods=['GET'])
def get_chain():
    print("====== get_chain start ======")

    consensus()
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data,
                       "peers": list(peers)})

@app.route('/mine', methods=['GET'])
def mine_unconfirmed_transactions():
    print("====== mine_unconfirmed_transactions start ======")

    result = blockchain.mine()
    if not result:
        return "无事务待挖掘"
    return "区块 #{} 已被挖掘".format(result)

@app.route('/register_node', methods=['POST'])
def register_new_peers():
    print("====== register_new_peers start ======")

    node_address = request.get_json()["node_address"]
    if not node_address:
        return "无效数据", 400

    peers.add(node_address)

    return get_chain()

@app.route('/register_with', methods=['POST'])
def register_with_existing_node():
    print("====== register_with_existing_node start ======")

    """
    内部调用 register_node 端点，将当前节点注册到请求中指定的节点，并同步区块链和对等数据。 
    """
    node_address = request.get_json()["node_address"]
    if not node_address:
        return "无效数据", 400

    data = {"node_address": request.host_url}
    headers = {'Content-Type': "application/json"}

    response = requests.post(node_address + "/register_node",
                             data=json.dumps(data), headers=headers)

    if response.status_code == 200:
        global blockchain
        global peers

        chain_dump = response.json()['chain']
        blockchain = create_chain_from_dump(chain_dump)
        peers.update(response.json()['peers'])
        return "注册成功", 200
    else:
        return response.content, response.status_code

def create_chain_from_dump(chain_dump):
    blockchain = Blockchain()
    for idx, block_data in enumerate(chain_dump):
        block = Block(block_data["index"],
                      block_data["transactions"],
                      block_data["timestamp"],
                      block_data["previous_hash"])
        proof = block_data['hash']
        if idx > 0:
            added = blockchain.add_block(block, proof)
            if not added:
                raise Exception("链堆被篡改！")
        else:
            blockchain.chain.append(block)
    return blockchain

@app.route('/add_block', methods=['POST'])
def verify_and_add_block():
    print("====== verify_and_add_block start ======")

    block_data = request.get_json()
    block = Block(block_data["index"],
                  block_data["transactions"],
                  block_data["timestamp"],
                  block_data["previous_hash"])

    proof = block_data['hash']
    added = blockchain.add_block(block, proof)

    if not added:
        return "该块已被节点丢弃", 400

    return "区块已添加到链", 201

@app.route('/pending_tx')
def get_pending_tx():
    print("====== get_pending_tx start ======")

    return json.dumps(blockchain.unconfirmed_transactions)

def consensus():
    """
    简单共识算法：如果找到一个更长的有效链，则用它替换我们的链。
    """
    global blockchain

    longest_chain = None
    current_len = len(blockchain.chain)

    for node in peers:
        print('{}/chain'.format(node))
        response = requests.get('{}chain'.format(node))
        print("Content", response.content)
        length = response.json()['length']
        chain = response.json()['chain']
        if length > current_len and blockchain.check_chain_validity(chain):
            current_len = length
            longest_chain = chain

    if longest_chain:
        blockchain = longest_chain
        return True

    return False

def announce_new_block(block):
    """
    像网络宣告此块已被挖掘。
    其它区块可简单验证工作证明，并将其添加到各自的链中。
    """
    for peer in peers:
        url = "{}add_block".format(peer)
        requests.post(url, data=json.dumps(block.__dict__, sort_keys=True))
