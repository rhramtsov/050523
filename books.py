import json


class Book:
    def __init__(self, id, name, author, year_published, book_type):
        self.id = id
        self.name = name
        self.author = author
        self.year_published = year_published
        self.book_type = book_type
    
    def print(self):
        print(f"Book Id: {self.id}, Name: {self.name}, Author: {self.author}, Year Published: {self.year_published}, Type: {self.book_type}")
    
    def toJSON(self):
        return {
            "book id": self.id,
            "name": self.name,
            "author": self.author,
            "year_published": self.year_published,
            "book_type": self.book_type
        }


class BookList:
    all_books = []
    current_id = 1

    def __init__(self): 
        self.load_from_json()

    def add_book(self, name, author, year_published, book_type):
        if len(self.all_books) == 0:
            book_id = 1
        else:
            book_id = max([c.id for c in self.all_books]) + 1
        book = Book(book_id, name, author, year_published, book_type)
        self.all_books.append(book)
        self.save_to_json()
        return book


    def display_books(self):
        self.load_from_json()
        for book in self.all_books:
            book.print()

    def find_book_by_name(self, name):
        found_books = [book for book in self.all_books if book.name.lower() == name.lower()]
        if len(found_books) == 0:
            print("No book found with that name")
        else:
            for book in found_books:
                book.print()


    def remove_book(self, id):
        self.load_from_json()
        self.all_books = [book for book in self.all_books if book.id != id]
        self.save_to_json()
        # LoanList.remove_book_loans(id)

    def get_book_type_loan_duration(self, book):
        if book.book_type == 1:
            return 10
        elif book.book_type == 2:
            return 5
        elif book.book_type == 3:
            return 2
        else:
            return 0

    def load_from_json(self):
        with open('books.json', 'r') as f:
            books_data = json.load(f) 
            self.all_books = [Book(data["id"], data["name"], data["author"], data["year_published"], data["book_type"]) for data in books_data]

    def save_to_json(self):
        json_list = [book.toJSON() for book in self.all_books]
        with open("books.json", "w") as f:
            json.dump(json_list, f, indent=4)


class CustomEncoder(json.JSONEncoder):
    def default(self, o):
            return o.__dict__
    


all_books = []

def load_all_books():
    f = open("books.json")
    all_json_data = json.load(f)
    print("reading from file. the result is:", all_json_data)
    for json_obj_dict in all_json_data:
   
        book = Book(id=json_obj_dict["id"],name=json_obj_dict["name"],author=json_obj_dict["author"],year_published=json_obj_dict["year_published"],book_type=json_obj_dict["book_type"])
        all_books.append(book)
  

