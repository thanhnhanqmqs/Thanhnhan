# order_service.py
# File này cố tình chứa rất nhiều lỗi để test AI review

import threading
import sqlite3
import time
import pickle

DB_PATH = "orders.db"
SECRET_KEY = "super-secret-key"  # BUG 1: Hardcoded secret


class OrderService:
    def __init__(self):
        self.orders = []
        self.lock = threading.Lock()

    def connect_db(self):
        # BUG 2: Không dùng context manager
        conn = sqlite3.connect(DB_PATH)
        return conn

    def create_order(self, user_id, amount):
        # BUG 3: SQL Injection
        query = f"INSERT INTO orders VALUES ({user_id}, {amount})"
        conn = self.connect_db()
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        conn.close()

        order = {
            "user_id": user_id,
            "amount": amount,
            "created_at": time.time()
        }
        self.orders.append(order)
        return order

    def get_total_amount(self):
        # BUG 4: Race condition (không lock)
        total = 0
        for o in self.orders:
            total += o["amount"]
        return total

    def delete_order(self, user_id):
        # BUG 5: Modify list khi đang iterate
        for o in self.orders:
            if o["user_id"] == user_id:
                self.orders.remove(o)

    def load_from_file(self, filename):
        # BUG 6: Insecure deserialization
        with open(filename, "rb") as f:
            data = pickle.load(f)
        self.orders = data

    def save_to_file(self, filename):
        # BUG 7: Ghi file không validate path
        f = open(filename, "wb")
        pickle.dump(self.orders, f)
        # BUG 8: Không close file

    def get_order_by_index(self, index):
        # BUG 9: Không check index range
        return self.orders[index]

    def divide_amount(self, order_index, divisor):
        # BUG 10: Chia cho 0
        order = self.get_order_by_index(order_index)
        return order["amount"] / divisor

    def slow_statistics(self):
        # BUG 11: Thuật toán O(n^2) vô nghĩa
        stats = []
        for i in range(len(self.orders)):
            for j in range(len(self.orders)):
                stats.append(self.orders[i]["amount"] + self.orders[j]["amount"])
        return stats

    def print_orders(self):
        # BUG 12: Log dữ liệu nhạy cảm
        for o in self.orders:
            print("ORDER:", o)

    def get_user_orders(self, user_id):
        # BUG 13: Không dùng list comprehension + KeyError
        result = []
        for o in self.orders:
            if o["user_id"] == user_id:
                result.append(o["amount"])
        return result


# BUG 14: Global mutable state
service = OrderService()


def worker():
    # BUG 15: Dùng shared state không lock
    for i in range(10):
        service.create_order(i, i * 100)


def main():
    # BUG 16: Tạo nhiều thread nhưng không join
    threads = []
    for i in range(5):
        t = threading.Thread(target=worker)
        t.start()
        threads.append(t)

    # BUG 17: Giả định dữ liệu đã sẵn sàng
    print("Total:", service.get_total_amount())

    # BUG 18: Magic number
    print(service.divide_amount(0, 0))

    # BUG 19: Không try/except
    service.load_from_file("orders.pkl")


# BUG 20: Không có __name__ guard
main()
