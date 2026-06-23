"""
Higher Order Functions Implementation - Shopping Cart System
A practical project demonstrating higher-order functions in Python.
"""

from functools import reduce
from typing import Callable, List, Dict, Any


# ============================================================================
# 1. FUNCTIONS THAT RETURN FUNCTIONS (Function Factories)
# ============================================================================

def create_discount(discount_percent: float) -> Callable:
    """Factory function that creates a discount function."""
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percent / 100)
    return apply_discount


def create_validator(rule: str) -> Callable:
    """Factory function that creates validation functions."""
    def validator(value: Any) -> bool:
        if rule == "positive":
            return value > 0
        elif rule == "email":
            return "@" in str(value)
        elif rule == "non_empty":
            return len(str(value)) > 0
        return False
    return validator


def create_multiplier(factor: float) -> Callable:
    """Create a function that multiplies values by a factor."""
    def multiply(value: float) -> float:
        return value * factor
    return multiply


# ============================================================================
# 2. FUNCTIONS THAT TAKE FUNCTIONS AS ARGUMENTS
# ============================================================================

def apply_operation(operation: Callable, values: List[float]) -> List[float]:
    """Apply a function to each value in a list."""
    return [operation(val) for val in values]


def filter_products(products: List[Dict], filter_func: Callable) -> List[Dict]:
    """Filter products using a custom filter function."""
    return [p for p in products if filter_func(p)]


def calculate_total(products: List[Dict], price_modifier: Callable) -> float:
    """Calculate total price with a price modifier function."""
    return reduce(
        lambda total, price: total + price_modifier(price),
        [p["price"] for p in products],
        0
    )


def sort_by_criteria(items: List, criteria: Callable) -> List:
    """Sort items using a custom criteria function."""
    return sorted(items, key=criteria)


# ============================================================================
# 3. DECORATORS (Higher-Order Functions)
# ============================================================================

def log_transaction(func: Callable) -> Callable:
    """Decorator that logs transaction details."""
    def wrapper(*args, **kwargs):
        print(f"🔵 Executing: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Completed: {func.__name__}")
        return result
    return wrapper


def apply_tax(tax_rate: float) -> Callable:
    """Decorator factory that applies tax to a function's result."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * (1 + tax_rate / 100)
        return wrapper
    return decorator


# ============================================================================
# 4. PRODUCT OPERATIONS
# ============================================================================

def create_product(name: str, price: float, category: str) -> Dict:
    """Create a product dictionary."""
    return {"name": name, "price": price, "category": category}


@log_transaction
def process_order(products: List[Dict], discount_func: Callable) -> Dict:
    """Process an order with a discount function."""
    subtotal = sum(p["price"] for p in products)
    total = discount_func(subtotal)
    return {
        "items": len(products),
        "subtotal": subtotal,
        "total": total,
        "saved": subtotal - total
    }


# ============================================================================
# 5. MAIN DEMO
# ============================================================================

def main():
    print("=" * 60)
    print("🛒 SHOPPING CART SYSTEM - Higher Order Functions Demo")
    print("=" * 60)
    
    # Sample products
    products = [
        create_product("Laptop", 1000, "Electronics"),
        create_product("Mouse", 30, "Electronics"),
        create_product("Keyboard", 80, "Electronics"),
        create_product("Monitor", 300, "Electronics"),
        create_product("USB Cable", 15, "Accessories"),
    ]
    
    print("\n📦 Available Products:")
    for i, p in enumerate(products, 1):
        print(f"   {i}. {p['name']}: ${p['price']}")
    
    # -------- DEMO 1: Function Factories --------
    print("\n" + "=" * 60)
    print("Demo 1: Function Factories (create_discount)")
    print("=" * 60)
    
    discount_10 = create_discount(10)
    discount_20 = create_discount(20)
    
    original_price = 100
    print(f"Original Price: ${original_price}")
    print(f"With 10% Discount: ${discount_10(original_price)}")
    print(f"With 20% Discount: ${discount_20(original_price)}")
    
    # -------- DEMO 2: Apply Function to List --------
    print("\n" + "=" * 60)
    print("Demo 2: Apply Operation (map-like behavior)")
    print("=" * 60)
    
    prices = [100, 200, 50, 150]
    double_prices = apply_operation(create_multiplier(2), prices)
    print(f"Original prices: {prices}")
    print(f"Doubled prices: {double_prices}")
    
    # -------- DEMO 3: Filtering --------
    print("\n" + "=" * 60)
    print("Demo 3: Filter with Custom Functions")
    print("=" * 60)
    
    expensive = filter_products(products, lambda p: p["price"] > 100)
    electronics = filter_products(products, lambda p: p["category"] == "Electronics")
    
    print(f"\nExpensive Items (> $100):")
    for p in expensive:
        print(f"   - {p['name']}: ${p['price']}")
    
    print(f"\nElectronics Category:")
    for p in electronics:
        print(f"   - {p['name']}: ${p['price']}")
    
    # -------- DEMO 4: Sorting with Criteria --------
    print("\n" + "=" * 60)
    print("Demo 4: Sorting with Custom Criteria")
    print("=" * 60)
    
    sorted_by_price = sort_by_criteria(products, lambda p: p["price"])
    print("\nProducts sorted by price (ascending):")
    for p in sorted_by_price:
        print(f"   - {p['name']}: ${p['price']}")
    
    # -------- DEMO 5: Validators --------
    print("\n" + "=" * 60)
    print("Demo 5: Validator Functions")
    print("=" * 60)
    
    is_positive = create_validator("positive")
    is_email = create_validator("email")
    
    test_values = [100, -50, 0]
    print(f"\nValidator Results (positive check):")
    for val in test_values:
        print(f"   {val} is positive: {is_positive(val)}")
    
    emails = ["user@email.com", "invalid", "test@domain.org"]
    print(f"\nValidator Results (email check):")
    for email in emails:
        print(f"   {email} is email: {is_email(email)}")
    
    # -------- DEMO 6: Processing Orders --------
    print("\n" + "=" * 60)
    print("Demo 6: Process Order with Discount Function")
    print("=" * 60)
    
    selected_products = products[:3]  # Laptop, Mouse, Keyboard
    
    order = process_order(selected_products, discount_20)
    print(f"\nOrder Summary:")
    print(f"   Items: {order['items']}")
    print(f"   Subtotal: ${order['subtotal']}")
    print(f"   Total (20% off): ${order['total']}")
    print(f"   You saved: ${order['saved']}")
    
    # -------- DEMO 7: Chaining Functions --------
    print("\n" + "=" * 60)
    print("Demo 7: Chaining Higher-Order Functions")
    print("=" * 60)
    
    # Get expensive electronics, sort by price
    result = sort_by_criteria(
        filter_products(products, lambda p: p["category"] == "Electronics" and p["price"] > 50),
        lambda p: p["price"]
    )
    
    print(f"\nExpensive Electronics (> $50), sorted by price:")
    for p in result:
        print(f"   - {p['name']}: ${p['price']}")
    
    # -------- DEMO 8: Reduce (Advanced) --------
    print("\n" + "=" * 60)
    print("Demo 8: Reduce Operation")
    print("=" * 60)
    
    total_inventory_value = reduce(lambda acc, p: acc + p["price"], products, 0)
    print(f"\nTotal Inventory Value: ${total_inventory_value}")
    
    print("\n" + "=" * 60)
    print("✨ Higher-Order Functions Demo Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
