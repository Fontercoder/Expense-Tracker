import pandas as pd
from datetime import datetime, timedelta
import os

def load_expense_data(file_path="data/expenses.csv"):
    if not os.path.exists(file_path):
        print(" Expense file not found.")
        return pd.DataFrame()
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

# Current day's expenditure
def daily_summary(df):
    today = pd.to_datetime(datetime.today().date())
    day_total = df[df['Date'] == today]['Amount'].sum()
    return round(day_total, 2)

# Current week's expenditure
def weekly_summary(df):
    today = datetime.today()
    start_of_week = today - timedelta(days=today.weekday())  # Monday as start
    week_df = df[(df['Date'] >= pd.to_datetime(start_of_week.date()))]
    return round(week_df['Amount'].sum(), 2)

# Current month's expenditure
def monthly_summary(df):
    today = datetime.today()
    month_df = df[(df['Date'].dt.month == today.month) & (df['Date'].dt.year == today.year)]
    return round(month_df['Amount'].sum(), 2)

# Overall expenditure
def overall_summary(df):
    return round(df['Amount'].sum(), 2)

# Generate full report
def generate_summary_report():
    df = load_expense_data()
    if df.empty:
        print("No data available for summary.")
        return

    print("\n Expense Summary:")
    daily = daily_summary(df)
    weekly = weekly_summary(df)
    monthly = monthly_summary(df)
    overall = overall_summary(df)

    print(f"📅 Today       : ₹{daily}")
    print(f"📆 This Week   : ₹{weekly}")
    print(f"🗓️  This Month  : ₹{monthly}")
    print(f"📈 Overall     : ₹{overall}")

    # Prepare export DataFrame
    summary_df = pd.DataFrame([{
        "Date": datetime.today().strftime("%Y-%m-%d"),
        "Today": daily,
        "Week": weekly,
        "Month": monthly,
        "Overall": overall
    }])

    # Export the summary report
    os.makedirs("data/reports", exist_ok=True)
    export_path = f"data/reports/summary_report_{datetime.today().strftime('%Y%m%d')}.csv"
    summary_df.to_csv(export_path, index=False)

    print(f"\n✅ Report exported to: {export_path}")

if __name__ == "__main__":
    generate_summary_report()
 