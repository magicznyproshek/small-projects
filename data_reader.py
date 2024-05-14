import csv

class Customer:
    def __init__(self, id, firstName, lastName, company, address, city, state, zip):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.company = company
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip

    def full_name(self):
        return f"{self.firstName} {self.lastName}"

    def full_address(self):
        if self.company:
            return f"{self.address}\n{self.company}\n{self.city}, {self.state} {self.zip}"
        else:
            return f"{self.address}\n{self.city}, {self.state} {self.zip}"

class CustomerViewer:
    def __init__(self, filename):
        self.customers = self.read_customers_from_csv(filename)

    def read_customers_from_csv(self, filename):
        customers = []
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                id = row.get('cust_id', None)
                firstName = row.get('first_name', '')
                lastName = row.get('last_name', '')
                company = row.get('company_name', '')
                address = row.get('address', '')
                city = row.get('city', '')
                state = row.get('state', '')
                zip = row.get('zip', '')
                
                if id is not None:  # Ensure 'cust_id' column exists
                    customer = Customer(id, firstName, lastName, company, address, city, state, zip)
                    customers.append(customer)
        return customers

    def find_customer_by_id(self, id):
        for customer in self.customers:
            if customer.id == id:
                return customer
        return None

    def display_customer_info(self, customer):
        if customer:
            print(customer.full_name())
            print(customer.full_address())
        else:
            print("No customer with that ID.")

    def run(self):
        print("Customer Viewer")
        while True:
            customer_id = input("Enter customer ID: ")
            customer = self.find_customer_by_id(customer_id)
            self.display_customer_info(customer)
            continue_option = input("Continue? (y/n): ")
            if continue_option.lower() != 'y':
                print("Bye!")
                break
def main():
    filename = input("Enter the path to the customer CSV file: ")
    viewer = CustomerViewer(filename)
    viewer.run()

if __name__ == "__main__":
    main()

