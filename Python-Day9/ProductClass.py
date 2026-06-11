#Create Product Class
class Product:
    def __init__(self, name, price):
        self.name= name
        self.price= price

    def display(self):
        print("Product name:", self.name)
        print("Product Price:", self.price)

product1 = Product("Laptop", 1000)
product2 = Product("Smartphone", 500)
product3 = Product("Headphones", 150)

product1.display()
product2.display()
product3.display()