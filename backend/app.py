from flask import Flask, jsonify, request
from flask_cors import CORS
from block import Blockchain

app = Flask(__name__)
CORS(app)  # Cho phép frontend kết nối từ cổng 5500
blockchain = Blockchain()

@app.route('/mine', methods=['GET'])
def mine_block():
    previous_block = blockchain.get_previous_block()
    proof = blockchain.proof_of_work(previous_block['proof'])
    previous_hash = blockchain.hash(previous_block)
    block = blockchain.create_block(proof, previous_hash)
    return jsonify({'message': 'Block successfully mined!', 'block': block}), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify({'chain': blockchain.chain, 'length': len(blockchain.chain)}), 200

@app.route('/validate', methods=['GET'])
def validate_chain():
    return jsonify({'valid': blockchain.is_chain_valid()}), 200

@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.get_json()
    required_fields = ['sender', 'receiver', 'amount']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    index = blockchain.add_transaction(data['sender'], data['receiver'], data['amount'])
    return jsonify({'message': f'Transaction added to Block {index}'}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
