import pandas as pd
import os

def load_expenses(file_path="data/expenses.csv"):
    if not os.path.exists(file_path):
        print(" Expense file not found.")
        return pd.DataFrame()
    df = pd.read_csv(file_path)
    return df

def load_budgets(file_path="data/budgets.csv"):
    if not os.path.exists(file_path):
        print(" Budget file not found.")
        return pd.DataFrame()
    df = pd.read_csv(file_path)
    return df

def check_overall_budget(exp_df, budget_df):
    total_spent = exp_df['Amount'].sum()
    overall_budget = budget_df[(budget_df['Type'] == 'Overall')]['Amount'].values[0]

    print("\n Overall Budget Check:")
    print(f" Total Spent  : ₹{total_spent}")
    print(f" Budget Limit : ₹{overall_budget}")

    if total_spent > overall_budget:
        print(" ALERT: You’ve exceeded your overall budget!")
    else:
        print("You're within your overall budget.")

def check_category_budgets(exp_df, budget_df):
    print("\n Category-wise Budget Check:")
    category_budgets = budget_df[budget_df['Type'] == 'Category']

    for _, row in category_budgets.iterrows():
        category = row['Category']
        limit = row['Amount']
        spent = exp_df[exp_df['Category'] == category]['Amount'].sum()

        status = "OK" if spent <= limit else "Budget limit has Over"
        print(f" - {category:15}: Spent ₹{spent:>6} / Budget ₹{limit:<6} => {status}")

def checkBudget():
    exp_df = load_expenses()
    budget_df = load_budgets()

    if exp_df.empty or budget_df.empty:
        print(" Cannot proceed — missing data.")
        return

    check_overall_budget(exp_df, budget_df)
    check_category_budgets(exp_df, budget_df)

if __name__ == "__main__":
    checkBudget()
