// test-review.js
// File này có nhiều lỗi để test Copilot Review

// Lỗi 1: SQL Injection
function getUser(userId) {
    var query = "SELECT * FROM users WHERE id = " + userId;
    return database.execute(query);
}

// Lỗi 2: Hardcoded secret
const API_KEY = "sk-1234567890abcdef";
const PASSWORD = "admin123";

// Lỗi 3: XSS vulnerability
function displayName(name) {
    document.getElementById('user').innerHTML = name;
}

// Lỗi 4: No error handling
function divide(a, b) {
    return a / b;  // Không check b === 0
}

// Lỗi 5: Using var
var globalCount = 0;

// Lỗi 6: Console.log
function processData(data) {
    console.log("Processing:", data);
    return data.map(x => x * 2);
}

// Lỗi 7: High complexity
function complexFunction(a, b, c, d, e) {
    if (a > 0) {
        if (b > 0) {
            if (c > 0) {
                if (d > 0) {
                    if (e > 0) {
                        return a + b + c + d + e;
                    }
                }
            }
        }
    }
    return 0;
}

// Lỗi 8: Unused variable

// Lỗi 9: No null check
function getName(user) {
    return user.name. toUpperCase();  // user có thể null
}

// Lỗi 10: Eval - nguy hiểm
function runUserCode(code) {
    eval(code);
}

// Lỗi 11: == instead of ===
function checkValue(val) {
    if (val == "123") {
        return true;
    }
    return false;
}

// Lỗi 12: No JSDoc
function calculateTotal(items) {
    return items.reduce((sum, item) => sum + item.price, 0);
}

module.exports = {
    getUser,
    displayName,
    divide,
    processData,
    complexFunction,
    getName,
    runUserCode,
    checkValue,
    calculateTotal
};