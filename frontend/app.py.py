import streamlit as st
import pandas as pd
import requests

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="Banking Management System",
    page_icon="🏦",
    layout="wide"
)

# -----------------------------------
# TITLE
# -----------------------------------

st.title("🏦 Banking Management System")

st.write("Manage and visualize banking database tables.")

# -----------------------------------
# SIDEBAR
# -----------------------------------

menu = st.sidebar.selectbox(
    "Select Table",
    [
        "Customers",
        "Branches",
        "Accounts",
        "Transactions",
        "cards",
        "Loans",
        "Loan Payments",
        "Employees"
    ]
)

# -----------------------------------
# API URL
# -----------------------------------

BASE_URL = "http://127.0.0.1:8000"




# -----------------------------------
# CUSTOMERS
# -----------------------------------

if menu == "Customers":

    st.header("Customers")

    # Add new customer form
    st.subheader("Add New Customer")

    with st.form("add_customer_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        address = st.text_input("Address")

        submitted = st.form_submit_button("Add Customer")

        if submitted:
            customer_data = {
                "full_name": full_name,
                "email": email,
                "phone": phone,
                "address": address
            }
            response = requests.post(f"{BASE_URL}/customers", json=customer_data)

            if response.status_code == 200:
                st.success("Customer added successfully!")
            else:
                st.error("Failed to add customer")


    #delete customer form
    st.subheader("Delete Customer")

    with st.form("delete_customer_form"):
        customer_id = st.number_input("Customer ID", step=1)

        submitted = st.form_submit_button("Delete Customer")

        if submitted:
            response = requests.delete(f"{BASE_URL}/customers/{customer_id}")

            if response.status_code == 200:
                st.success("Customer deleted successfully!")
            else:
                st.error("Failed to delete customer")


    # Fetch and display customers data
    st.subheader("Customers Data")

    if st.button("Refresh Data"):
        response = requests.get(f"{BASE_URL}/customers")

        if response.status_code == 200:

            data = response.json()

        df = pd.DataFrame(
            data["customers"],
            columns=["customer_id", "full_name", "email", "phone", "address" , "created_at"]
       )

        st.dataframe(df,  width="stretch")

    else:
        st.error("Failed to load customers data")


# -----------------------------------
# BRANCHES
# -----------------------------------

elif menu == "Branches":

    st.header("Branches")

    # Add Branch
    st.subheader("Add New Branch")

    with st.form("add_branch_form"):

        branch_name = st.text_input(
            "Branch Name"
        )

        location = st.text_input(
            "Location"
        )

        submitted = st.form_submit_button(
            "Add Branch"
        )

        if submitted:

            branch_data = {
                "branch_name": branch_name,
                "location": location
            }

            response = requests.post(
                f"{BASE_URL}/branches",
                json=branch_data
            )

            if response.status_code == 200:
                st.success("Branch added successfully!")

            else:
                st.error("Failed to add branch")


    # Delete Branch
    st.subheader("Delete Branch")

    with st.form("delete_branch_form"):

        branch_id = st.number_input(
            "Branch ID",
            step=1
        )

        submitted = st.form_submit_button(
            "Delete Branch"
        )

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/branches/{branch_id}"
            )

            if response.status_code == 200:
                st.success("Branch deleted successfully!")

            else:
                st.error("Failed to delete branch")


    # Display Branches
    st.subheader("Branches Data")

    response = requests.get(f"{BASE_URL}/branches")

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(
            data["branches"],
            columns=[
                "branch_id",
                "branch_name",
                "location",
                "created_at"
            ]
        )

        st.dataframe(df, width="stretch")

    else:
        st.error("Failed to load branches data")



# -----------------------------------
# ACCOUNTS
# -----------------------------------

elif menu == "Accounts":

    st.header("Accounts")

    # add new account form
    st.subheader("Add New Account")

    with st.form("add_account_form"):
        customer_id = st.number_input("Customer ID", step=1)
        branch_id = st.number_input("Branch ID", step=1)
        account_type = st.selectbox("Account Type", ["Current", "Savings"])
        balance = st.number_input("Initial Balance", step=0.01)

        submitted = st.form_submit_button("Add Account")

        if submitted:
            account_data = {
                "customer_id": customer_id,
                "branch_id": branch_id,
                "account_type": account_type,
                "balance": balance
            }
            response = requests.post(f"{BASE_URL}/accounts", json=account_data)

            if response.status_code == 200:
                st.success("Account added successfully!")
            else:
                st.error("Failed to add account")


    # delete account form
    st.subheader("Delete Account")

    with st.form("delete_account_form"):
        account_id = st.number_input("Account ID", step=1)

        submitted = st.form_submit_button("Delete Account")

        if submitted:
            response = requests.delete(f"{BASE_URL}/accounts/{account_id}")

            if response.status_code == 200:
                st.success("Account deleted successfully!")
            else:
                st.error("Failed to delete account")

    # Fetch and display accounts data
    st.subheader("Accounts Data")

   # display accounts data in a table
    if st.button("Refresh Data"):

        response = requests.get(f"{BASE_URL}/accounts")

        if response.status_code == 200:

           data = response.json()

           df = pd.DataFrame(data["accounts"], columns=["account_id", "customer_id", "branch_id", "account_type", "balance", "created_at"])

           st.dataframe(df,  width="stretch")

    else:
        st.error("Failed to load accounts data")


