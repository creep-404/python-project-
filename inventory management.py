inventory = {}
transaction_log = []

try:
    f = open("inventory.txt", "r")
    for line in f:
        parts = line.strip().split(",")
        inventory[parts[0]] = {
            "name": parts[1],
            "category": parts[2],
            "price": float(parts[3]),
            "quantity": int(parts[4]),
            "reorder": int(parts[5])
        }
    f.close()
    print(f"{len(inventory)} products loaded!")
except FileNotFoundError:
    print("No saved data found, starting fresh")

def add_product():
    pid = input("Product ID: ").strip().upper()
    if pid in inventory:
        print("ID already exists!")
        return
    name = input("Name: ").strip()
    cat = input("Category: ").strip()
    try:
        price = float(input("Price: "))
        qty = int(input("Quantity: "))
        reorder = int(input("Reorder Level: "))
    except ValueError:
        print("Invalid input!")
        return
    inventory[pid] = {"name": name, "category": cat, "price": price, "quantity": qty, "reorder": reorder}
    print(f"{name} added!")

def stock_in():
    pid = input("Product ID: ").strip().upper()
    if pid not in inventory:
        print("Product not found!")
        return
    try:
        qty = int(input("Units to add: "))
    except ValueError:
        print("Invalid!")
        return
    inventory[pid]["quantity"] += qty
    transaction_log.append(f"IN | {pid} | {inventory[pid]['name']} | {qty} units")
    print(f"Done! New qty: {inventory[pid]['quantity']}")

def stock_out():
    pid = input("Product ID: ").strip().upper()
    if pid not in inventory:
        print("Product not found!")
        return
    try:
        qty = int(input("Units to remove: "))
    except ValueError:
        print("Invalid!")
        return
    if qty > inventory[pid]["quantity"]:
        print(f"Not enough stock! Only {inventory[pid]['quantity']} available")
        return
    inventory[pid]["quantity"] -= qty
    transaction_log.append(f"OUT | {pid} | {inventory[pid]['name']} | {qty} units")
    print(f"Done! Remaining qty: {inventory[pid]['quantity']}")

def view_inventory():
    if not inventory:
        print("No products!")
        return
    print(f"\n{'ID':<8} {'Name':<20} {'Category':<15} {'Price':>8} {'Qty':>5} {'Reorder':>8}")
    print("-" * 65)
    for pid, p in inventory.items():
        print(f"{pid:<8} {p['name']:<20} {p['category']:<15} {p['price']:>8.2f} {p['quantity']:>5} {p['reorder']:>8}")
    total = sum(p["price"] * p["quantity"] for p in inventory.values())
    print(f"\nTotal Value: Rs. {total:.2f}")

def low_stock():
    print("--- Low Stock Alert ---")
    found = False
    for pid, p in inventory.items():
        if p["quantity"] <= p["reorder"]:
            print(f"[LOW] {pid} - {p['name']} | Qty: {p['quantity']} | Reorder: {p['reorder']}")
            found = True
    if not found:
        print("All stock levels are fine!")

def report():
    if not inventory:
        print("No data!")
        return
    total_value = sum(p["price"] * p["quantity"] for p in inventory.values())
    categories = set(p["category"] for p in inventory.values())
    low = sum(1 for p in inventory.values() if p["quantity"] <= p["reorder"])
    top = max(inventory, key=lambda x: inventory[x]["price"] * inventory[x]["quantity"])

    print("======= INVENTORY REPORT =======")
    print(f"Total Products : {len(inventory)}")
    print(f"Total Value    : Rs. {total_value:.2f}")
    print(f"Categories     : {', '.join(categories)}")
    print(f"Low Stock Items: {low}")
    print(f"Top Product    : {inventory[top]['name']}")

    if transaction_log:
        print("--- Transaction Log ---")
        for t in transaction_log:
            print(f"  {t}")

print("===== INVENTORY MANAGEMENT SYSTEM =====")

while True:
    print("1.Add  2.Stock In  3.Stock Out  4.View  5.Low Stock  6.Report  7.Exit")
    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("enter a number!")
        continue

    if choice == 1:
        add_product()
    elif choice == 2:
        stock_in()
    elif choice == 3:
        stock_out()
    elif choice == 4:
        view_inventory()
    elif choice == 5:
        low_stock()
    elif choice == 6:
        report()
    elif choice == 7:
        f = open("inventory.txt", "w")
        for pid, p in inventory.items():
            f.write(f"{pid},{p['name']},{p['category']},{p['price']},{p['quantity']},{p['reorder']}\n")
        f.close()
        print("Saved! Bye!")
        break
    else:
        print("pick 1 to 7!")
