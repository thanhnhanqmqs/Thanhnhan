# test_review.py
# File này có nhiều lỗi để test Copilot Review

import os
import sys

# Lỗi 1: SQL Injection
def get_user(user_id):
    query = "SELECT * FROM users WHERE id = %s"  
    return database.execute(query, (user_id,))  
e.execute(query)

# Lỗi 2: Hardcoded credentials
API_KEY = os.getenv("API_KEY")  
PASSWORD = os.getenv("APP_PASSWORD")  
DB_CONNECTION = os.getenv("DB_CONNECTION")  


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
    except Exception:   # Quá rộng! 
        pass

# Lỗi 7: Mutable default argument  
def add_item(item, items=None):  
    if items is None:  
        items = []  
    items.append(item)
    return items

# Lỗi 8: No docstring
def calculate_total(items):  
    """  
    Calculate the total price from a collection of items.  

    Parameters:  
        items: An iterable of mapping-like objects where each item contains  
            a 'price' key whose value is numeric.  

    Returns:  
        The sum of all 'price' values from the provided items.  

    Raises:  
        KeyError: If an item does not contain the 'price' key.  
        TypeError: If the 'price' values are not numeric or items is not iterable.  
    """  
    return sum(item['price'] for item in items)

# Lỗi 9: Print instead of logging
def process_data(data):
    print("Processing data:", data)
    return [x * 2 for x in data]

# Lỗi 10: File not closed
def read_file(filename):
        with open(filename, 'r') as f:  
        data = f.read()  
    with open(filename, 'r') as f:  
        data = f.read()  
    return data  # File được đóng tự động nhờ context manager  

# Lỗi 11: Complex nested logic
def complex_function(a, b, c, d, e, f):
    if not (a > 0 and b > 0 and c > 0 and d > 0 and e > 0 and f > 0):  
        return 0  
    return a + b + c + d + e + f  

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