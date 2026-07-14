print("Welcome to my Expense Tracker!")

expenses = []
def add_expense():
    expense_name = input("What did you buy? ")
    expense_amount = float(input("How much did it cost? "))
 
    expenses.append({
        "name": expense_name,
        "amount": expense_amount
    })
    print("Expense added successfully!")
while True:
    add_expense()
    again = input("Do you want to add another expense? (yes/no) ")
    if again == "no":
        break
def view_expenses():
    for expense in expenses:
        print(f"You spent ${expense['amount']} on {expense['name']}.")

total_spent = 0

def calculate_total():
    total_spent = 0
    for expense in expenses:
        total_spent += expense['amount']
    return total_spent
total = calculate_total()
print(f"Total amount spent: ${total}")

show_expenses = input("Do you want to view your expenses? (yes/no) ")
if show_expenses == "yes": 
    view_expenses()
if show_expenses == "no":
    print("Okay, have a great day!")
    
want_total = input("Do you want to calculate the total amount spent? (yes/no) ")
if want_total == "yes":
    total = calculate_total()
    print(f"Total amount spent: ${total}")
if want_total == "no":
    print("Okay, have a great day!")