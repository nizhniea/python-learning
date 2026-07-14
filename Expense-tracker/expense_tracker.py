print("Welcome to my Expense Tracker!")

expenses = []
while True:
    expense_name = input("What did you buy? ")
    expense_amount = float(input("How much did it cost? "))
    if expense_name == "quit":
        break

    expenses.append({
        "name": expense_name,
        "amount": expense_amount
    })
    print("Expense added successfully!")

    again = input("Do you want to add another expense? (yes/no) ")
    if again == "no":
        break
print(expenses)
for expense in expenses:
    print(f"You spent ${expense['amount']} on {expense['name']}.")
total_spent = 0
for expense in expenses:
    total_spent += expense['amount']
print(f"Total amount spent: ${total_spent}")