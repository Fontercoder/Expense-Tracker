import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

def load_data(file_path="data/expenses.csv"):
    if not os.path.exists(file_path):
        print(" Expense file not found.")
        return pd.DataFrame()
    df = pd.read_csv(file_path)
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def show_pie_chart(df):
    category_totals = df.groupby('Category')['Amount'].sum()
    plt.figure(figsize=(7, 7))
    plt.pie(category_totals, labels=category_totals.index, autopct='%1.1f%%', startangle=140)
    plt.title("Expense Distribution by Category")
    plt.axis('equal')
    plt.show()

def show_bar_chart(df, period="monthly"):
    df['Month'] = df['Date'].dt.to_period('M')
    df['Week'] = df['Date'].dt.to_period('W')

    if period == "monthly":
        summary = df.groupby('Month')['Amount'].sum()
        plt.bar(summary.index.astype(str), summary.values, color='skyblue')
        plt.title("Monthly Expense Summary")
        plt.xlabel("Month")
    else:
        summary = df.groupby('Week')['Amount'].sum()
        plt.bar(summary.index.astype(str), summary.values, color='salmon')
        plt.title("Weekly Expense Summary")
        plt.xlabel("Week")

    plt.ylabel("Amount (₹)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def show_line_chart(df):
    daily_summary = df.groupby('Date')['Amount'].sum()
    plt.plot(daily_summary.index, daily_summary.values, marker='o', linestyle='-')
    plt.title("Daily Expenses Over Time")
    plt.xlabel("Date")
    plt.ylabel("Amount (₹)")
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualise_expenses():
    df = load_data()
    if df.empty:
        return

    print("\n📈 Chart Options:")
    print("1. Pie Chart - Category wise")
    print("2. Bar Chart - Monthly")
    print("3. Bar Chart - Weekly")
    print("4. Line Chart - Daily Trends")

    choice = input("Choose chart type (1-4): ")

    if choice == '1':
        show_pie_chart(df)
    elif choice == '2':
        show_bar_chart(df, period="monthly")
    elif choice == '3':
        show_bar_chart(df, period="weekly")
    elif choice == '4':
        show_line_chart(df)
    else:
        print(" Invalid choice!")

if __name__ == "__main__":
    visualise_expenses()
