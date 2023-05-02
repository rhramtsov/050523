from customers import CustomerList
from books import BookList
from loans import LoanList
import json

book_list = BookList()
all_customers = CustomerList()
loan_list = LoanList()

def display_menu():
    print("""
1. Add a new customer
2. Display all customers
3. Find customer by name
4. Remove customer
5. Add a new book
6. Display all books
7. Find book by name
8. Remove book
9. Loan a book
10. Return a book
11. Display all loans
12. Display late loans
0. Exit
""")

def add_customer():
    name = input("Enter customer name: ")
    city = input("Enter customer city: ")
    age = int(input("Enter customer age: "))
    customer = all_customers.add_customer(name, city, age)
    print("Customer added with id:", customer.customer_id)

def display_customers():
    all_customers.display_customers()

def find_customer_by_name():
    name = input("Enter customer name: ")
    found_customers = []
    for customer in all_customers.all_customers:
        if name.lower() in customer.name.lower():
            found_customers.append(customer)
    if len(found_customers) == 0:
        print("No customer found with that name")
    else:
        for customer in found_customers:
            print(customer)

def remove_customer():
    customer_id = int(input("Enter customer id: "))
    all_customers.remove_customer(customer_id)


def add_book():
    name = input("Enter book name: ")
    author = input("Enter book author: ")
    year_published = input("Enter year published: ")
    book_type = input("Enter book type (1/2/3): ")
    book = book_list.add_book(name, author, year_published, book_type)
    print("Book added with id:", book.book_id)


def display_books():
    book_list.display_books()


def find_book_by_name():
    name = input("Enter book name: ")
    book_list.find_book_by_name(name)


def remove_book():
    book_id = int(input("Enter book id: "))
    book_list.remove_book(book_id)

def loan_book():
    customer_id = int(input("Enter customer id: "))
    book_id = int(input("Enter book id: "))
    loan = loan_list.loan_book(customer_id, book_id)
    print(f"Book with id {book_id} has been loaned to customer with id {customer_id} with loan id {loan.loan_id}")


def return_book():
    loan_id = int(input("Enter loan id: "))
    loan_list.return_book(loan_id)

def display_loans():
    loan_list.display_loans()


def display_late_loans():
    loan_list.display_late_loans()


def main():
    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "0":
            break
        elif choice == "1":
            add_customer()
        elif choice == "2":
            display_customers()
        elif choice == "3":
            find_customer_by_name()
        elif choice == "4":
            remove_customer()
        elif choice == "5":
            add_book()
        elif choice == "6":
            display_books()
        elif choice == "7":
            find_book_by_name()
        elif choice == "8":
            remove_book()
        elif choice == "9":
            loan_book()
        elif choice == "10":
            return_book()
        elif choice == "11":
            display_loans()
        elif choice == "12":
            display_late_loans()
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
