import streamlit as st
import pandas as pd
import os

def load_expenses():
    if not os.path.exists("expenses.csv"):
        return pd.DataFrame()  # Return an empty DataFrame
    else:
        return pd.read_csv("expenses.csv")

def save_expenses(expenses):
    expenses.to_csv("expenses.csv", index=False)

def main(): 
    st.title("Habert Expense Tracker")

    # Load existing expenses or start with an empty DataFrame
    expenses = load_expenses()

    # Input fields for expense details
    expense_name = st.text_input("Enter Expense Name")
    expense_amount = st.number_input("Enter Amount")
    expense_date = st.date_input("Select Date")

    if st.button("Add Expense"):
        new_expense = pd.DataFrame({
            "Name": [expense_name],
            "Amount": [expense_amount],
            "Date": [expense_date]
        })
        expenses = pd.concat([expenses, new_expense], ignore_index=True)
        save_expenses(expenses)
        st.success("Expense added successfully!")

    # Display the current list of expenses
    if not expenses.empty:  # Check if the DataFrame is not empty
        st.header("List of Expenses")
        st.write(expenses)
    else:
        st.warning("No expenses added yet.")

if __name__ == "__main__":
    main()