// test-review.js
// File này có nhiều lỗi để test Copilot Review

// Fixed: SQL Injection - Using parameterized query
function getUser(userId) {
    var query = "SELECT * FROM users WHERE id = ?";
    return database.execute(query, [userId]);
}

// Fixed: Hardcoded secret - Using environment variables
const API_KEY = process.env.API_KEY;
const PASSWORD = process.env.PASSWORD;

// Fixed: XSS vulnerability - Using textContent instead of innerHTML
function displayName(name) {
    document.getElementById('user').textContent = name;
}

// Fixed: No error handling - Added check for division by zero
function divide(a, b) {
    if (b === 0) {
        throw new Error('Division by zero');
    }
    return a / b;
}

// Fixed: Using var - Changed to let
let globalCount = 0;

// Fixed: Console.log - Removed console.log
function processData(data) {
    return data.map(x => x * 2);
}

// Fixed: High complexity - Simplified logic
function complexFunction(a, b, c, d, e) {
    if (a > 0 && b > 0 && c > 0 && d > 0 && e > 0) {
        return a + b + c + d + e;
    }
    return 0;
}

// Fixed: Unused variable - Removed unused variable

// Fixed: No null check - Added null/undefined check
function getName(user) {
    if (!user || !user.name) {
        throw new Error('User or user name is null/undefined');
    }
    return user.name.toUpperCase();
}

// Fixed: Eval - Replaced with safer Function constructor (or remove entirely)
function runUserCode(code) {
    // Eval is dangerous and should not be used
    // If you need to execute user code, use a sandboxed environment
    throw new Error('Executing user code is not allowed for security reasons');
}

// Fixed: == instead of === - Using strict equality
function checkValue(val) {
    if (val === "123") {
        return true;
    }
    return false;
}

// Fixed: No JSDoc - Added JSDoc documentation
/**
 * Calculates the total price of all items
 * @param {Array<{price: number}>} items - Array of items with price property
 * @returns {number} The total sum of all item prices
 */
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