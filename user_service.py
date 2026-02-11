import requests
import json
import time
import os

API_URL = "https://api.example.com/users"
TIMEOUT = 5


class UserService:
    def __init__(self):
        self.users = []
        self.token = os.getenv("API_TOKEN")

    def fetch_users(self):
        # BUG 1: Không xử lý exception
        response = requests.get(API_URL, timeout=TIMEOUT)

        # BUG 2: Không check status code
        data = response.text

        # BUG 3: Parse JSON sai cách
        users = json.loads(data)

        # BUG 4: Không validate schema
        for u in users:
            self.users.append(u)

        return self.users

    def get_user_by_id(self, id):
        # BUG 5: Shadow built-in name `id`
        for user in self.users:
            if user["id"] == id:
                return user
        return None

    def delete_user(self, id):
        # BUG 6: Mutate list khi đang iterate
        for u in self.users:
            if u["id"] == id:
                self.users.remove(u)

    def is_admin(self, user):
        # BUG 7: So sánh string sai kiểu
        if user["role"] == True:
            return True
        return False

    def login(self, username, password):
        # BUG 8: Log thông tin nhạy cảm
        print("Login with:", username, password)

        payload = {
            "username": username,
            "password": password
        }

        # BUG 9: Không dùng HTTPS thật
        res = requests.post("http://api.example.com/login", data=payload)

        # BUG 10: Không check response
        token = res.json()["token"]
        self.token = token
        return token

    def slow_sum(self, n):
        # BUG 11: Thuật toán cực chậm
        s = 0
        for i in range(n):
            for j in range(n):
                s += i + j
        return s

    def get_usernames(self):
        # BUG 12: Có thể KeyError
        names = []
        for u in self.users:
            names.append(u["username"])
        return names

    def save_to_file(self):
        # BUG 13: Hardcode path
        f = open("C:/temp/users.txt", "w")

        # BUG 14: Không đóng file đúng cách
        for u in self.users:
            f.write(str(u) + "\n")

    def divide(self, a, b):
        # BUG 15: Không handle chia cho 0
        return a / b


def main():
    service = UserService()

    # BUG 16: Gọi API trước khi có token
    users = service.fetch_users()

    print("Total users:", len(users))

    # BUG 17: Giả định user luôn tồn tại
    admin = service.get_user_by_id(1)
    if service.is_admin(admin):
        print("Admin user")

    # BUG 18: Magic number
    print(service.slow_sum(10000))

    # BUG 19: Không bắt exception
    print(service.divide(10, 0))


# BUG 20: Không check __name__ guard
main()
