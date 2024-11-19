### **Transaction History Tracker – Project Setup**  

#### **What It Does**  
The Transaction History Tracker records barter transactions and outputs a summary of recent trades.  

#### **Key Features**  
- Logs each trade with items, values, and trade date.  
- Displays a summary of all transactions.  

#### **Python Code** (Simple Version)  
```python
# Transaction History Tracker

import datetime

# Initialize transaction log
transaction_log = []

def log_transaction(item1, value1, item2, value2):
    """
    Logs a barter transaction with date and details.
    """
    transaction = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "item1": item1,
        "value1": value1,
        "item2": item2,
        "value2": value2
    }
    transaction_log.append(transaction)
    print("\nTransaction logged successfully!\n")

def display_transactions():
    """
    Displays all logged transactions.
    """
    print("\nTransaction History:")
    for i, t in enumerate(transaction_log, start=1):
        print(f"{i}. {t['date']}: {t['item1']} (Value: {t['value1']}) ↔ {t['item2']} (Value: {t['value2']})")

# User interaction
print("Welcome to the Transaction History Tracker!")
while True:
    item1 = input("\nEnter the first item: ")
    value1 = float(input(f"Enter the value of {item1}: "))
    item2 = input("Enter the second item: ")
    value2 = float(input(f"Enter the value of {item2}: "))
    log_transaction(item1, value1, item2, value2)
    
    # Display transaction log
    display_transactions()
    
    # Continue or exit
    cont = input("\nWould you like to log another transaction? (yes/no): ").strip().lower()
    if cont != "yes":
        print("\nThank you for using the Transaction History Tracker!")
        break
