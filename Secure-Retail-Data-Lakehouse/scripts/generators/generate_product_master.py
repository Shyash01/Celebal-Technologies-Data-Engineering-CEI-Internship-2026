import os
import pandas as pd

products = [
    ["P001", "Laptop", "Electronics", 40000, 90000],
    ["P002", "Smartphone", "Electronics", 12000, 80000],
    ["P003", "Tablet", "Electronics", 15000, 60000],
    ["P004", "Smartwatch", "Electronics", 3000, 25000],
    ["P005", "Headphones", "Electronics", 1000, 15000],

    ["P006", "T-Shirt", "Clothing", 300, 1500],
    ["P007", "Jeans", "Clothing", 800, 3500],
    ["P008", "Jacket", "Clothing", 1500, 6000],
    ["P009", "Hoodie", "Clothing", 800, 4000],
    ["P010", "Sneakers", "Clothing", 1500, 8000],

    ["P011", "Rice", "Grocery", 50, 500],
    ["P012", "Wheat Flour", "Grocery", 40, 400],
    ["P013", "Cooking Oil", "Grocery", 100, 1000],
    ["P014", "Sugar", "Grocery", 40, 300],
    ["P015", "Tea", "Grocery", 80, 800],

    ["P016", "Mixer Grinder", "Home & Kitchen", 2000, 8000],
    ["P017", "Cookware Set", "Home & Kitchen", 1500, 12000],
    ["P018", "Water Bottle", "Home & Kitchen", 200, 1000],
    ["P019", "Vacuum Cleaner", "Home & Kitchen", 5000, 18000],
    ["P020", "Dining Set", "Home & Kitchen", 5000, 25000],

    ["P021", "Cricket Bat", "Sports", 500, 6000],
    ["P022", "Football", "Sports", 300, 2500],
    ["P023", "Yoga Mat", "Sports", 500, 3000],
    ["P024", "Dumbbells", "Sports", 1000, 10000],
    ["P025", "Running Shoes", "Sports", 1500, 12000],

    ["P026", "Face Wash", "Beauty", 150, 800],
    ["P027", "Shampoo", "Beauty", 200, 1200],
    ["P028", "Perfume", "Beauty", 800, 6000],
    ["P029", "Sunscreen", "Beauty", 300, 2000],
    ["P030", "Lipstick", "Beauty", 200, 2500],

    ["P031", "Novel", "Books", 250, 1000],
    ["P032", "Python Programming", "Books", 400, 1500],
    ["P033", "SQL Guide", "Books", 350, 1200],
    ["P034", "Data Science Handbook", "Books", 500, 1800],
    ["P035", "Biography", "Books", 300, 1200],

    ["P036", "Puzzle", "Toys", 300, 1500],
    ["P037", "Building Blocks", "Toys", 500, 4000],
    ["P038", "Toy Car", "Toys", 300, 2500],
    ["P039", "Teddy Bear", "Toys", 400, 3000],
    ["P040", "Board Game", "Toys", 500, 3500],
]

columns = [
    "product_id",
    "product_name",
    "category",
    "min_price",
    "max_price",
]

product_df = pd.DataFrame(products, columns=columns)

os.makedirs("master_data", exist_ok=True)

output_path = os.path.join("master_data", "product_master.csv")
product_df.to_csv(output_path, index=False)

print("Product master dataset created successfully.")
print(f"Location: {output_path}")
print(f"Total Products: {len(product_df)}")