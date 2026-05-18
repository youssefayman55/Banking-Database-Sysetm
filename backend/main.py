# import necessary libraries
from fastapi import FastAPI
from Database.database import get_db_connection

# create an instance of the FastAPI class
app = FastAPI()

#home route
@app.get("/")
def home():
    return {"message": "Welcome to the Banking API!"}    


# route to get all customers
@app.get("/customers")
def get_customers():
    conn = get_db_connection()
    cursor = conn.cursor()
    

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return {"customers": customers}


@app.post("/customers")
def add_customer(customer : dict):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """ insert into customers (full_name , email , phone , address)
    values (%s,%s,%s,%s)"""

    cursor.execute(query , (customer["full_name"], customer["email"], customer["phone"], customer["address"]))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Customer added successfully!"}

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    query= """DELETE FROM customers WHERE customer_id = %s"""

    cursor.execute(query, (customer_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Customer deleted successfully!"}



# =========================================
# BRANCHES
# =========================================

# Get all branches
@app.get("/branches")
def get_branches():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM branches")

    branches = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"branches": branches}


# Add new branch
@app.post("/branches")
def add_branch(branch: dict):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO branches
    (branch_name, location)
    VALUES (%s, %s)
    """

    cursor.execute(
        query,
        (
            branch["branch_name"],
            branch["location"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Branch added successfully!"}


# Delete branch
@app.delete("/branches/{branch_id}")
def delete_branch(branch_id: int):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM branches WHERE branch_id = %s"

    cursor.execute(query, (branch_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Branch deleted successfully!"}

# route to add a new account
@app.post("/accounts")
def add_account(account: dict):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = """ insert into accounts (customer_id , branch_id , account_type , balance)
    values (%s,%s,%s,%s)"""

    cursor.execute(query , (account["customer_id"], account["branch_id"], account["account_type"], account["balance"]))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Account added successfully!"}

# delete account route
@app.delete("/accounts/{account_id}")
def delete_account(account_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()

    query= "DELETE FROM accounts WHERE account_id = %s"

    cursor.execute(query, (account_id,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Account deleted successfully!"}

# route to get all accounts
@app.get("/accounts")
def get_accounts():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return {"accounts": accounts}



# =========================================
# TRANSACTIONS
# =========================================

@app.post("/transactions")
def add_transaction(transaction: dict):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO transactions
    (account_id, transaction_type, amount, description)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            transaction["account_id"],
            transaction["transaction_type"],
            transaction["amount"],
            transaction["description"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Transaction added successfully!"}


@app.delete("/transactions/{transaction_id}")
def delete_transaction(transaction_id: int):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM transactions WHERE transaction_id = %s"

    cursor.execute(query, (transaction_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Transaction deleted successfully!"}

# route to get all transactions 
@app.get("/transactions")
def get_transactions():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return {"transactions": transactions}


# =========================================
# CARDS
# =========================================

# route to get all cards
@app.get("/cards")     
def get_credit_cards():

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cards")
    cards = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return {"cards": cards}


@app.post("/cards")
def add_card(card: dict):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO cards
    (account_id, card_number, card_type, expiry_date)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            card["account_id"],
            card["card_number"],
            card["card_type"],
            card["expiry_date"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Card added successfully!"}


@app.delete("/cards/{card_id}")
def delete_card(card_id: int):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM cards WHERE card_id = %s"

    cursor.execute(query, (card_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Card deleted successfully!"}



# =========================================
# LOANS
# =========================================

# route to get all loans
@app.get("/loans")          
def get_loans():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM loans")
    loans = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return {"loans": loans}


@app.post("/loans")
def add_loan(loan: dict):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO loans
    (customer_id, loan_amount, interest_rate, status)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            loan["customer_id"],
            loan["loan_amount"],
            loan["interest_rate"],
            loan["status"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Loan added successfully!"}


@app.delete("/loans/{loan_id}")
def delete_loan(loan_id: int):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM loans WHERE loan_id = %s"

    cursor.execute(query, (loan_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Loan deleted successfully!"}



# =========================================
# LOAN PAYMENTS
# =========================================


# route to get all loan payments
@app.get("/loan_payments")
def get_loan_payments():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM loan_payments")
    loan_payments = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return {"loan_payments": loan_payments}


@app.post("/loan_payments")
def add_loan_payment(payment: dict):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO loan_payments
    (loan_id, amount)
    VALUES (%s, %s)
    """

    cursor.execute(
        query,
        (
            payment["loan_id"],
            payment["amount"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Loan payment added successfully!"}


@app.delete("/loan_payments/{payment_id}")
def delete_loan_payment(payment_id: int):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM loan_payments WHERE payment_id = %s"

    cursor.execute(query, (payment_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Loan payment deleted successfully!"}




# =========================================
# EMPLOYEES
# =========================================


# route to get all employees
@app.get("/employees")
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employees")

    employees = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return {"employees": employees} 

@app.post("/employees")
def add_employee(employee: dict):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO employees
    (full_name, position, salary, branch_id)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            employee["full_name"],
            employee["position"],
            employee["salary"],
            employee["branch_id"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Employee added successfully!"}


@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM employees WHERE employee_id = %s"

    cursor.execute(query, (employee_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Employee deleted successfully!"}
