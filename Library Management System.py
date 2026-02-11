import streamlit as st
import pandas as pd
import random
import re

books = {
    "Fiction / Literature": [
        {"name": "To Kill a Mockingbird", "price": 500},
        {"name": "1984", "price": 450},
        {"name": "The Great Gatsby", "price": 400},
        {"name": "Pride and Prejudice", "price": 350},
        {"name": "The Catcher in the Rye", "price": 420}
    ],
    "Self-Help / Personal Growth": [
        {"name": "Atomic Habits", "price": 700},
        {"name": "Think and Grow Rich", "price": 550},
        {"name": "The Power of Now", "price": 500}
    ],
    "Science / Knowledge / Tech": [
        {"name": "A Brief History of Time", "price": 600},
        {"name": "Python Crash Course", "price": 450},
        {"name": "Automate the Boring Stuff with Python", "price": 480}
    ],
}

class Library():
    def __init__(self, name: str, cnic: int, initial_deposit: int):
        self.name = name
        self.cnic = cnic
        self.initial_deposit = initial_deposit
        self.pin = random.randint(1000, 9999)

        # Append mode so existing accounts are not overwritten
        with open("user.txt", "a") as file:
            file.write(f"name:{self.name} cnic:{self.cnic} amt:{self.initial_deposit} pin:{self.pin}\n")

    @staticmethod
    def deposit(pin, amt):
        users = []
        pin_found = False

        with open('user.txt', 'r') as lines:
            for line in lines:
                pairs = re.findall(r'(\w+):([\w\d]+)', line)
                data = dict(pairs)
                users.append(data)

        for user in users:
            if int(user['pin']) == pin:
                user['amt'] = str(int(user["amt"]) + amt)
                pin_found = True
                break

        if not pin_found:
            return False

        with open("user.txt", "w") as file:
            for user in users:
                line = f"name:{user['name']} cnic:{user['cnic']} amt:{user['amt']} pin:{user['pin']}\n"
                file.write(line)

        return True

    @staticmethod
    def purchase_book(pin, price):
        users = []
        pin_found = False

        with open('user.txt', 'r') as lines:
            for line in lines:
                pairs = re.findall(r'(\w+):([\w\d]+)', line)
                data = dict(pairs)
                users.append(data)

        for user in users:
            if int(user['pin']) == pin:
                pin_found = True
                if int(user["amt"]) >= price:
                    user["amt"] = str(int(user["amt"]) - price)
                    # Write back updated data
                    with open("user.txt", "w") as file:
                        for u in users:
                            line = f"name:{u['name']} cnic:{u['cnic']} amt:{u['amt']} pin:{u['pin']}\n"
                            file.write(line)
                    return True
                else:
                    return "insufficient"

        if not pin_found:
            return False

# ---------------- Streamlit ----------------

st.title('Book Library')

menu = st.sidebar.selectbox(
    "Choose Option",
    ['Open Account', 'Deposit Money', 'Books']
)

# ----- Open Account -----
if menu == 'Open Account':
    name = st.text_input('Enter Your Name')
    cnic = st.number_input('Enter Your Cnic', step=1)
    initial_deposit = st.number_input('Enter Amount', step=1)

    if st.button('Submit'):
        ob1 = Library(name, cnic, initial_deposit)
        st.success(f"Account Created Successfully! Save this PIN: {ob1.pin}")

# ----- Deposit Money -----
if menu == 'Deposit Money':
    pin = st.number_input("Enter Your Pin", step=1)
    amt = st.number_input("Enter Amount", step=1)

    if st.button("Deposit"):
        result = Library.deposit(pin, amt)
        if result:
            st.success("Amount Successfully Deposited ✅")
        else:
            st.error("Invalid Pin ❌")

# ----- Books -----
if menu == 'Books':
    if "show_books" not in st.session_state:
        st.session_state.show_books = False

    selected_category = st.selectbox("Select Category", books.keys())

    if st.button('Show Books'):
        st.session_state.show_books = True

    if st.session_state.show_books:
        st.table(pd.DataFrame(books[selected_category], index=range(1, len(books[selected_category]) + 1)))

        selected_book = st.selectbox('Select Book', [book['name'] for book in books[selected_category]])
        book_price = next(book["price"] for book in books[selected_category] if book["name"] == selected_book)

        pin = st.number_input('Enter your account PIN to purchase', step=1)

        if st.button('Purchase Book'):
            result = Library.purchase_book(pin, book_price)
            if result == True:
                st.success(f'You have purchased "{selected_book}" for {book_price} Rs ✅')
            elif result == "insufficient":
                st.error("Insufficient Amount ❌")
            else:
                st.error("Invalid PIN ❌")