# -----------------------------------
# TRANSACTIONS              
# -----------------------------------
elif menu == "Transactions":

    st.header("Transactions")

    # Add Transaction
    st.subheader("Add New Transaction")

    with st.form("add_transaction_form"):

        account_id = st.number_input("Account ID", step=1)

        transaction_type = st.selectbox(
            "Transaction Type",
            ["Deposit", "Withdraw"]
        )

        amount = st.number_input("Amount", step=0.01)

        description = st.text_input("Description")

        submitted = st.form_submit_button("Add Transaction")

        if submitted:

            transaction_data = {
                "account_id": account_id,
                "transaction_type": transaction_type,
                "amount": amount,
                "description": description
            }

            response = requests.post(
                f"{BASE_URL}/transactions",
                json=transaction_data
            )

            if response.status_code == 200:
                st.success("Transaction added successfully!")

            else:
                st.error("Failed to add transaction")


    # Delete Transaction
    st.subheader("Delete Transaction")

    with st.form("delete_transaction_form"):

        transaction_id = st.number_input(
            "Transaction ID",
            step=1
        )

        submitted = st.form_submit_button(
            "Delete Transaction"
        )

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/transactions/{transaction_id}"
            )

            if response.status_code == 200:
                st.success("Transaction deleted successfully!")

            else:
                st.error("Failed to delete transaction")


    # Display Transactions
    st.subheader("Transactions Data")

    response = requests.get(f"{BASE_URL}/transactions")

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(
            data["transactions"],
            columns=[
                "transaction_id",
                "account_id",
                "transaction_type",
                "amount",
                "description",
                "transaction_date"
            ]
        )

        st.dataframe(df, width="stretch")

# -----------------------------------
# CREDIT CARDS  
# -----------------------------------

elif menu == "cards":

    st.header("Cards")

    # Add Card
    st.subheader("Add New Card")

    with st.form("add_card_form"):

        account_id = st.number_input("Account ID", step=1)

        card_number = st.text_input("Card Number")

        card_type = st.selectbox(
            "Card Type",
            ["Debit", "Credit"]
        )

        expiry_date = st.date_input("Expiry Date")

        submitted = st.form_submit_button("Add Card")

        if submitted:

            card_data = {
                "account_id": account_id,
                "card_number": card_number,
                "card_type": card_type,
                "expiry_date": str(expiry_date)
            }

            response = requests.post(
                f"{BASE_URL}/cards",
                json=card_data
            )

            if response.status_code == 200:
                st.success("Card added successfully!")

            else:
                st.error("Failed to add card")


    # Delete Card
    st.subheader("Delete Card")

    with st.form("delete_card_form"):

        card_id = st.number_input("Card ID", step=1)

        submitted = st.form_submit_button("Delete Card")

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/cards/{card_id}"
            )

            if response.status_code == 200:
                st.success("Card deleted successfully!")

            else:
                st.error("Failed to delete card")


    # Display Cards
    st.subheader("Cards Data")

    response = requests.get(f"{BASE_URL}/cards")

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(
            data["cards"],
            columns=[
                "card_id",
                "account_id",
                "card_number",
                "card_type",
                "expiry_date",
                "created_at"
            ]
        )

        st.dataframe(df, width="stretch")

# -----------------------------------
# LOANS
# -----------------------------------

