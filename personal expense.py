# personal expense tracker

expenses = []  # list to store all expense dicts
budget = 0.0   # monthly budget set at start

# valid expense categories
CATEGORIES = {"food", "travel", "bills", "entertainment", "others"}


def set_budget():
    global budget
    while True:
        try:
            value = float(input("Enter your monthly budget (Rs): "))
            if value <= 0:
                print("Budget has to be more than 0")
                continue
            budget = value
            break
        except ValueError:
            print("Please enter a valid number")


def validate_amount(prompt):
    # keep asking till we get a valid positive amount
    while True:
        try:
            amt = float(input(prompt))
            if amt <= 0:
                print("Amount should be greater than 0")
            else:
                return amt
        except ValueError:
            print("That's not a number, try again")


def add_expense():
    print("\n==== Add New Expense ====")

    desc = input("Description: ").strip()
    if desc == "":
        print("Description can't be empty")
        return

    print("Categories:", ", ".join(CATEGORIES))
    cat = input("Category: ").strip().lower()

    if cat not in CATEGORIES:
        print(f"'{cat}' not recognized, saving as 'others'")
        cat = "others"

    amount = validate_amount("Amount (Rs): ")
    date = input("Date (DD-MM-YYYY): ").strip()

    # Date format validation is not implemented yet

    expense = {
        "desc": desc,
        "category": cat,
        "amount": amount,
        "date": date
    }

    expenses.append(expense)

    total = sum(e["amount"] for e in expenses)
    print(f"Expense added! Total spent so far: Rs. {total:.2f}")


def view_expenses():
    if len(expenses) == 0:
        print("No expenses added yet")
        return

    print("\n==== All Expenses ====")
    print(f"{'No.':<5} {'Description':<20} {'Category':<15} {'Amount':>10} {'Date':<12}")
    print("-" * 65)

    for i, e in enumerate(expenses):
        print(
            f"{i+1:<5} {e['desc']:<20} {e['category']:<15} Rs.{e['amount']:>8.2f} {e['date']:<12}"
        )


def category_summary():
    if not expenses:
        print("No data to show")
        return

    summary = {}

    for e in expenses:
        cat = e["category"]

        if cat in summary:
            summary[cat] += e["amount"]
        else:
            summary[cat] = e["amount"]

    print("\n==== Category Summary ====")

    for cat, total in summary.items():
        print(f"{cat:<15} : Rs. {total:.2f}")

    # also show unique categories using a set
    unique_cats = set(e["category"] for e in expenses)
    print(f"\nUnique categories used: {unique_cats}")


def get_top_category():
    # returns the category where most money was spent

    if not expenses:
        return None, 0

    summary = {}

    for e in expenses:
        cat = e["category"]
        summary[cat] = summary.get(cat, 0) + e["amount"]

    top_cat = max(summary, key=summary.get)

    return top_cat, summary[top_cat]


def budget_report():
    if not expenses:
        print("No expenses to report on")
        return

    total_spent = sum(e["amount"] for e in expenses)
    remaining = budget - total_spent

    if budget > 0:
        percent_used = (total_spent / budget) * 100
    else:
        percent_used = 0

    top_cat, top_amt = get_top_category()

    print("\n==== Budget Report ====")
    print(f"Total Spent  : Rs. {total_spent:.2f}")
    print(f"Budget Limit : Rs. {budget:.2f}")
    print(f"Remaining    : Rs. {remaining:.2f}")
    print(f"Used         : {percent_used:.2f}%")

    if percent_used >= 100:
        print("ALERT: You have exceeded your budget!")
    elif percent_used >= 80:
        print(f"WARNING: You have used {percent_used:.0f}% of your budget!")
    else:
        print("You are within budget, good job.")

    if top_cat:
        print(f"Top Category : {top_cat} (Rs. {top_amt:.2f})")


def show_menu():
    print("\n======= PERSONAL EXPENSE TRACKER =======")
    print(f"Monthly Budget: Rs. {budget:.2f}")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Category Summary")
    print("4. Budget Report")
    print("5. Exit")


# main program starts here

print("Welcome to Personal Expense Tracker")
set_budget()

while True:
    show_menu()

    try:
        choice = int(input("Choice: "))
    except ValueError:
        print("Enter a number between 1 and 5")
        continue

    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        category_summary()
    elif choice == 4:
        budget_report()
    elif choice == 5:
        print("Exiting... Bye!")
        break
    else:
        print("Invalid choice, pick 1 to 5")