import datetime
import json

class ExpenseTracker:
    def __init__(self):
        self.expenses = {}

    def add_expense(self):
        amount = float(input("Enter the amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter the category (e.g., food, transportation, entertainment): ")
        date = datetime.date.today().strftime("%Y-%m-%d")

        if date not in self.expenses:
            self.expenses[date] = []

        self.expenses[date].append({
            "amount": amount,
            "description": description,
            "category": category
        })

        self.save_expenses()

    def view_expenses(self):
        date = input("Enter the date (YYYY-MM-DD) or 'all' to view all expenses: ")

        if date == 'all':
            for date, expenses in self.expenses.items():
                print(f"Expenses for {date}:")
                for expense in expenses:
                    print(f"  - {expense['description']}: ${expense['amount']} ({expense['category']})")
        elif date in self.expenses:
            print(f"Expenses for {date}:")
            for expense in self.expenses[date]:
                print(f"  - {expense['description']}: ${expense['amount']} ({expense['category']})")
        else:
            print("No expenses found for the given date.")

    def view_summary(self):
        date = input("Enter the date (YYYY-MM-DD) or 'all' to view summary: ")

        if date == 'all':
            total = 0
            categories = {}
            for date, expenses in self.expenses.items():
                for expense in expenses:
                    total += expense['amount']
                    if expense['category'] not in categories:
                        categories[expense['category']] = 0
                    categories[expense['category']] += expense['amount']

            print(f"Total expenses: ${total}")
            for category, amount in categories.items():
                print(f"  - {category}: ${amount}")
        elif date in self.expenses:
            total = 0
            categories = {}
            for expense in self.expenses[date]:
                total += expense['amount']
                if expense['category'] not in categories:
                    categories[expense['category']] = 0
                categories[expense['category']] += expense['amount']

            print(f"Total expenses for {date}: ${total}")
            for category, amount in categories.items():
                print(f"  - {category}: ${amount}")
        else:
            print("No expenses found for the given date.")

    def save_expenses(self):
        with open('expenses.json', 'w') as f:
            json.dump(self.expenses, f)

    def load_expenses(self):
        try:
            with open('expenses.json', 'r') as f:
                self.expenses = json.load(f)
        except FileNotFoundError:
            pass

def main():
    tracker = ExpenseTracker()
    tracker.load_expenses()

    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Summary")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            tracker.add_expense()
        elif choice == '2':
            tracker.view_expenses()
        elif choice == '3':
            tracker.view_summary()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()