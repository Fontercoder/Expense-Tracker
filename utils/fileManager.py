import pandas as pd
import os
from datetime import datetime

file_path = "data/expenses.csv"

os.makedirs("data", exist_ok=True)

CATEGORIES = ['Food', 'Transport', 'Shopping', 'Utilities', 'Entertainment', 'Medical', 'Others'] # List of categories

def log_expense():
    date = input("Enter date (YYYY-MM-DD) [Leave empty for today]: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    
    print("\nAvailable categories:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}. {cat}")
    
    cat_index = int(input("\nSelect category by number: "))
    category = CATEGORIES[cat_index - 1]

    amount = float(input("Enter amount (₹): "))
    note = input("Optional note (e.g., KFC dinner, Uber): ")

    # new entry dataframe
    new_entry = pd.DataFrame([{
        "Date": date,
        "Category": category,
        "Amount": amount,
        "Note": note
    }])

    # Check if file exists, then append or create
    if os.path.exists(file_path):
        existing_data = pd.read_csv(file_path)
        updated_data = pd.concat([existing_data, new_entry], ignore_index=True)
    else:
        updated_data = new_entry

    updated_data.to_csv(file_path, index=False)
    print(f"\n Expense logged: ₹{amount} under '{category}' on {date}")
