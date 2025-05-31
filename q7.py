class Car:
    """
    Task 1
    - Define a class named Car with attributes: make, model, year
    - Initialize these attributes in the __init__ method
    - Add a method named describe_car() that prints information about the car as "Year Make Model"
    """

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print(f"{self.year} {self.make} {self.model}")
        
# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Calling the method to describe the car
my_car.describe_car()  # Expected Output: "2020 Toyota Corolla"