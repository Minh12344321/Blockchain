import hashlib
import json

from blockchain import Blockchain

def hash_data(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()
#json.dumps(data, sort_keys=True): Chuyển đổi dữ liệu Python (dict, list, v.v.) sang chuỗi JSON có thứ tự khóa cố định để đảm bảo dữ liệu đầu vào luôn được băm một cách nhất quán.

# .encode(): Chuyển đổi chuỗi JSON thành dạng bytes, cần thiết để dùng thuật toán băm.

# hashlib.sha256(...).hexdigest(): Tạo mã băm SHA-256 và chuyển kết quả thành chuỗi hex.