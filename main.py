from datetime import datetime
import json
import os


class expenseTeacker():
    def __init__(self):
        self.id = 0
        self.expenses = []

        if os.path.exists("expenses.json"):
            with open("expenses.json", "r") as file:
                self.expenses = json.load(file)

            if self.expenses:
                self.id = max(expense["id"] for expense in self.expenses)

    def add_expense(self, expense_data):
        self.id += 1
        expense_data['id'] = self.id
        self.expenses.append(expense_data)

        with open("expenses.json", "w") as file:
            json.dump(self.expenses, file, indent=4)

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return

        for expense in self.expenses:
            print(
                f"{expense['id']} \t | "
                f"{expense['title']} \t | "
                f"{expense['category']} \t | "
                f"{expense['amount']} EGP"
            )

    def search_expense(self, search):
        for expense in self.expenses:
            if search.lower() in expense['title'].lower():
                print(
                    f"{expense['id']} \t | "
                    f"{expense['title']} \t | "
                    f"{expense['category']} \t | "
                    f"{expense['amount']} EGP"
                )

    def filter_expenses(self, filter):
        for expense in self.expenses:
            if filter.lower() in expense['category'].lower():
                print(
                    f"{expense['id']} \t | "
                    f"{expense['title']} \t | "
                    f"{expense['category']} \t | "
                    f"{expense['amount']} EGP"
                )

    def delete_expense(self, expense_id):
        for expense in self.expenses:
            if expense['id'] == expense_id:
                self.expenses.remove(expense)

                with open("expenses.json", "w") as file:
                    json.dump(self.expenses, file, indent=4)

                print("Expense deleted successfully!")
                return

        print("Expense not found.")

    def summary_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return
        
        total_expenses = len(self.expenses)
        total_spending = sum(expense['amount'] for expense in self.expenses)

        category_totals = {}

        for expense in self.expenses:
            category = expense['category']

            if category in category_totals:
                category_totals[category] += expense['amount']
            else:
                category_totals[category] = expense['amount']
        
        highest_expense_category = max(
            category_totals,
            key=category_totals.get
        )
        
        print(f"Total Expenses: {total_expenses}")
        print(f"Total Spending: {total_spending} EGP")
        print("\n")

        for category, total in category_totals.items():
            print(f"{category}: {total} EGP")

        print("\n")
        print(
            f"Highest Expense: {highest_expense_category} - "
            f"{category_totals[highest_expense_category]} EGP"
        )


expense_tracker = expenseTeacker()


while True:

    print("\n===== Expense Tracker =====")
    print("1 - Add Expense")
    print("2 - View Expenses")
    print("3 - Search Expense")
    print("4 - Filter Expense")
    print("5 - Delete Expense")
    print("6 - Summary Expense")
    print("7 - Exit")

    option = input("Choose an option: ")

    if option == "1":

        expense_title = input("Expense Title: ")

        while not expense_title or expense_title.isdigit():
            print("Invalid title. Please try again.")
            expense_title = input("Expense Title: ")

        expense_category = input("Expense Category: ")

        while not expense_category:
            print("Invalid category. Please try again.")
            expense_category = input("Expense Category: ")

        expense_amount = input("Expense Amount: ")

        while True:
            try:
                expense_amount = float(expense_amount)

                if expense_amount <= 0:
                    print("Amount must be greater than 0.")
                    expense_amount = input("Expense Amount: ")
                else:
                    break

            except ValueError:
                print("Invalid amount. Please enter a number.")
                expense_amount = input("Expense Amount: ")

        expense = {
            "title": expense_title.capitalize(),
            "category": expense_category.capitalize(),
            "amount": expense_amount,
            "date": datetime.now().isoformat()
        }

        expense_tracker.add_expense(expense)

        print("Expense added successfully!")

    elif option == "2":

        expense_tracker.view_expenses()

    elif option == "3":

        search = input("Enter expense title to search: ")

        expense_tracker.search_expense(search)

    elif option == "4":

        filter = input("Enter expense category to filter: ")

        expense_tracker.filter_expenses(filter)

    elif option == "5":

        expense_id = int(input("Enter expense ID to delete: "))

        expense_tracker.delete_expense(expense_id)

    elif option == "6":

        expense_tracker.summary_expenses()

    elif option == "7":

        print("Goodbye!")
        break

    else:

        print("Invalid operation. Please choose 1-7.")