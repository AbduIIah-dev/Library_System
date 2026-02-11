# Mini Book Library with Account & Payment System

**Mini Book Library with Account & Payment System** is a professional, interactive Python application built using **Streamlit** that combines a digital library with a mini banking system. It allows users to create personal accounts, deposit money, browse multiple book categories, and purchase books securely using their account balance. Each user is assigned a unique PIN for authentication, ensuring secure and verified transactions. All account data, including balances and transactions, is stored persistently in a text file (`user.txt`) to maintain user information across sessions.  

Users can open an account by providing their name, CNIC, and initial deposit amount. They can deposit additional money into their account at any time using their PIN. The library offers multiple book categories such as Fiction/Literature, Self-Help/Personal Growth, and Science/Knowledge/Tech, each containing a variety of books with defined prices. Users can browse these categories, view books in organized tables using **Pandas**, select a book, and complete the purchase by entering their account PIN. The system automatically checks if the account has sufficient funds and deducts the book’s price, displaying appropriate success or error messages for insufficient balance or invalid PIN.  

The project demonstrates practical usage of Python concepts such as **file handling**, **regular expressions for parsing user data**, **random number generation for PINs**, and **Streamlit session state management** for smooth, interactive web application behavior. It is designed to be both educational and functional, giving users hands-on experience with implementing account management, transaction logic, and UI interactivity.  

This application can be run locally by cloning the repository, installing the required dependencies with `pip install streamlit pandas`, and executing `streamlit run app.py`. It is a strong foundation for understanding real-world applications such as e-commerce or digital payment systems, and it can be extended further with features like purchase history, real-time account balance display, secure PIN hashing, book inventory management, and multi-user session handling.  

**Tech Stack:** Python 3.x, Streamlit, Pandas, Regex, Random  

**Note:** This project is for educational purposes and demonstrates how digital accounts, secure transactions, and interactive interfaces can be implemented in Python. It is not intended for real financial operations.
