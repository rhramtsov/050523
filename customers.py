import json

class Customer:
    def __init__(self, customer_id, name, city, age):
        self.customer_id = customer_id
        self.name = name
        self.city = city
        self.age = age

    def __str__(self):
        return f"Customer Id: {self.customer_id}, Name: {self.name}, City: {self.city}, Age: {self.age}"

    def toJSON(self):
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "city": self.city,
            "age": self.age
        }

class CustomerList:
    def __init__(self):
        self.all_customers = []
        self.load_from_json()

    def add_customer(self, name, city, age):
        if len(self.all_customers) == 0:
            customer_id = 1
        else:
            customer_id = max([c.customer_id for c in self.all_customers]) + 1
        customer = Customer(customer_id, name, city, age)
        self.all_customers.append(customer)
        self.save_to_json()
        return customer

    def save_to_json(self):
        with open('customers.json', 'w') as f:
            json.dump([c.toJSON() for c in self.all_customers], f, indent=2)

    def load_from_json(self):
        try:
            with open('customers.json', 'r') as f:
                customer_data = json.load(f)
                for c in customer_data:
                    customer = Customer(c['customer_id'], c['name'], c['city'], c['age'])
                    self.all_customers.append(customer)
        except FileNotFoundError:
            pass

    def display_customers(self):
        for customer in self.all_customers:
            print(customer)

    def find_customer_by_name(self, name):
        found_customers = [customer for customer in self.all_customers if customer.name.lower() == name.lower()]
        if len(found_customers) == 0:
            print("No customer found with that name")
        else:
            for customer in found_customers:
                print(customer)

    def remove_customer(self, customer_id):
        self.all_customers = [customer for customer in self.all_customers if customer.customer_id != customer_id]
        self.save_to_json()