elif menu == "Loans":

    st.header("Loans")

    # Add Loan
    st.subheader("Add New Loan")

    with st.form("add_loan_form"):

        customer_id = st.number_input("Customer ID", step=1)

        loan_amount = st.number_input(
            "Loan Amount",
            step=0.01
        )

        interest_rate = st.number_input(
            "Interest Rate",
            step=0.01
        )

        status = st.selectbox(
            "Loan Status",
            ["Pending", "Approved", "Rejected", "Paid"]
        )

        submitted = st.form_submit_button("Add Loan")

        if submitted:

            loan_data = {
                "customer_id": customer_id,
                "loan_amount": loan_amount,
                "interest_rate": interest_rate,
                "status": status
            }

            response = requests.post(
                f"{BASE_URL}/loans",
                json=loan_data
            )

            if response.status_code == 200:
                st.success("Loan added successfully!")

            else:
                st.error("Failed to add loan")


    # Delete Loan
    st.subheader("Delete Loan")

    with st.form("delete_loan_form"):

        loan_id = st.number_input(
            "Loan ID",
            step=1
        )

        submitted = st.form_submit_button(
            "Delete Loan"
        )

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/loans/{loan_id}"
            )

            if response.status_code == 200:
                st.success("Loan deleted successfully!")

            else:
                st.error("Failed to delete loan")


    # Display Loans
    st.subheader("Loans Data")

    response = requests.get(f"{BASE_URL}/loans")

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(
            data["loans"],
            columns=[
                "loan_id",
                "customer_id",
                "loan_amount",
                "interest_rate",
                "status",
                "created_at"
            ]
        )

        st.dataframe(df, width="stretch")

    else:
        st.error("Failed to load loans data")



# -----------------------------------
# LOAN PAYMENTS
# -----------------------------------

elif menu == "Loan Payments":

    st.header("Loan Payments")

    # Add Loan Payment
    st.subheader("Add New Loan Payment")

    with st.form("add_payment_form"):

        loan_id = st.number_input(
            "Loan ID",
            step=1
        )

        amount = st.number_input(
            "Payment Amount",
            step=0.01
        )

        submitted = st.form_submit_button(
            "Add Payment"
        )

        if submitted:

            payment_data = {
                "loan_id": loan_id,
                "amount": amount
            }

            response = requests.post(
                f"{BASE_URL}/loan_payments",
                json=payment_data
            )

            if response.status_code == 200:
                st.success("Loan payment added successfully!")

            else:
                st.error("Failed to add payment")


    # Delete Loan Payment
    st.subheader("Delete Loan Payment")

    with st.form("delete_payment_form"):

        payment_id = st.number_input(
            "Payment ID",
            step=1
        )

        submitted = st.form_submit_button(
            "Delete Payment"
        )

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/loan_payments/{payment_id}"
            )

            if response.status_code == 200:
                st.success("Loan payment deleted successfully!")

            else:
                st.error("Failed to delete payment")


    # Display Loan Payments
    st.subheader("Loan Payments Data")

    response = requests.get(f"{BASE_URL}/loan_payments")

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(
            data["loan_payments"],
            columns=[
                "payment_id",
                "loan_id",
                "amount",
                "payment_date"
            ]
        )

        st.dataframe(df, width="stretch")

    else:
        st.error("Failed to load loan payments data")




# -----------------------------------
# EMPLOYEES
# -----------------------------------

elif menu == "Employees":

    st.header("Employees")

    # Add Employee
    st.subheader("Add New Employee")

    with st.form("add_employee_form"):

        full_name = st.text_input(
            "Full Name"
        )

        position = st.text_input(
            "Position"
        )

        salary = st.number_input(
            "Salary",
            step=0.01
        )

        branch_id = st.number_input(
            "Branch ID",
            step=1
        )

        submitted = st.form_submit_button(
            "Add Employee"
        )

        if submitted:

            employee_data = {
                "full_name": full_name,
                "position": position,
                "salary": salary,
                "branch_id": branch_id
            }

            response = requests.post(
                f"{BASE_URL}/employees",
                json=employee_data
            )

            if response.status_code == 200:
                st.success("Employee added successfully!")

            else:
                st.error("Failed to add employee")


    # Delete Employee
    st.subheader("Delete Employee")

    with st.form("delete_employee_form"):

        employee_id = st.number_input(
            "Employee ID",
            step=1
        )

        submitted = st.form_submit_button(
            "Delete Employee"
        )

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/employees/{employee_id}"
            )

            if response.status_code == 200:
                st.success("Employee deleted successfully!")

            else:
                st.error("Failed to delete employee")


    # Display Employees
    st.subheader("Employees Data")

    response = requests.get(f"{BASE_URL}/employees")

    if response.status_code == 200:

        data = response.json()

        df = pd.DataFrame(
            data["employees"],
            columns=[
                "employee_id",
                "full_name",
                "position",
                "salary",
                "branch_id",
                "created_at"
            ]
        )

        st.dataframe(df, width="stretch")

    else:
        st.error("Failed to load employees data")