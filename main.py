from utils import fileManager as fm
from utils import setBudget as sb
from analysis import summary as sm
from analysis import budget_checker as bc
from visualization import charts as vc


choice = 0  
while choice != 7:
    print("1. Daily Expense log")
    print("2. Expense Summary")
    print("3. Visualize Expenses")
    print("4. Set Budget")
    print("5. Check Overages")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        fm.log_expense()
    elif choice == 2:
        sm.generate_summary_report()
    elif choice == 3:
        vc.visualise_expenses()
    elif choice == 4:
        sb.set_budget()
    elif choice == 5:
        bc.checkBudget()
    elif choice == 6:
        print("Exiting the program...")
    else:
        print("Invalid choice, please try again.")