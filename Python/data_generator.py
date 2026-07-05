import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta
import os

# ---------------- CONFIGURATION ----------------

fake = Faker("en_IN")

random.seed(42)
np.random.seed(42)
Faker.seed(42)

DATASET_PATH = "../Dataset"

os.makedirs(DATASET_PATH, exist_ok=True)

# ---------------- MASTER DATA ----------------

CATEGORIES = [
    "Staples",
    "Dairy",
    "Beverages",
    "Snacks",
    "Personal Care",
    "Household",
    "Frozen Foods",
    "Bakery",
    "Baby Care",
    "Cleaning Supplies"
]

BRANDS = [
    "Amul",
    "Nestlé",
    "Britannia",
    "Tata",
    "Aashirvaad",
    "Fortune",
    "Parle",
    "Dabur",
    "Patanjali",
    "Haldiram"
]

WAREHOUSE_CITIES = [
    "Delhi",
    "Mumbai",
    "Pune",
    "Bengaluru",
    "Hyderabad",
    "Chennai",
    "Ahmedabad",
    "Jaipur",
    "Lucknow",
    "Kolkata",
    "Bhopal",
    "Indore",
    "Nagpur",
    "Surat",
    "Patna",
    "Chandigarh",
    "Kochi",
    "Bhubaneswar",
    "Guwahati",
    "Visakhapatnam"
]

print("Master Data Loaded Successfully ✅")

PRODUCT_CATALOG = {
    "Staples": [
        "Rice",
        "Wheat Flour",
        "Sugar",
        "Salt",
        "Toor Dal",
        "Moong Dal",
        "Chana Dal",
        "Poha"
    ],

    "Dairy": [
        "Milk",
        "Butter",
        "Paneer",
        "Cheese",
        "Curd",
        "Ghee"
    ],

    "Beverages": [
        "Tea",
        "Coffee",
        "Fruit Juice",
        "Soft Drink",
        "Energy Drink",
        "Mineral Water"
    ],

    "Snacks": [
        "Biscuits",
        "Potato Chips",
        "Namkeen",
        "Instant Noodles",
        "Popcorn",
        "Cookies"
    ],

    "Personal Care": [
        "Shampoo",
        "Soap",
        "Toothpaste",
        "Face Wash",
        "Body Lotion",
        "Hair Oil"
    ],

    "Household": [
        "Detergent Powder",
        "Dishwash Liquid",
        "Floor Cleaner",
        "Toilet Cleaner",
        "Garbage Bags"
    ],

    "Frozen Foods": [
        "Frozen Peas",
        "Frozen Corn",
        "Frozen French Fries",
        "Frozen Veg Mix"
    ],

    "Bakery": [
        "Bread",
        "Cake",
        "Burger Buns",
        "Muffins"
    ],

    "Baby Care": [
        "Baby Diapers",
        "Baby Wipes",
        "Baby Powder",
        "Baby Lotion"
    ],

    "Cleaning Supplies": [
        "Glass Cleaner",
        "Surface Cleaner",
        "Disinfectant Spray",
        "Cleaning Sponge"
    ]
}
PACK_SIZES = [
    "100g", "200g", "500g", "1kg",
    "250ml", "500ml", "1L", "2L"
]

def generate_products(num_products=100):

    products = []

    for product_id in range(1, num_products + 1):

        category = random.choice(list(PRODUCT_CATALOG.keys()))

        product_name = random.choice(PRODUCT_CATALOG[category])

        brand = random.choice(BRANDS)

        size = random.choice(PACK_SIZES)

        unit_cost = round(random.uniform(20, 500), 2)

        selling_price = round(unit_cost * random.uniform(1.10, 1.40), 2)

        shelf_life_days = random.choice([30, 60, 90, 180, 365])

        products.append({
            "product_id": product_id,
            "product_name": f"{brand} {product_name} {size}",
            "category": category,
            "brand": brand,
            "unit_cost": unit_cost,
            "selling_price": selling_price,
            "shelf_life_days": shelf_life_days
        })

    df = pd.DataFrame(products)

    df.to_csv(f"{DATASET_PATH}/products.csv", index=False)

    print(f"✅ {num_products} Products Generated Successfully")

    #generate_products(100)

    