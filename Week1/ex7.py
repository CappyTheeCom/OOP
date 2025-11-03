class Product:

    def __init__(self, fnum,snum):
        self.fnum = fnum 
        self.snum = snum 
    
    def product(self):
        return self.fnum * self.snum



first_num = int(input("Enter first integer: "))
second_num = int(input("Enter second integer: "))

product = Product(first_num, second_num)


print(f"product: {product.product()}")