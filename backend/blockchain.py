import hashlib
import json
import time



class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(previous_hash="1", proof=100)  # Tạo Genesis Block
        
#         self.chain: Lưu danh sách các block của blockchain.

# self.transactions: Lưu các giao dịch trước khi được thêm vào một block.

# create_block(previous_hash="1", proof=100): Tạo Genesis Block (block đầu tiên).

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.transactions.copy(),  # Lưu giao dịch vào block
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.transactions = []  # Xóa giao dịch sau khi đã thêm vào block
        self.chain.append(block)
        return block
    
#     proof: Giá trị dùng trong thuật toán Proof of Work.

# previous_hash: Giá trị băm của khối trước đó để đảm bảo tính liên kết.

# Mỗi block chứa:

#     Chỉ mục (index)

#     Thời gian tạo (timestamp)

#     Danh sách giao dịch

#     Bằng chứng công việc (proof)

#     Băm của khối trước (previous_hash)

#  Lấy khối trước đó
    def get_previous_block(self):
        return self.chain[-1]
    
    # Trả về khối mới nhất trong chuỗi blockchain.

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while not self.is_valid_proof(new_proof, previous_proof):
            new_proof += 1
        return new_proof
    # Lặp qua các giá trị new_proof cho đến khi tìm được giá trị phù hợp với điều kiện băm.

    def is_valid_proof(self, new_proof, previous_proof):
        guess = f'{new_proof}{previous_proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    def hash_block(self, block):
        return hashlib.sha256(json.dumps(block, sort_keys=True).encode()).hexdigest()

    def add_transaction(self, sender, receiver, amount):
        transaction = {'sender': sender, 'receiver': receiver, 'amount': amount}
        self.transactions.append(transaction)
        return self.get_previous_block()['index'] + 1
# Tạo một giao dịch với 3 thông tin: người gửi, người nhận, số tiền.

# Giao dịch được thêm vào danh sách chờ (self.transactions).

# Trả về chỉ mục của khối tiếp theo.

    def is_chain_valid(self, chain):
        for i in range(1, len(chain)):
            if chain[i]['previous_hash'] != self.hash_block(chain[i - 1]):
                return False
            if not self.is_valid_proof(chain[i]['proof'], chain[i - 1]['proof']):
                return False
        return True
    
#  Kiểm tra liên kết giữa các block: previous_hash của block hiện tại phải khớp với hash_block() của block trước đó.

# Kiểm tra Proof of Work: Đảm bảo mỗi block được đào hợp lệ.
