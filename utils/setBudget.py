import pandas as pd
import os

BUDGET_FILE = "data/budgets.csv"

def load_budgets():
    if os.path.exists(BUDGET_FILE):
        return pd.read_csv(BUDGET_FILE)
    else:
        return pd.DataFrame(columns=["Type", "Category", "Amount"])

def save_budgets(df):
    df.to_csv(BUDGET_FILE, index=False)
    print(" Budget updated successfully!")

def set_overall_budget(df):
    try:
        amount = float(input(" Enter new overall budget amount (₹): "))
        if 'Overall' in df['Type'].values:
            df.loc[df['Type'] == 'Overall', 'Amount'] = amount
        else:
            df = pd.concat([df, pd.DataFrame([{"Type": "Overall", "Category": "-", "Amount": amount}])], ignore_index=True)
        print(f" Set overall budget to ₹{amount}")
    except ValueError:
        print(" Invalid input. Please enter a number.")
    return df

def set_category_budget(df):
    category = input(" Enter category name: ").strip().title()
    try:
        amount = float(input(f" Enter budget for '{category}' (₹): "))
        mask = (df['Type'] == 'Category') & (df['Category'] == category)

        if mask.any():
            df.loc[mask, 'Amount'] = amount
            print(f"Updated budget for '{category}' to ₹{amount}")
        else:
            new_row = pd.DataFrame([{"Type": "Category", "Category": category, "Amount": amount}])
            df = pd.concat([df, new_row], ignore_index=True)
            print(f"Added new category '{category}' with budget ₹{amount}")
    except ValueError:
        print(" Invalid input. Please enter a number.")
    return df

def set_budget():
    df = load_budgets()
    print("\nBudget Settings Menu:")
    print("1. Set/Update Overall Budget")
    print("2. Set/Update Category Budget")
    
    choice = input("Choose an option (1 or 2): ").strip()
    
    if choice == '1':
        df = set_overall_budget(df)
    elif choice == '2':
        df = set_category_budget(df)
    else:
        print("Invalid choice.")

    save_budgets(df)

if __name__ == "__main__":
    set_budget()
