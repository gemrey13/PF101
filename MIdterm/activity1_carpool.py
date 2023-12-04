class Vehicle:
    def __init__(self, name: str, capacity: int, fare_per_kilo: float):
        self.name = name
        self.capacity = capacity
        self.fare_per_kilo = fare_per_kilo
        self.driver = None
        self.customers = []
        self.total_fare = 0

    def assign_driver(self, driver):
        self.driver = driver
        print(f'Driver {self.driver.get_name} with license number ({self.driver.get_license_number}) assigned to vehicle {self.name}')

    def add_customer(self, customer):
        if len(self.customers) != self.capacity:
            self.customers.append(customer)
            print(f'Customer {customer.name} is added')
        else:
            print(f'Vehicle {self.name} reached it\'s capacity')
    
    def calculate_fare(self, km):
        self.total_fare = self.fare_per_kilo * km
        print(f'Total Fare is {self.total_fare}')

    def get_description(self):
        print()
        print(f'Vehicle {self.name} have capacity of {self.capacity} and have {len(self.customers)} customers.\n[Fare:\t\t{self.total_fare}]')
        print(f'Customer\tSeat')
        for index, customer in enumerate(self.customers):
            print(f'{customer.name}\t\t#{index + 1}')

class Driver:
    def __init__(self, name: str, license_number: str):
        self.name = name
        self.license_number = license_number

    @property
    def get_name(self):
        return self.name.title()

    @property
    def get_license_number(self):
        return self.license_number.title()

class Customer:
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number

ferrari = Vehicle('ferrari', 2, 2.5)

mcqueen = Driver('mc queen', '0201-987561')

loki = Customer('loki', '095242141')
thor = Customer('thor', '095745612')
odin = Customer('odin', '096674841')

ferrari.assign_driver(mcqueen)

ferrari.add_customer(loki)
ferrari.add_customer(thor)
ferrari.add_customer(odin)


ferrari.calculate_fare(10)

ferrari.get_description()


