from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class Wallet:
    def __init__(self):
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
#     Tạo cặp khóa RSA (2048-bit) dùng để bảo mật giao dịch.

# private_key: Khóa bí mật của ví, được sử dụng để ký giao dịch.

# public_key: Khóa công khai, dùng để xác minh chữ ký.

    def sign_transaction(self, transaction):
        transaction_data = str(transaction).encode()
        signature = self.private_key.sign(
            transaction_data,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return signature
#     Nhận dữ liệu giao dịch, chuyển thành bytes.

# Ký giao dịch bằng khóa riêng tư với thuật toán SHA-256 và cơ chế PSS padding.

# Trả về chữ ký số của giao dịch.
    

    def verify_signature(self, transaction, signature):
        transaction_data = str(transaction).encode()
        try:
            self.public_key.verify(
                signature,
                transaction_data,
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
            return True
        except:
            return False
# Kiểm tra xem chữ ký có hợp lệ không bằng khóa công khai.

# Nếu chữ ký đúng với dữ liệu giao dịch → Trả về True, ngược lại False.

    def get_public_key(self):
        return self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ).decode()


# Chuyển khóa công khai thành dạng PEM (chuẩn lưu trữ khóa).

# Trả về khóa công khai dưới dạng string để có thể chia sẻ với người khác.