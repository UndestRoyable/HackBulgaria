class Product:

    def __init__(self,name,stock_price,final_price):
        self.name = name
        self.stock_price = stock_price
        self.final_price = final_price

    def profit(self):
        profit = 0
        profit = (self.final_price - self.stock_price)
        return profit

    def __str__(self):
        return "{} {} {}".format(self.name, self.stock_price, self.final_price) 
        #this way in list_product() i can write only item and it will return in this case
        #name, stock_price, final_price

class Laptop(Product):

    def __init__(self, name, stock_price, final_price, diskspace, ram):
        super().__init__(name, stock_price, final_price)
        self.diskspace = diskspace
        self.ram = ram

    def print_laptop(self):
        return "{}, {}, {}, {}, {}".format(self.name, self.stock_price, self.final_price, self.diskspace, self.ram)


class Smartphone(Product):
    def __init__(self, name, stock_price, final_price,display_size,mega_pixels):
        super().__init__(name, stock_price, final_price)
        self.display_size = display_size
        self.mega_pixels = mega_pixels


class Store:
    _total_income = 0
    def __init__(self, name):
        self.name = name
        self.items = {}

    def load_new_products(self, item, count):
        if item in self.items:
            self.items[item] += count
        else:
            self.items[item] = count

    def list_products(self, item_class):
        for item in self.items:
            if isinstance(item,item_class):
                print(item)

    def sell_product(self, product):
        for item in self.items:
            if self.items[item] > 0:
                self.items[item] -= 1
                self._total_income += poduct.profit()
                return True
            else:
                return False

    def total_income(self):
        #print(self._total_income)
        pass


"""def main():
    
    new_product = Product('HP HackBook', 1000, 1243) #Creates product instance
    print("Profit after selling HP HackBook: ")
    new_product.profit()
#-----------------------------------------------------------------------------------
    new_laptop = Laptop('HP HackBook', 1000, 1243, 1000, 4)#Creates Laptop instance
    #new_laptop.print_laptop()
#----------------------------------------------------------------------------------
    new_smarthphone = Smartphone('Hack Phone', 500, 820, 7, 10)
#-----------------------------------------------------------------------------------
    new_store = Store('Laptop.bg')
    new_store.load_new_products(new_smarthphone, 2)
    new_store.load_new_products(new_laptop, 20)
#---------------------------------------------------------------------------------- 
    print("Items available in the store: ")
    new_store.list_products(Laptop)
    new_store.list_products(Smartphone)
#-----------------------------------------------------------------------------------
    print(new_store.sell_product(new_smarthphone)) # True
    print(new_store.sell_product(new_smarthphone)) # True
    print(new_store.sell_product(new_smarthphone))



if __name__ == "__main__":
    main()
"""