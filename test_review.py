# test_review.py
# File này có nhiều lỗi để test Copilot Review

import os
import sys

# Lỗi 1: SQL Injection
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = " + str(user_id)
    return database.execute(query)

# Lỗi 2: Hardcoded credentials
API_KEY = "sk-1234567890abcdef"
PASSWORD = "admin123"
DB_CONNECTION = "postgresql://admin:password@localhost/db"

# Lỗi 3: Eval - nguy hiểm
def run_user_code(code):
    eval(code)

# Lỗi 4: No error handling
def divide(a, b):
    return a / b  # Không check b == 0

# Lỗi 5: Unused imports
import json
import hashlib

# Lỗi 6: Bare except
def risky_operation():
    try:
        # some code
        pass
    except:   # Quá rộng! 
        pass

# L��i 7: Mutable default argument
def add_item(item, items=[]):
    items.append(item)
    return items

# Lỗi 8: No docstring
def calculate_total(items):
    return sum(item['price'] for item in items)

# Lỗi 9: Print instead of logging
def process_data(data):
    print("Processing data:", data)
    return [x * 2 for x in data]

# Lỗi 10: File not closed
def read_file(filename):
    f = open(filename, 'r')
    data = f.read()
    return data  # File không được close! 

# Lỗi 11: Complex nested logic
def complex_function(a, b, c, d, e, f):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        if f > 0:
                            return a + b + c + d + e + f
    return 0

# Lỗi 12: Global variable modification
counter = 0
def increment():
    global counter
    counter += 1

# Lỗi 13: No type hints
def add_numbers(a, b):
    return a + b

# Lỗi 14: String concatenation in loop (inefficient)
def build_string(items):
    result = ""
    for item in items:
        result += str(item) + ","
    return result