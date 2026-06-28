from typing import Dict

# -----------------------------
# PRODUCTS DATABASE
# -----------------------------

PRODUCTS: Dict[str, Dict] = {

    "P101": {
        "product_id": "P101",
        "name": "Nike Air Max",
        "category": "Shoes",
        "price": 7999,
        "stock": 15,
        "rating": 4.7
    },

    "P102": {
        "product_id": "P102",
        "name": "Adidas Ultraboost",
        "category": "Shoes",
        "price": 6999,
        "stock": 22,
        "rating": 4.6
    },

    "P103": {
        "product_id": "P103",
        "name": "Puma Runner",
        "category": "Shoes",
        "price": 4999,
        "stock": 18,
        "rating": 4.5
    },

    "P104": {
        "product_id": "P104",
        "name": "Campus Running Shoes",
        "category": "Shoes",
        "price": 2999,
        "stock": 31,
        "rating": 4.3
    },

    "P105": {
        "product_id": "P105",
        "name": "Boat Rockerz 550",
        "category": "Headphones",
        "price": 1999,
        "stock": 40,
        "rating": 4.4
    },

    "P106": {
        "product_id": "P106",
        "name": "Sony WH-CH520",
        "category": "Headphones",
        "price": 4499,
        "stock": 20,
        "rating": 4.8
    },

    "P107": {
        "product_id": "P107",
        "name": "Apple AirPods 4",
        "category": "Earbuds",
        "price": 12999,
        "stock": 8,
        "rating": 4.9
    },

    "P108": {
        "product_id": "P108",
        "name": "Samsung Galaxy Buds FE",
        "category": "Earbuds",
        "price": 5999,
        "stock": 12,
        "rating": 4.7
    }

}

# -----------------------------
# ORDERS DATABASE
# -----------------------------

ORDERS: Dict[str, Dict] = {

    "ORD-1001": {
        "order_id": "ORD-1001",
        "customer": "Rahul Sharma",
        "product_id": "P101",
        "status": "Delivered",
        "tracking_location": "Delivered to Customer",
        "delivery_date": "24 June 2026"
    },

    "ORD-1002": {
        "order_id": "ORD-1002",
        "customer": "Harsh Agarwal",
        "product_id": "P102",
        "status": "In Transit",
        "tracking_location": "Jaipur Hub",
        "delivery_date": "29 June 2026"
    },

    "ORD-1003": {
        "order_id": "ORD-1003",
        "customer": "Amit",
        "product_id": "P106",
        "status": "Packed",
        "tracking_location": "Delhi Warehouse",
        "delivery_date": "30 June 2026"
    }
}
