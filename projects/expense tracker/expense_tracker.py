import csv
import os
from datetime import datetime

class Expense:
    """
    This object represents an expense, storing details like amount, category, and date.
    """
    def __init__(self, amount, category, date=None):
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.today().strftime('%Y-%m-%d')


class ExpenseTracker:
    """
    This object manages adding, viewing, and categorizing expenses, with sorting functionality.
    """
    FILE_NAME = "expenses.csv"

    def __init__(self):
        self.expenses = []
        self.load_expenses()

    def add_expense(self, expense):
        self.expenses.append(expense)
        self.save_expenses()
        print(f"Expense of Rs. {expense.amount} added under category '{expense.category}' on {expense.date}.")

    def view_expenses(self, sort_by=None):
        if not self.expenses:
            print("No expenses recorded.")
            return

        if sort_by == "date":
            self.expenses.sort(key=lambda x: x.date)
        elif sort_by == "category":
            self.expenses.sort(key=lambda x: x.category)
        
        print("\nYour Expenses:")
        print("Date       | Category       | Amount")
        print("----------------------------------")
        for exp in self.expenses:
            print(f"{exp.date} | {exp.category.ljust(12)} | Rs. {exp.amount}")

    def total_expense(self):
        total = sum(exp.amount for exp in self.expenses)
        print(f"Total expenses: Rs. {total}")
        return total

    def save_expenses(self):
        with open(self.FILE_NAME, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount"])
            for exp in self.expenses:
                writer.writerow([exp.date, exp.category, exp.amount])

    def load_expenses(self):
        if not os.path.exists(self.FILE_NAME):
            return
        with open(self.FILE_NAME, mode='r') as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                self.expenses.append(Expense(float(row[2]), row[1], row[0]))


def main():
    tracker = ExpenseTracker()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Expenses (Sorted by Date)")
        print("4. View Expenses (Sorted by Category)")
        print("5. Total Expenses")
        print("6. Exit")

        choice = input("Choose an option: ")
        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            tracker.add_expense(Expense(amount, category))
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.view_expenses(sort_by="date")
        elif choice == "4":
            tracker.view_expenses(sort_by="category")
        elif choice == "5":
            tracker.total_expense()
        elif choice == "6":
            print("Exiting... Your expenses have been saved.")
            break
        else:
            print("Invalid choice, please try again.")
        input("Press any key to continue...")

if __name__ == "__main__":
    main()
