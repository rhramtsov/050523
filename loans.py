
import json
from datetime import datetime, timedelta

class LoanList:
    def __init__(self):
        self.loan_file = "loans.json"
        self.loans = []
        self.load_loans()

    def load_loans(self):
        with open(self.loan_file, 'r') as f:
            data = json.load(f)
            for loan_data in data:
                loan = Loan.from_dict(loan_data)
                self.loans.append(loan)

    def save_all_loans(self):
        with open(self.loan_file, 'w') as f:
            data = [loan.to_dict() for loan in self.loans]
            json.dump(data, f)

    def loan_book(self, customer_id, book_id):
        loan_id = len(self.loans) + 1
        date_issued = datetime.now()
        due_date = date_issued + timedelta(days=14)
        loan = Loan(loan_id, customer_id, book_id, date_issued, due_date)
        self.loans.append(loan)
        self.save_all_loans()
        return loan

    def find_loan_by_id(self, loan_id):
        for loan in self.loans:
            if loan.loan_id == loan_id:
                return loan
        return None

    def remove_loan(self, loan_id):
        loan = self.find_loan_by_id(loan_id)
        if loan is not None:
            self.loans.remove(loan)
            self.save_all_loans()
            print(f"Loan with id {loan_id} has been removed.")
        else:
            print(f"Loan with id {loan_id} not found.")

    def return_book(self, loan_id):
        loan = self.find_loan_by_id(loan_id)
        if loan is not None:
            loan.return_date = datetime.now()
            self.save_all_loans()
            print(f"Book with id {loan.book_id} has been returned by customer with id {loan.customer_id}.")
        else:
            print(f"Loan with id {loan_id} not found.")

    def display_loans(self):
        if len(self.loans) > 0:
            print("Loans:")
            for loan in self.loans:
                print(f"Loan id: {loan.loan_id}")
                print(f"Customer id: {loan.customer_id}")
                print(f"Book id: {loan.book_id}")
                print(f"Start date: {loan.start_date}")
                if loan.return_date is not None:
                    print(f"Return date: {loan.return_date}")
                print()
        else:
            print("No loans found.")

    def display_late_loans(self):
        now = datetime.now()
        late_loans = [loan for loan in self.loans if loan.end_date < now and loan.return_date is None]
        if len(late_loans) > 0:
            print("Late loans:")
            for loan in late_loans:
                print(f"Loan id: {loan.loan_id}")
                print(f"Customer id: {loan.customer_id}")
                print(f"Book id: {loan.book_id}")
                print(f"End date: {loan.end_date}")
                print()
        else:
            print("No late loans found.")


class Loan:
    def __init__(self, loan_id, customer_id, book_id, start_date, end_date, return_date=None):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.book_id = book_id
        self.start_date = start_date
        self.end_date = end_date
        self.return_date = return_date

    @classmethod
    def from_dict(cls, loan_dict):
        loan_id = loan_dict.get('loan_id')
        customer_id = loan_dict.get('customer_id')
        book_id = loan_dict.get('book_id')
        start_date_str = loan_dict.get('start_date')
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M:%S') if start_date_str else None
        end_date_str = loan_dict.get('end_date')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d %H:%M:%S') if end_date_str else None
        return_date_str = loan_dict.get('return_date')
        return_date = datetime.strptime(return_date_str, '%Y-%m-%d %H:%M:%S') if return_date_str else None
        if loan_id is None or customer_id is None or book_id is None or start_date is None or end_date is None:
            raise ValueError("Loan data missing required fields")
        return cls(loan_id, customer_id, book_id, start_date, end_date, return_date)

    def to_dict(self):
        return {
            "loan_id": self.loan_id,
            "customer_id": self.customer_id,
            "book_id": self.book_id,
            "start_date": self.start_date.strftime('%Y-%m-%d %H:%M:%S') if self.start_date else None,
            "end_date": self.end_date.strftime('%Y-%m-%d %H:%M:%S') if self.end_date else None,
            "return_date": self.return_date.strftime('%Y-%m-%d %H:%M:%S') if self.return_date else None,
        }

