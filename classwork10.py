from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self, name, year_joined):
        self.name = name
        self.year_joined = year_joined

    def years_on_platform(self):
        return 2025 - self.year_joined

    @abstractmethod
    def role(self):
        pass

    def __str__(self):
        return f"{self.name} is a {self.role()} and has been using the platform for {self.years_on_platform()} years."

class Customer(User):
    def role(self):
        return "Customer"

class Vendor(User):
    def role(self):
        return "Vendor"

u1 = Customer("Alice", 2020)
u2 = Vendor("Bob", 2018)

print(u1)
