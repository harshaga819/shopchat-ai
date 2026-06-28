from typing import Dict, List
from database import PRODUCTS, ORDERS


def get_order(order_id: str) -> Dict:
    """Fetch order details using an order ID."""
    order = ORDERS.get(order_id.upper())
    if not order:
        return {"success": False, "message": "Order not found."}
    return {"success": True, "data": order}


def get_product(product_id: str) -> Dict:
    """Fetch product details using a product ID."""
    product = PRODUCTS.get(product_id.upper())
    if not product:
        return {"success": False, "message": "Product not found."}
    return {"success": True, "data": product}


def search_products(query: str) -> Dict:
    """Search products by keyword (matches against name or category)."""
    query = query.lower().strip()
    results: List[Dict] = []
    for product in PRODUCTS.values():
        if query in product["name"].lower() or query in product["category"].lower():
            results.append(product)
    if not results:
        return {"success": False, "message": "No products found."}
    return {"success": True, "count": len(results), "data": results}


if __name__ == "__main__":
    print(get_order("ORD-1002"))
    print()
    print(get_product("P102"))
    print()
    print(search_products("Shoes"))