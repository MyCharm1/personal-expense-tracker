import json
import os
from datetime import datetime

DATA_FILE = "expenses.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(expenses):
    with open(DATA_FILE, "w") as f:
        json.dump(expenses, f, indent=4)

def add_expense(expenses):
    amount = float(input("Enter amount ($): "))
    category = input("Enter category (e.g., Food, Transport, Rent): ").strip().title()
    description = input("Enter note/description: ").strip()
    date_str = datetime.now().strftime("%Y-%m-%d %H:%M")

    record = {
        "id": len(expenses) + 1,
        "amount": amount,
        "category": category,
        "description": description,
        "date": date_str
    }
    expenses.append(record)
    save_data(expenses)
    print(f"\n[+] Added ${amount:.2f} under '{category}'.\n")

def view_expenses(expenses):
    if not expenses:
        print("\n[!] No expenses recorded yet.\n")
        return

    print("\n" + "=" * 60)
    print(f"{'ID':<5} | {'Date':<16} | {'Category':<12} | {'Amount':<8} | {'Description'}")
    print("=" * 60)
    total = 0.0
    for item in expenses:
        total += item["amount"]
        print(f"{item['id']:<5} | {item['date']:<16} | {item['category']:<12} | ${item['amount']:<7.2f} | {item['description']}")
    print("=" * 60)
    print(f"Total Spent: ${total:.2f}\n")

def view_summary(expenses):
    if not expenses:
        print("\n[!] No expenses recorded yet.\n")
        return

    categories = {}
    total = 0.0
    for item in expenses:
        cat = item["category"]
        categories[cat] = categories.get(cat, 0.0) + item["amount"]
        total += item["amount"]

    print("\n--- Expense Summary by Category ---")
    for cat, amt in categories.items():
        percentage = (amt / total) * 100
        print(f"{cat:<15}: ${amt:<8.2f} ({percentage:.1f}%)")
    print(f"Total: ${total:.2f}\n")

def main():
    expenses = load_data()
    while True:
        print("--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Category Summary")
        print("4. Exit")
        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_summary(expenses)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("[!] Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()