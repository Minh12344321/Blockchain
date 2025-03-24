from flask import Flask, jsonify, request
from flask_cors import CORS
from blockchain import Blockchain



app = Flask(__name__)
CORS(app)

blockchain = Blockchain()

@app.route('/', methods=['GET'])
def index():
    return jsonify({"message": "Hello from the Blockchain API!"}), 200

@app.route('/mine', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash_block(previous_block)
    block = blockchain.create_block(proof, previous_hash)

    response = {
        'message': 'New block mined!',
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash']
    }
    return jsonify(response), 200
# Lấy block cuối cùng (get_previous_block()).

# Tìm proof hợp lệ (proof_of_work()).

# Tạo block mới (create_block()).

# Trả về thông tin block vừa đào.
@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    data = request.get_json()
    if not data or not all(k in data for k in ("sender", "receiver", "amount")):
        return jsonify({"error": "Missing transaction fields"}), 400

    index = blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return jsonify({'message': f'Transaction will be added to Block {index}'}), 201
# LLấy dữ liệu từ request (request.get_json()).

# Kiểm tra dữ liệu hợp lệ (cần có "sender", "receiver", "amount").

# Thêm giao dịch vào blockchain (add_transaction()).

# Trả về block mà giao dịch sẽ được thêm vào.

#Trả về toàn bộ blockchain dưới dạng JSON.
@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify({'chain': blockchain.chain}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
